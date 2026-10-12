"""Forgejo API access shared by the cvportal scripts.

Token lookup order: FORGEJO_TOKEN env var, then the macOS Keychain item
named by KEYCHAIN_SERVICE. Requests go through curl so the system trust
store, which holds the LAN's private CA, is used.
"""

import json
import os
import re
import subprocess
import sys

URL = os.environ.get("FORGEJO_URL", "https://fed.home.vplan").rstrip("/")
USER = os.environ.get("FORGEJO_USER", "thefed")
KEYCHAIN_SERVICE = "cvportal-forgejo"
CURL = "/usr/bin/curl" if sys.platform == "darwin" else "curl"


def repo_name_from_remotes(remote_lines):
    """Name of the repo on this Forgejo that a clone pushes to, or '' if none."""
    host = re.escape(URL.split("//")[-1])
    for line in remote_lines:
        m = re.search(rf"{host}[:/0-9]*/[^/]+/([^/\s]+?)(\.git)?(\s|$)", line)
        if m:
            return m.group(1)
    return ""


class ApiError(Exception):
    pass


def token():
    value = os.environ.get("FORGEJO_TOKEN", "").strip()
    if value or sys.platform != "darwin":
        return value
    r = subprocess.run(
        ["security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
        capture_output=True, text=True,
    )
    return r.stdout.strip() if r.returncode == 0 else ""


def get(path, raw=False):
    """GET an API path. Returns (body, headers); body is None on 404."""
    tok = token()
    # The token goes to curl on stdin so it never appears in the process list.
    config = f'header = "Authorization: token {tok}"\n' if tok else ""
    r = subprocess.run(
        [CURL, "-sS", "--max-time", "20", "-K", "-", "-D", "-", f"{URL}/api/v1{path}"],
        input=config.encode(), capture_output=True,
    )
    if r.returncode != 0:
        raise ApiError(r.stderr.decode(errors="replace").strip() or f"curl exit {r.returncode}")
    out = r.stdout
    head = b""
    while out.startswith(b"HTTP/"):
        head, _, out = out.partition(b"\r\n\r\n")
    lines = head.decode(errors="replace").split("\r\n")
    status = int(lines[0].split()[1]) if lines and len(lines[0].split()) > 1 else 0
    headers = {k.strip().lower(): v.strip() for k, _, v in (l.partition(":") for l in lines[1:])}
    if status == 404:
        return None, headers
    if status >= 400 or status == 0:
        raise ApiError(f"HTTP {status} for {path}")
    text = out.decode(errors="replace")
    return (text if raw else json.loads(text)), headers


def get_all(path, limit=50):
    """Follow page= pagination until a short page."""
    items, page = [], 1
    sep = "&" if "?" in path else "?"
    while True:
        chunk, _ = get(f"{path}{sep}limit={limit}&page={page}")
        if not chunk:
            break
        items += chunk
        if len(chunk) < limit:
            break
        page += 1
    return items


def check():
    if not token():
        print(f"No token: set FORGEJO_TOKEN or add Keychain item '{KEYCHAIN_SERVICE}'.")
        return 1
    try:
        me, _ = get("/user")
        repos = get_all("/user/repos")
    except ApiError as exc:
        print(f"Token found, but the request failed: {exc}")
        return 1
    private = sum(1 for r in repos if r.get("private"))
    print(f"OK: signed in to {URL} as {me['login']}; {len(repos)} repos visible ({private} private).")
    return 0


if __name__ == "__main__":
    sys.exit(check())

#!/usr/bin/env python3
"""Print a resume's Markdown with its {{% contact "..." %}} placeholders filled in.

Fields come from data/contact.toml. With --with-address, the postal address from the
gitignored private/contact.toml (or CVPORTAL_PRIVATE_CONTACT) is added on its own line
above each contact line. Without it, an address is never printed, even if asked for.
usage: expand_contact.py RESUME.md [--with-address]
"""
import os
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLACEHOLDER = re.compile(r'\{\{[%<]\s*contact\s+"([^"]*)"\s*[%>]\}\}')
UNSET = "FILL IN"


def main():
    source, with_address = Path(sys.argv[1]), "--with-address" in sys.argv[2:]
    contact = tomllib.loads((ROOT / "data" / "contact.toml").read_text())
    contact.pop("address", None)
    address = ""
    if with_address:
        private = Path(os.environ.get("CVPORTAL_PRIVATE_CONTACT", ROOT / "private" / "contact.toml"))
        if not private.is_file():
            sys.exit(f"{private} not found: create it with an address = \"...\" line")
        address = tomllib.loads(private.read_text()).get("address", "").strip()
        if not address or UNSET in address:
            sys.exit(f"set address in {private} first")

    def fill(match):
        fields = [f.strip() for f in match.group(1).split(",") if f.strip() and f.strip() != "address"]
        line = " · ".join(str(contact[f]) for f in fields if contact.get(f))
        return f"{address}  \n{line}" if address else line

    sys.stdout.write(PLACEHOLDER.sub(fill, source.read_text()))


if __name__ == "__main__":
    main()

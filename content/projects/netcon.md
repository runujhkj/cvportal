---
title: "netcon — iOS Network Coverage Mapper"
status: "Submitted"
featured: true
summary: "A self-contained iOS app that passively measures Wi-Fi and cellular network quality as the user moves and renders results as a zoomable heatmap overlay on a map. No server, no account, no third-party SDKs."
tech: ["Swift", "SwiftUI", "CoreLocation", "CoreMotion", "CoreData", "MapKit", "CoreGraphics", "URLSession"]
problem: "Understanding real-world network quality in specific places — a building, a commute route, a campus — requires either expensive professional tools or trusting crowd-sourced data collected by someone else. There was no simple tool for building your own spatial network quality record tied to your own movements."
approach: "A background measurement pipeline runs randomized HEAD/GET probes to configurable endpoints via URLSession, computes median latency/jitter/packet-loss per host, and adapts probe cadence to movement (30s moving, 300s stationary via CMMotionActivityManager). A custom MapKit tile rasteriser subclasses MKTileOverlay to render the heatmap per tile request using manual Web-Mercator projection and zoom-adaptive power-of-2 grid snapping to eliminate tile-boundary jumping at zoom transitions."
current:
  - "Background measurement with adaptive cadence and CLLocationManager always-on mode."
  - "Core Data persistence with incremental per-cell tile statistics and rolling 7-day window."
  - "Custom heatmap rasteriser with Web-Mercator projection, confidence opacity ramp, and blob rendering mode."
  - "Multi-format export: zip bundle (manifest + JSONL + CSV + GeoJSON), standalone CSV, standalone GeoJSON FeatureCollection."
  - "Privacy: BSSID hashed with SHA-256 at ingest; optional ±25m coordinate fuzzing on export."
  - "BGProcessingTask + CLCircularRegion geofencing for re-wake on departure."
  - "~15 Swift source files; zero third-party dependencies."
next:
  - "App Store submission."
  - "Configurable probe endpoints and per-SSID filtering in UI."
  - "Tile export for offline map viewing."
repo_status: "Private; submission materials drafted."
---

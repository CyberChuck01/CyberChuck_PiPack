# 08 — Touchscreen dashboard

A **Seeed XIAO ESP32-C5** + **round touchscreen** shows live Kismet data in the
field without needing the attached monitor.

## Working pages
- **Summary** — top-level Kismet stats
- **Nearby APs** — list of nearby access points
- **GPS** — current fix (reads gpsd, which now listens on all interfaces — see
  [03-gps-gpsd.md](03-gps-gpsd.md))
- **Touch paging** between screens

## Data path
ESP32-C5 → Kismet REST API (with the API key from
[02-kismet-setup.md](02-kismet-setup.md)) over the `RaspAP` network → renders
on the round display.

Firmware lives in
[`../dashboard/firmware/xiao_c5_dashboard/`](../dashboard/firmware/xiao_c5_dashboard/).

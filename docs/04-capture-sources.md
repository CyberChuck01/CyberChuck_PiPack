# 04 — Capture sources

Radios feeding Kismet:

| Source | Interface | Notes |
|--------|-----------|-------|
| Pi 5 onboard Bluetooth | `hci0` | Bluetooth scanning source |
| Panda WiFi adapter #1 | `wlanX` | WiFi capture |
| Panda WiFi adapter #2 | `wlanY` | WiFi capture |

Add them in Kismet (UI → *Data Sources*, or `kismet_site.conf`). Both Panda
adapters need monitor mode, and neither should be the interface hosting the
`RaspAP` AP.

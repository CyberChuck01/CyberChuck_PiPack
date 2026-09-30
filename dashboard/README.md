# PiPack Dashboard

A Seeed **XIAO ESP32-C5** driving a **round touchscreen**, showing live Kismet
data in the field. See [../docs/08-dashboard.md](../docs/08-dashboard.md).

- `firmware/xiao_c5_dashboard/` — the ESP32-C5 sketch/firmware
- `server/` — notes on the Kismet REST endpoints the dashboard reads

## Pages (working)
- Summary · Nearby APs · GPS · touch paging

## Data path
XIAO C5 → Kismet REST API (API-key auth) over the `RaspAP` network → round
display.

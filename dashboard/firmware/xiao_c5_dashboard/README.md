# xiao_c5_dashboard firmware

Drop your ESP32-C5 sketch here (Arduino / PlatformIO).

Config it reads:
- `KISMET_HOST` / `KISMET_PORT` (default 2501)
- `KISMET_APIKEY` — scoped key from Kismet (see ../../docs/02-kismet-setup.md)
- WiFi creds for the `RaspAP` network

Endpoints used (see ../server/README.md):
- summary, device list (nearby APs), GPS location

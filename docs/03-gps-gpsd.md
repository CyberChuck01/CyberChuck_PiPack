# 03 — GPS via gpsd

GPS location tags every capture and feeds the dashboard's GPS page.

## The fix
By default gpsd only listens on localhost, so the ESP32-C5 dashboard couldn't
reach it. gpsd is reconfigured to **listen on all interfaces**.

Edit `/etc/default/gpsd` (example in
[`../config/gpsd.default`](../config/gpsd.default)):

```
GPSD_OPTIONS="-G -n"
```

- `-G` = listen on all addresses (not just localhost)
- `-n` = don't wait for a client before polling the GPS

Then:
```bash
sudo systemctl restart gpsd
gpspipe -w -n 5   # sanity check you're getting fixes
```

> Security note: `-G` exposes gpsd on the network. Fine on the isolated
> `RaspAP` net; don't do it on an untrusted LAN.

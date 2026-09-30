# PiPack

A portable wardriving / RF-recon rig built on a **Raspberry Pi 5** running
**DragonOS**, driving **Kismet** for WiFi + Bluetooth capture, GPS logging,
ADS-B aircraft tracking, Flock Safety camera detection, and a small
touchscreen dashboard.

Built and maintained by **[CyberChuck01](https://github.com/CyberChuck01)**
([YouTube: cyberchuck01](https://www.youtube.com/@cyberchuck01)).

---

## Credit where it's due — akrex

The PiPack runs on top of the **DragonOS / Trixie uConsole image built by
akrex** — `ak-rex` on GitHub, known as **"Rex"** on the ClockworkPi forums.
None of this would exist without the enormous amount of work he puts into
building, patching, and maintaining custom OS images for the uConsole and
DevTerm community.

- GitHub: <https://github.com/ak-rex>
- APT repo: <https://github.com/ak-rex/ClockworkPi-apt>
- His OS threads live on the [ClockworkPi forums](https://forum.clockworkpi.com/tag/uconsole)

**This repository does not redistribute Rex's images.** Everything here is my
own configuration, scripts, and add-ons that sit *on top of* his base image.
Grab the OS from Rex directly, then layer this on. If you use his work, go
support him.

See [CREDITS.md](CREDITS.md) for the full list of upstream projects.

---

## Hardware

| Part | Role |
|------|------|
| Raspberry Pi 5 | Main compute, runs DragonOS + Kismet |
| Pi 5 onboard Bluetooth | Bluetooth capture source |
| 2× Panda WiFi adapters | WiFi capture sources |
| GPS receiver (via gpsd) | Location tagging |
| Nooelec RTL-SDR V5 | ADS-B (1090 MHz) aircraft tracking |
| Seeed Studio round touchscreen + XIAO ESP32-C5 | Dashboard display |

The Pi broadcasts its own AP on SSID `RaspAP` and also has a keyboard/monitor
attached directly for bench work.

---

## What's in here (the modifications)

Each item below has a detailed writeup in [`docs/`](docs/):

1. **Base OS from akrex** — [`docs/01-base-os-akrex.md`](docs/01-base-os-akrex.md)
2. **Kismet setup + API-key auth** (moved off the default `admin/admin`) — [`docs/02-kismet-setup.md`](docs/02-kismet-setup.md)
3. **GPS via gpsd** listening on all interfaces so the dashboard can reach it — [`docs/03-gps-gpsd.md`](docs/03-gps-gpsd.md)
4. **Multiple capture sources** (Pi onboard Bluetooth + 2× Panda WiFi adapters) — [`docs/04-capture-sources.md`](docs/04-capture-sources.md)
5. **ADS-B tracking** with the RTL-SDR V5 + the `log_types` fix so ADS-B devices actually log — [`docs/05-adsb.md`](docs/05-adsb.md)
6. **Flock Safety camera detection** *(⚠️ work in progress)* — scan Kismet-logged MACs against known Flock OUI prefixes — [`docs/06-flock-detection.md`](docs/06-flock-detection.md)
7. **WDGWars upload** — export WiFi/BT (`wiglecsv`) + ADS-B and push to [wdgwars.pl](https://wdgwars.pl) — [`docs/07-wdgwars-upload.md`](docs/07-wdgwars-upload.md)
8. **Touchscreen dashboard** (summary / nearby-APs / GPS pages, touch paging) — [`docs/08-dashboard.md`](docs/08-dashboard.md)

---

## Automation

After each wardrive session, [`scripts/postwardrive.sh`](scripts/postwardrive.sh)
runs the whole export chain: WiGLE export → ADS-B export → Flock scan →
WDGWars upload. Wire it to a cron job, a hotkey, or run it by hand.

```bash
./scripts/postwardrive.sh
```

---

## Repo layout

```
PiPack/
├── docs/        Per-modification setup + notes
├── scripts/     Automation + export + detection scripts
├── config/      Example gpsd / Kismet config snippets
└── dashboard/   ESP32-C5 firmware + server-side notes
```

---

## Disclaimer

For educational and lawful use only. Passive RF monitoring, wardriving, and
counter-surveillance laws vary by jurisdiction — know yours. You are
responsible for how you use this.

## License

[MIT](LICENSE) — covers my own code and configs in this repo only. The
underlying OS image and all upstream tools keep their own licenses.

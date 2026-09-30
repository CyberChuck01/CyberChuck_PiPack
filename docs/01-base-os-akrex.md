# 01 — Base OS (from akrex)

The PiPack runs **DragonOS** on a **Raspberry Pi 5**, using the
**uConsole / Trixie image built by akrex** (`ak-rex` on GitHub, "Rex" on the
ClockworkPi forums).

## Get the image from Rex directly

- GitHub: <https://github.com/ak-rex>
- APT repo: <https://github.com/ak-rex/ClockworkPi-apt>
- OS release threads: <https://forum.clockworkpi.com/tag/uconsole>

Flash his DragonOS/Trixie image, boot, update, then layer the PiPack configs
and scripts from this repo on top. **Do not redistribute his image** — point
people back to his sources.

## PiPack-specific base tweaks
- AP broadcast on SSID `RaspAP` (via RaspAP) for headless access in the field.
- Keyboard + monitor attached directly to the Pi for bench work.

# 07 — WDGWars upload

Wardrive data gets uploaded to **WDGWars** (<https://wdgwars.pl>).

## What gets uploaded
- WiFi + Bluetooth as `wiglecsv` (Kismet exports this natively)
- ADS-B export

## Flow
1. `scripts/wigle_export.sh` — export the session to `.wiglecsv`
2. `scripts/adsb_export.sh` — export ADS-B
3. `scripts/wdgwars_upload.py` — push the files to WDGWars

Put your WDGWars credentials/token in `secrets.env` (gitignored):
```bash
WDGWARS_TOKEN=your_token_here
```

> Confirm the exact upload endpoint/method WDGWars expects and fill it into
> `wdgwars_upload.py` — the script is scaffolded with a clearly marked TODO.

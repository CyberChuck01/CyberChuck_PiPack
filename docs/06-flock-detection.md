# 06 — Flock Safety camera detection

> ⚠️ **Work in progress.** OUI matching is functional but the known-OUI
> list is incomplete and still being validated in the field — expect
> false negatives (and possibly false positives) until it's dialed in.


After each wardrive, scan the WiFi devices Kismet logged and flag any whose MAC
prefix (OUI) matches known **Flock Safety** camera hardware.

## How it works
- Pull device MACs from the latest kismetdb (or the exported wiglecsv).
- Compare each MAC's OUI (first 3 octets) against a list of known Flock OUIs.
- Print/log any matches with SSID, signal, and GPS if available.

Run:
```bash
python3 scripts/flock_detect.py --db /path/to/latest.kismet
# or against an exported CSV:
python3 scripts/flock_detect.py --csv /path/to/session.wiglecsv
```

## Maintaining the OUI list
The known-OUI list lives in
[`../scripts/flock_ouis.txt`](../scripts/flock_ouis.txt), one prefix per line.
**Paste your verified list there** — OUIs change and get added over time, so
keep it current. The file ships with placeholders you must replace/verify.

This runs automatically inside
[`../scripts/postwardrive.sh`](../scripts/postwardrive.sh).

#!/usr/bin/env bash
# adsb_export.sh — export ADS-B devices from the latest Kismet session.
# Relies on the log_types=...,adsb fix (see docs/05-adsb.md) so ADS-B is logged.
set -euo pipefail

KISMET_LOG_DIR="${KISMET_LOG_DIR:-$HOME/.kismet}"
OUT_DIR="${OUT_DIR:-$HOME/wardrives}"
mkdir -p "$OUT_DIR"

latest="$(ls -t "$KISMET_LOG_DIR"/*.kismet 2>/dev/null | head -n1 || true)"
if [[ -z "${latest:-}" ]]; then
  echo "[!] No .kismet files found in $KISMET_LOG_DIR" >&2
  exit 1
fi

base="$(basename "${latest%.kismet}")"
out="$OUT_DIR/${base}_adsb.csv"
echo "[*] exporting ADS-B from $latest -> $out"

# kismetdb_dump_devices emits JSON; pull ADS-B (phy 'RTLADSB') rows.
# Adjust the phyname/fields to match your Kismet version if needed.
kismetdb_dump_devices --in "$latest" --skip-clean 2>/dev/null \
  | python3 -c '
import sys, json, csv
w = csv.writer(sys.stdout)
w.writerow(["icao","callsign","last_time","lat","lon","alt"])
for line in sys.stdin:
    line=line.strip().rstrip(",")
    if not line or line in "[]": continue
    try: d=json.loads(line)
    except Exception: continue
    phy=str(d.get("kismet.device.base.phyname",""))
    if "ADSB" not in phy.upper(): continue
    w.writerow([
        d.get("kismet.device.base.macaddr",""),
        d.get("kismet.device.base.name",""),
        d.get("kismet.device.base.last_time",""),
        d.get("kismet.common.location.avg_lat",""),
        d.get("kismet.common.location.avg_lon",""),
        d.get("kismet.common.location.avg_alt",""),
    ])
' > "$out"
echo "$out"

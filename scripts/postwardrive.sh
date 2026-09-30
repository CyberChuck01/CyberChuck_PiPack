#!/usr/bin/env bash
# postwardrive.sh — run after each wardrive session.
# Chain: WiGLE export -> ADS-B export -> Flock scan -> WDGWars upload.
set -euo pipefail
cd "$(dirname "$0")/.."          # repo root

# Load secrets if present (KISMET_APIKEY, WDGWARS_TOKEN, etc.)
if [[ -f secrets.env ]]; then
  set -a; source secrets.env; set +a
fi

echo "=== [1/4] WiGLE export ==="
wigle="$(bash scripts/wigle_export.sh)"

echo "=== [2/4] ADS-B export ==="
adsb="$(bash scripts/adsb_export.sh || true)"

echo "=== [3/4] Flock camera scan ==="
python3 scripts/flock_detect.py --csv "$wigle" || true

echo "=== [4/4] WDGWars upload ==="
if [[ -n "${WDGWARS_TOKEN:-}" ]]; then
  python3 scripts/wdgwars_upload.py "$wigle" ${adsb:+"$adsb"} || true
else
  echo "[i] WDGWARS_TOKEN not set — skipping upload."
fi

echo "=== done ==="

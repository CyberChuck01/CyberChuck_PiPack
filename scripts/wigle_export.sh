#!/usr/bin/env bash
# wigle_export.sh — export the most recent Kismet session to .wiglecsv
# (WiFi + Bluetooth) using kismetdb_to_wiglecsv.
set -euo pipefail

KISMET_LOG_DIR="${KISMET_LOG_DIR:-$HOME/.kismet}"    # adjust if yours differs
OUT_DIR="${OUT_DIR:-$HOME/wardrives}"
mkdir -p "$OUT_DIR"

latest="$(ls -t "$KISMET_LOG_DIR"/*.kismet 2>/dev/null | head -n1 || true)"
if [[ -z "${latest:-}" ]]; then
  echo "[!] No .kismet files found in $KISMET_LOG_DIR" >&2
  exit 1
fi

base="$(basename "${latest%.kismet}")"
out="$OUT_DIR/$base.wiglecsv"
echo "[*] exporting $latest -> $out"
kismetdb_to_wiglecsv --in "$latest" --out "$out"
echo "$out"

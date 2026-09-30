#!/usr/bin/env python3
"""
flock_detect.py — flag WiFi devices whose MAC OUI matches known Flock Safety
camera hardware, from a Kismet .kismet db or an exported .wiglecsv.

Usage:
    python3 flock_detect.py --db /path/to/latest.kismet
    python3 flock_detect.py --csv /path/to/session.wiglecsv
    python3 flock_detect.py --db latest.kismet --ouis scripts/flock_ouis.txt

Exit code is 0 always; matches are printed to stdout and written to
flock_matches.csv next to the input. Wire this into postwardrive.sh.
"""
import argparse
import csv
import os
import sqlite3
import sys

DEFAULT_OUI_FILE = os.path.join(os.path.dirname(__file__), "flock_ouis.txt")


def load_ouis(path):
    """Load OUI prefixes, normalized to uppercase 'AA:BB:CC'."""
    ouis = set()
    if not os.path.exists(path):
        sys.stderr.write(f"[!] OUI file not found: {path}\n")
        return ouis
    with open(path) as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if not line:
                continue
            norm = line.upper().replace("-", ":")
            parts = norm.split(":")[:3]
            if len(parts) == 3:
                ouis.add(":".join(p.zfill(2) for p in parts))
    return ouis


def oui_of(mac):
    parts = mac.upper().replace("-", ":").split(":")
    if len(parts) < 3:
        return None
    return ":".join(p.zfill(2) for p in parts[:3])


def from_kismetdb(db_path):
    """Yield (mac, ssid, signal, lat, lon) from a kismet sqlite db."""
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    # 'devices' table has devmac plus min/max lat/lon and strongest_signal.
    try:
        cur.execute(
            "SELECT devmac, strongest_signal, min_lat, min_lon "
            "FROM devices"
        )
    except sqlite3.OperationalError as e:
        sys.stderr.write(f"[!] Could not read devices table: {e}\n")
        con.close()
        return
    for row in cur.fetchall():
        yield (row["devmac"], "", row["strongest_signal"],
               row["min_lat"], row["min_lon"])
    con.close()


def from_wiglecsv(csv_path):
    """Yield (mac, ssid, signal, lat, lon) from a wiglecsv export."""
    with open(csv_path, newline="") as fh:
        # wiglecsv has a 1-line pre-header, then a real header row.
        first = fh.readline()
        if "MAC" not in first:
            pass  # already at header
        reader = csv.DictReader(fh)
        for r in reader:
            mac = r.get("MAC") or r.get("mac") or ""
            yield (mac,
                   r.get("SSID", ""),
                   r.get("RSSI", r.get("Signal", "")),
                   r.get("CurrentLatitude", r.get("Lat", "")),
                   r.get("CurrentLongitude", r.get("Lon", "")))


def main():
    ap = argparse.ArgumentParser(description="Flock camera OUI scan")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--db", help="path to a .kismet sqlite db")
    src.add_argument("--csv", help="path to a .wiglecsv export")
    ap.add_argument("--ouis", default=DEFAULT_OUI_FILE,
                    help="OUI prefix list (default: scripts/flock_ouis.txt)")
    args = ap.parse_args()

    ouis = load_ouis(args.ouis)
    if not ouis:
        sys.stderr.write("[!] No OUIs loaded — nothing to match against. "
                         "Populate flock_ouis.txt.\n")

    rows = from_kismetdb(args.db) if args.db else from_wiglecsv(args.csv)
    src_path = args.db or args.csv
    out_path = os.path.join(os.path.dirname(os.path.abspath(src_path)),
                            "flock_matches.csv")

    matches = []
    for mac, ssid, sig, lat, lon in rows:
        if not mac:
            continue
        if oui_of(mac) in ouis:
            matches.append((mac, ssid, sig, lat, lon))

    if matches:
        print(f"[!!] {len(matches)} possible Flock device(s):")
        with open(out_path, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["MAC", "SSID", "Signal", "Lat", "Lon"])
            for m in matches:
                w.writerow(m)
                print(f"     {m[0]}  ssid={m[1]!r}  sig={m[2]}  "
                      f"@ {m[3]},{m[4]}")
        print(f"[+] Wrote {out_path}")
    else:
        print("[+] No Flock OUI matches in this session.")


if __name__ == "__main__":
    main()

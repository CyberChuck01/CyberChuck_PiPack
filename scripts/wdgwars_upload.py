#!/usr/bin/env python3
"""
wdgwars_upload.py — push exported wardrive files to WDGWars (wdgwars.pl).

Usage:
    python3 wdgwars_upload.py file1.wiglecsv [file2.csv ...]

Reads WDGWARS_TOKEN from the environment (source secrets.env first):
    set -a; source secrets.env; set +a
    python3 scripts/wdgwars_upload.py session.wiglecsv adsb.csv

NOTE: confirm the exact upload endpoint + field names WDGWars expects and fill
them into UPLOAD_URL / the POST call below. Left as a clearly marked TODO so
nothing silently uploads to the wrong place.
"""
import os
import sys

# TODO: set this to the real WDGWars upload endpoint.
UPLOAD_URL = os.environ.get("WDGWARS_URL", "https://wdgwars.pl/UPLOAD_ENDPOINT")


def main(paths):
    token = os.environ.get("WDGWARS_TOKEN")
    if not token:
        sys.exit("[!] WDGWARS_TOKEN not set. Source secrets.env first.")
    if "UPLOAD_ENDPOINT" in UPLOAD_URL:
        sys.exit("[!] Set the real WDGWars endpoint (UPLOAD_URL / WDGWARS_URL) "
                 "before uploading.")

    try:
        import requests
    except ImportError:
        sys.exit("[!] pip install requests")

    for p in paths:
        if not os.path.exists(p):
            print(f"[!] skip missing: {p}")
            continue
        with open(p, "rb") as fh:
            files = {"file": (os.path.basename(p), fh)}
            headers = {"Authorization": f"Bearer {token}"}
            print(f"[*] uploading {p} ...")
            resp = requests.post(UPLOAD_URL, files=files, headers=headers,
                                 timeout=60)
            print(f"    -> HTTP {resp.status_code}: {resp.text[:200]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])

# 02 — Kismet setup + API-key auth

Kismet is the core capture engine (WiFi + Bluetooth + ADS-B feeds).

## Auth
The box originally shipped on the default `admin/admin` login. **That's been
retired** — the PiPack now uses **API-key authentication** for the REST API
that the dashboard talks to.

1. Log into the Kismet web UI once and set a real admin user/password.
2. Create a scoped API key for the dashboard (Kismet UI → *Settings → Login &
   Users → API keys*, or via the REST API).
3. Store the key OUTSIDE the repo. Put it in `secrets.env` (gitignored):

   ```bash
   # secrets.env  (DO NOT COMMIT)
   KISMET_APIKEY=your_key_here
   KISMET_HOST=127.0.0.1
   KISMET_PORT=2501
   ```

See [`../config/kismet_site.conf.example`](../config/kismet_site.conf.example)
for httpd/site notes.

## Capture sources
Configured in Kismet — see [04-capture-sources.md](04-capture-sources.md).

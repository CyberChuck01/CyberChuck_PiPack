# 05 — ADS-B aircraft tracking

A **Nooelec RTL-SDR V5** receives 1090 MHz ADS-B and feeds it into Kismet.

## The log_types fix
ADS-B devices weren't being written to the kismetdb because the ADS-B log type
wasn't enabled. Add the missing `log_types` entry so ADS-B logs correctly.

See [`../config/kismet_logging.conf`](../config/kismet_logging.conf):

```
log_types=kismet,pcapng,wiglecsv,adsb
```

Restart Kismet and confirm ADS-B devices appear and persist in the db.

## Export
ADS-B is exported as part of the post-wardrive chain — see
[`../scripts/adsb_export.sh`](../scripts/adsb_export.sh).

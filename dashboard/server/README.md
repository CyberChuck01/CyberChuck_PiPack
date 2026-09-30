# Kismet REST endpoints used by the dashboard

All calls authenticate with the dashboard's API key.

| Page       | Endpoint (Kismet REST) |
|------------|------------------------|
| Summary    | `/system/status.json` |
| Nearby APs | `/devices/views/phydot11_accesspoints/devices.json` |
| GPS        | `/gps/location.json` |

> Endpoint names vary slightly by Kismet version — confirm against your build's
> REST docs: <https://www.kismetwireless.net/docs/api/rest/>

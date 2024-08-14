# CDN IP Geolocation

* Fork this repository and Enable Actions Workflow.

# STEPS

### Extract IP
* Edit [extractip/config.txt](./extractip/config.txt) and put your configs, get your exracted IPs at `exteactip/ex.txt`.

### Range Maker
* Edit [rangemaker/singleip.txt](./rangemaker/singleip.txt) and put IPs from step above, get your ranges at `rangemaker/exrange.txt`.

### Appender + IP Geolocations
* Edit [files/ranges.txt](./files/ranges.txt) and put your CDN ranges from step above, get IP Geolocations at `files/countries.txt`.

### Certain Address Replacer
* For an extra feature, you could replace certain config addresses as `addresses_to_change` variable in [`limitbreaker/limitbreaker.py`](./limitbreaker/limitbreaker.py), by putting your configs in [limitbreaker/limited.txt](./limitbreaker/limited.txt). New configs with replaced addresses will be at `limitbreaker/limitbreaker.txt`.

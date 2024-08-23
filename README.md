# CDN IP Geolocation

* Fork this repository and Enable Actions Workflow.

# STEPS

### Extract IP
🧧 Edit [extractip/config.txt](./extractip/config.txt) and put your configs, get your exracted IPs at `exteactip/ex.txt`.

### Range Maker
🧧 Edit [rangemaker/singleip.txt](./rangemaker/singleip.txt) and put IPs from step above, get your ranges at `rangemaker/exrange.txt`.

### Appender + IP Geolocations
🧧 Edit [files/ranges.txt](./files/ranges.txt) and put your CDN ranges from step above, get IP Geolocations at `files/countries.txt`.

![0](https://raw.githubusercontent.com/Surfboardv2ray/IPGeolocation/main/.github/media/line.gif)
### CHAIN REACTION
🧧 Adding your configs to [chainreaction/config.txt](./chainreaction/config.txt) will trigger a "Chain Reaction" that will do all the steps above subsequently, with a single effort.

⚠️ BEWARE that Chain Reaction Step 3, or "IP Geolocations" is time taking, so adjust the number of your configs accordingly and avoid unnecessary triggers. Or simply cancel the workflow if you did, by mistake.

![0](https://raw.githubusercontent.com/Surfboardv2ray/IPGeolocation/main/.github/media/line.gif)
### Certain Address Replacer
🧧 For an extra feature, you could replace certain config addresses as `addresses_to_change` variable in [limitbreaker/limitbreaker.py](./limitbreaker/limitbreaker.py), by putting your configs in [limitbreaker/limited.txt](./limitbreaker/limited.txt). New configs with replaced addresses will be at `limitbreaker/limitbreaker.txt`.

### Domain Resolve
🧧 As the name calls, put your domains in in [domainresolve/domain.txt](./domainresolve/domain.txt). New configs with replaced addresses will be at `domainresolve/resolved+ip.txt`.

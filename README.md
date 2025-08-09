# h00th00t
## Sub-Byte Binary Underflow in WiFi Devices
## Warning: Test With Extreme Care
### Warning: USE AT YOUR OWN PERIL
## Summary
Sending WiFi beacons where the SSID is set to some non-byte number of bits and a poorly matching SSID length breaks many random WiFi devices in range.  
  
Some devices freeze, some reboot, some break, some brick.  
Results are superfically non-deterministic and further study is required.  
  
In theory, it could be leveraged into other forms of binary exploitation.  
  
List of devices vulnerable is unknown and likely very large.

## Mechanism of Action
At best judgement, the failure of alignment of the bits in the SSID field causes alignment down to deeper levels of the system, possibly down to the processor, causing difficult to predict consequences.

## Impact
Testing is very challenging as it requires being out of range of all other WiFi devices during testing, but anecdotal evidence suggests some non-trivial percentage of all WiFi devices can be impacted in varied ways.

## Hooting (usage)
**DO NOT TEST IN RANGE OF ANY DEVICE YOU ARE UNWILLING TO DAMAGE**
_prerequisites_
1. Linux with bash (tested on fully upgraded Kali Linux 2025.2 on Raspberry Pi 5)
2. Python3 (tested on Python 3.13.3)
3. [Scapy](https://scapy.readthedocs.io/en/latest/installation.html) (tested on Scapy 2.6.13)
4. [A wifi device capable of monitor mode](https://www.stationx.net/best-wifi-adapters-for-kali-linux/) (tested with Alfa AWUS036ACH)

_running_
1. Set wifi device to monitor mode `bash wifi_monitor_mode.sh`
   * for usage see note at the top of [wifi_monitor_mode.sh](./wifi_monitor_mode.sh)
2. Optional: edit line `4` and `5` of [h00thoot.py](./h00th00t.py) to match your sender and wifi device preferences
   * Defaults to random source MAC and device wlan1
3. Install 
4. Uncomment line `38` of [h00thoot.py](./h00th00t.py)
5. `sudo python h00th00t.py`
---
![Stolas uwu~](./assets/stolas-headdesk.gif)

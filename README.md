# h00th00t
## Sub-Byte Binary Underflow in WiFi Devices
## Warning: Test With Extreme Care
### Summary
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
1. Install Scapy
2. Uncomment line 19 of h00thoot.py
3. `python h00th00t.py`
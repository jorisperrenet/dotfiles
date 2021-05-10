#!/usr/bin/env bash

rofi="rofi -theme $HOME/.config/rofi/applet.rasi"
title=' Network '

## Get info
STATUS="$(nmcli radio wifi)"

if (ping -c 1 yahoo.com || ping -c 1 google.com) &>/dev/null; then
    connect="睊"
	SSID="﬉ $(iwgetid -r)"
	PIP="$(curl ifconfig.me -s -m 1)"
else
    connect="直"
    SSID="Disconnected"
    PIP="Not Available"
fi

settings=""

## Main
descr="$SSID  :  $PIP"
option="$settings\n$connect"
name='#textbox-prompt-colon { str: "'$title'"; }'
chosen=$(echo -e $option | $rofi -monitor -1 -dmenu -p "$descr" -theme-str "$name")
case $chosen in
    $connect)
		if [[ $STATUS == *"enable"* ]]; then
			nmcli radio wifi off
		else
			nmcli radio wifi on
		fi
        ;;
    $settings)
        $TERMINAL -e nmtui
        ;;
esac


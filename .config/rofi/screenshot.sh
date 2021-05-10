#!/usr/bin/env bash

rofi="rofi -theme $HOME/.config/rofi/applet.rasi"
app='gnome-screenshot'
title=' Screenshot '

# Options
screen=""
window=""
area=""

descr="App : $app"
option="$screen\n$area\n$window"
name='#textbox-prompt-colon { str: "'$title'"; }'
chosen=$(echo -e $option | $rofi -monitor -1 -dmenu -p "$descr" -theme-str "$name")
case $chosen in
    $screen)
        options=""
        ;;
    $area)
        options="-a"
        ;;
    $window)
        options="-w"
        ;;
esac

dirname="$HOME/Pictures/screenshots"
file="$(date +'%Y_%b_%d_%H:%M:%S').jpg"
if [ -n "$chosen" ]; then
    $app -f "$dirname/$file" "$options";
fi


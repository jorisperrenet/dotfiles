#!/usr/bin/env bash

rofi="rofi -theme $HOME/.config/rofi/applet.rasi"
title=' Menu '
font='monospace 11'

programs="Dmenu"
network="Network"
power="Power"
screenshot="Screenshot"

## Main
option="$programs\n$power\n$network\n$screenshot"
descr="Program  :  Select"
name='#textbox-prompt-colon { str: "'$title'"; }'
name2='#element { font: "'$font'"; }'
chosen=$(echo -e $option | $rofi -monitor -1 -dmenu -p "$descr" -theme-str "$name" -theme-str "$name2")
case $chosen in
    $programs)
        bash $HOME/.config/rofi/launcher.sh
        ;;
    $network)
        bash $HOME/.config/rofi/network.sh
        ;;
    $power)
        bash $HOME/.config/rofi/power.sh
        ;;
    $screenshot)
        bash $HOME/.config/rofi/screenshot.sh
        ;;
esac


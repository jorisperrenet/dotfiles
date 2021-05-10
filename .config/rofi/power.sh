#!/usr/bin/env bash

rofi="rofi -theme $HOME/.config/rofi/applet.rasi"
prompt="$HOME/.config/rofi/promptmenu.sh"
title=' Power '

lock=""
shutdown=""
# log_out=""
log_out=""
reboot=""

confirm() {
    conf=$(rofi -theme "$HOME/.config/rofi/confirm.rasi" \
                -monitor -1 \
                -dmenu \
                -p "Are You Sure?" \
                -theme-str '#textbox-prompt-colon { str: " Shutdown "; }')
    if [[ $conf == "" || $conf == "no" || $conf == "n" || $conf == "N" ]]; then
        echo false
    else
        echo true
    fi
}

## Main
option="$lock\n$shutdown\n$log_out\n$reboot"
descr="Uptime  :  $(uptime -p | sed -e 's/up //g')"
name='#textbox-prompt-colon { str: "'$title'"; }'
chosen=$(echo -e $option | $rofi -monitor -1 -dmenu -p "$descr" -theme-str "$name")
case $chosen in
    $lock)
        i3lock -e -f -c 000000
        ;;
    $shutdown)
        bash $prompt --yes-command "shutdown now" --query "Shutdown?"
        ;;
    $log_out)
        bash $prompt --yes-command "i3-msg exit" --query "Exit i3?"
        ;;
    $reboot)
        bash $prompt --yes-command "reboot" --query "Reboot?"
        ;;
esac


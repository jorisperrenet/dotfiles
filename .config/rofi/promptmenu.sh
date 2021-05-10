#!/bin/bash

rofi_command="rofi -theme applet.rasi"

### Options ###
yes_text="Confirm"
no_text="Cancel"
query="Are you sure?"
descr="There is no turning back."
font="monospace 20"
# Parse the args
if [[ $# -eq 0 ]]; then
    echo -e "Usage: promptmenu -y <command>"
    echo -e "All the options:\n" \
        "\e[35mREQUIRED  [ -y | --yes-command ] <command>\n" \
        "\e[34mOPTIONNAL [ -n | --no-command ] <command>\n" \
        "\e[34mOPTIONNAL [ -o | --yes-text ] <text>\n" \
        "\e[34mOPTIONNAL [ -c | --no-text ] <text>\n" \
        "\e[34mOPTIONNAL [ -d | --font ] txt\n" \
        "\e[34mOPTIONNAL [ -q | --query ] txt\n" \
        "\e[34mOPTIONNAL [ -d | --descr ] txt"
    exit 1
else
    while [ $# -ne 0 ]; do
        case "$1" in
            -o | --yes-text)
                [ -n "$2" ] && yes_text="$2" || yes_text=""
                shift
                ;;
            -c | --no-text)
                [ -n "$2" ] && no_text="$2" || no_text=""
                shift
                ;;
            -y | --yes-command) # Required
                [ -n "$2" ] && yes_command="$2"
                shift
                ;;
            -n | --no-command)
                [ -n "$2" ] && no_command="$2"
                shift
                ;;
            -q | --query)
                [ -n "$2" ] && query="$2"
                shift
                ;;
            -d | --descr)
                [ -n "$2" ] && descr="$2"
                shift
                ;;
            -f | --font)
                [ -n "$2" ] && font="$2"
                shift
                ;;
        esac
        shift
    done
fi
# Variable passed to rofi
options="$yes_text\n$no_text"

name='#textbox-prompt-colon { str: "'$query'"; }'
name2='#element { font: "'$font'"; }'
chosen="$(echo -e "$options" | $rofi_command -dmenu -p "$descr" -theme-str "$name" -theme-str "$name2" -a 0 -u 1)"
case $chosen in
    $yes_text)
        eval "$yes_command"
        ;;
    $no_text)
        eval "$no_command"
        ;;
esac


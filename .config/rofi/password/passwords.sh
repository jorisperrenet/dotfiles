#!/usr/bin/env bash
dir="$HOME/Desktop/encryptie/rofi"
encr="$dir/interface.py"

enter_passwd() {
    rofi -theme "$HOME/.config/rofi/password/passwd.rasi" \
         -monitor -1 \
         -dmenu \
         -p "$1" \
         -theme-str '#textbox-prompt-colon { str: " Passwords "; }'
}

get_text() {
    count=0
    text="false"
    while [ "$text" == "false" ]; do
        if [[ $count -eq 0 ]]; then
            passwd=$(enter_passwd "Enter Your Password:")
        else
            passwd=$(enter_passwd "Wrong, Enter Your Password ($count):")
        fi
        if [ -z "$passwd" ]; then
            exit
        fi
        text=$(python3 "$encr" "$passwd")
        count=$(($count+1))
    done
}

get_info() {
    python3 "$dir/search.py" "$text" "search" "$want" |\
          $rofi -theme-str "$name" -theme-str "$name2"
}

menu() {
    ch1='1) To show a password'
    ch2='2) To add a password'
    ch3='3) To change a password'
    ch4='4) To encrypt or decrypt a file'
    ch5='5) To change the main password'
    ch6='6) To generate a new password'
    option="$ch1\n$ch2\n$ch3\n$ch4\n$ch5\n$ch6"
    rofi="rofi -theme $HOME/.config/rofi/password/choice.rasi -monitor -1 -i -dmenu -p "
    title=" Menu "
    name='#textbox-prompt-colon { str: "'$title'"; }'
    name2='configuration { lines: 3; }'
    chosen=$(echo -e "$option" | $rofi -theme-str "$name" -theme-str "$name2")
    case $chosen in
        "$ch1")
            title=" Search "
            name='#textbox-prompt-colon { str: "'$title'"; }'
            name2='configuration { lines: 10; }'
            want=$(python3 "$dir/search.py" "$text" "get" |\
                   $rofi -theme-str "$name" -theme-str "$name2")
            line=$(get_info)
            while [ -n "$line" ]; do
                cmd=$(python3 "$dir/search.py" "cmd" "$line")
                eval "$cmd"
                line=$(get_info)
                read -r  # wait until enter is pressed to restart
            done
            # echo python3 "$dir/search.py" "cmd" "$(getinfo)"
            # echo get_info



            ;;
        "$ch2")
            bash "$HOME/.config/rofi/network.sh"
            ;;
        "$ch3")
            bash "$HOME/.config/rofi/power.sh"
            ;;
        "$ch4")
            bash "$HOME/.config/rofi/screenshot.sh"
            ;;
        "$ch5")
            bash "$HOME/.config/rofi/screenshot.sh"
            ;;
        "$ch6")
            bash "$HOME/.config/rofi/screenshot.sh"
            ;;
    esac
}

get_text
menu

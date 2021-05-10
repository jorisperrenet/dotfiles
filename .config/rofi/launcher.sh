#!/usr/bin/env bash

theme="config.rasi"
dir="$HOME/.config/rofi/"

rofi -monitor -1 -no-lazy-grab -show drun -theme $dir/"$theme"

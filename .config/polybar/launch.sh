#!/bin/bash

# Terminate already running bar instances
pkill polybar

# Wait until the processes have been shut down
while pgrep polybar >/dev/null; do sleep 1; done

## Launch
if [ "$ON_LAPTOP" = true ]; then
    echo "on laptop"
    polybar laptop &
else
    polybar main &
fi

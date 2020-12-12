#!/bin/sh
tmux new-session -c "$(find /home/daniel -not -path '*/\.*' -maxdepth 3 -type d | rofi -dmenu)"

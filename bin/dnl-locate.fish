#!/bin/bash

xdg-open "$(rg /home/daniel --files --ignore=node_modules,vendor | rofi -threads 0 -i -p 'file' -dmenu)"

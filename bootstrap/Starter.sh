#!/bin/bash

cd /home/daniel

HOME='/home/daniel'

mkdir -p $HOME/.config

git clone https://dnlcorrea@github.com/dnlcorrea/dot .dot
git clone https://gitlab.com/dwt1/wallpapers

wal -i wallpapers

ln -sf $HOME/.dot/.xinitrc .xinitrc
ln -sf $HOME/.dot/qtile .config/
ln -sf $HOME/.dot/bin .

rm -v .bashrc .gitignore .zshrc

git config --global user.email "daniel@31solutions.com"
git config --global user.name "Daniel Correa"

# AUR
git clone https://aur.archlinux.org/yay.git
cd yay
yes | makepkg -si

cd ..

yay -S --no-confirm dropbox rofi-greenclip

# FZF
git clone https://github.com/junegunn/fzf .fzf
cd .fzf
yes | bash install

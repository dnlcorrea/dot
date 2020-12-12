#!/usr/bin/env bash

FONTDIR="$HOME/.local/share/fonts/"
tmp='fooTEMPman'

mkdir $tmp

cp -v "$1" $tmp; cd $tmp

unzip "$1"

mv -v *.ttf *.otf $FONTDIR

cd ..

rm -vr $tmp

fc-cache

# Disable access control for the current user.
xhost +SI:localuser:$USER

# Make Java applications aware this is a non-reparenting window manager.
export _JAVA_AWT_WM_NONREPARENTING=1

~/bin/keys &

# Editor
export VISUAL="nvim"
export EDITOR="$VISUAL"
export ALTERNATE_EDITOR="vim"

emacs --daemon &

dunst &

greenclip daemon &

nm-applet &

#urxvtd -q &

barriers &

#discord &

#(conky -c ~/.oconkyrc | while read LINE; do xsetroot -name "`echo "$LINE" | ~/bin/dnl-block`"; done) &

dropbox &

if [[ -z $WM ]];
then 
    ~/bin/xr -m fodao && picom -b && wal -R && exec qtile > ~/log
else
	~/bin/xr -m note && conky -d && picom -b && wal -R && exec $WM
fi

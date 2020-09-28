# Disable access control for the current user.
xhost +SI:localuser:$USER

# Make Java applications aware this is a non-reparenting window manager.
export _JAVA_AWT_WM_NONREPARENTING=1

~/bin/keys

# Editor
export VISUAL="nvim"
export EDITOR="$VISUAL"
export ALTERNATE_EDITOR="vim"

dunst &

nm-applet &

/usr/bin/stalonetray &

( ~/bin/xr -m fodao && conky -d && picom -b && wal -R ) &

barriers &

(conky -c ~/.oconkyrc | while read LINE; do xsetroot -name "`echo "$LINE" | ~/bin/dnl-block`"; done) &

dropbox &

if [[ -z $WM ]];
then 
	exec ~/bin/startdwm
else
	exec $WM
fi

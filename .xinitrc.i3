# Disable access control for the current user.
xhost +SI:localuser:$USER

# Make Java applications aware this is a non-reparenting window manager.
export _JAVA_AWT_WM_NONREPARENTING=1

# Set default cursor.
xsetroot -cursor_name left_ptr

set r rate 200 60

export VISUAL="nvim"
export EDITOR="$VISUAL"
export ALTERNATE_EDITOR="vim"

/home/daniel/bin/xr -m fodao &
/home/daniel/bin/keys &

exec i3

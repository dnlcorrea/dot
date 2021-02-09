# Look in https://github.com/qtile/qtile/blob/v0.16.1/libqtile/resources/default_config.py
# for examples
# Updated: Thu Jan 28 16:55:46 -03 2021

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Rule, Click, Drag, Group, Key, Screen, Match, ScratchPad, DropDown
from libqtile.lazy import lazy

from libqtile.log_utils import logger

from margins import *

import pywal

colors = pywal.colors.file(".cache/wal/colors.json")['colors']

import socket,subprocess

def kick_to_next_screen(qtile):
    cur = 1 if int(qtile.current_screen.index) == 0 else 0
    qtile.current_window.toscreen(cur)
    qtile.to_screen(cur)
    return True

mod = "mod4"
terminal = "kitty"
browser="/home/daniel/Applications/brave"

keys = [
    Key([], "Print", lazy.spawn("printscreen"), desc="Print Screen"),

    # Function Keys
    Key([mod], "F1", lazy.spawn("pavucontrol"), desc="Pulse Audio GUI"),
    Key([mod], "F2", lazy.spawn(terminal + " -t htop -e htop"), desc="htop"),
    Key([mod], "F3", lazy.spawn(terminal + " -t BashTOP -e bashtop"), desc="bashtop"),
    Key([mod], "F4", lazy.spawn(browser + " --new-window https://web.whatsapp.com"), desc="whatsapp"),

    # QTile COnfig and documentation
    Key([mod], "p", lazy.spawn(terminal + " -e nvim .config/qtile/config.py"), desc="Edit config file"),
    Key([mod, "shift"], "p",
        lazy.spawn(browser + " --new-window http://docs.qtile.org/en/latest/"), desc="QTile documentation on the world wide web."
    ),

    Key([mod], "i", lazy.layout.grow(), lazy.layout.toggle_split(), desc="Increase Ratio"),
    Key([mod], "u", lazy.layout.shrink(), lazy.layout.normalize(), desc="Decrease Ratio"),


    # Move windows up or down in current stack
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),

    Key(["shift"], "space", lazy.layout.shuffle_up()),

    Key([mod, "shift"], "g", lazy.spawn("google-chrome-stable"), desc="Launch browser"),
    Key([mod], "g", lazy.spawn("/home/daniel/Applications/brave"), desc="Launch browser"),

    Key([mod], "slash", lazy.window.toggle_floating(),
        desc="Toggle Floating"),

    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"),

    Key([mod], "w", lazy.prev_screen()),

    Key([mod], "o", lazy.layout.flip(), desc="Shrink Main"),
    Key([mod], "y", lazy.layout.maximize(), desc="Shrink Main"),

    Key([mod], "x", lazy.function(kick_to_next_screen)),

    Key([mod], "bracketleft", lazy.findwindow(), desc='Find window'),

    Key([mod], "b", lazy.hide_show_bar("top"), desc='Toggle bar' ),
    Key([mod], "t", lazy.function(toggleMargins)),
    Key([mod], "z", lazy.function(incMargins)),
    Key([mod, "shift"], "z", lazy.function(decMargins)),

    # Screens
    Key([mod], "m", lazy.screen.toggle_group(), ),
    Key([mod], "period", lazy.layout.shuffle_down() ),
    Key([mod], "comma", lazy.layout.shuffle_up() ),

    #Key([mod], "bracketleft", lazy.prev_screen() ),

    Key([mod], "r", lazy.spawn(terminal + " -e ranger"), desc="Launch Ranger"),

    Key([mod], "v", lazy.spawn(terminal + " -e nvim"), desc="Launch Nvim"),

    Key([mod], "Tab", lazy.next_layout(),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod, "shift"], "Tab", lazy.prev_layout(),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod], "BackSpace", lazy.spawn("sxiv /home/daniel/.config/qtile"),
        desc="Adjust volume using pulsemixer"),

    Key([mod], "backslash", lazy.spawn("exeq"), desc="ROFI Executables"),

    Key([mod], "bracketright", lazy.spawn("rofilocate"), desc="ROFI Executables"),

    # Swap panes of split stack

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key(["mod1"], "space", lazy.spawn("rofi -show window")),

    Key([mod], "apostrophe", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show")),

    Key([mod], "equal", lazy.spawn("pactl -- set-sink-volume 0 +10%")),
    Key([mod], "minus", lazy.spawn("pactl -- set-sink-volume 0 -10%")),

    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod], "0", lazy.spawn('/home/daniel/bin/wallie'), desc="Qtile CMD"),
    Key([mod, "shift"], "0", lazy.spawn(terminal + " -e fish -c wallpaper"), desc="Qtile CMD"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    #Key([mod], "q", lazy.spawn("emacs"), desc="Emacs"),

    #Key([mod], "dead_acute", lazy.spawn("rofi -show drun"),
    #    desc="Spawn a command using a prompt widget"),

    Key([mod], "ccedilla", lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),

    Key([mod, "shift"], "s", lazy.spawn("rofi -show ssh")),

    #### Layouts Index
    Key([mod], "a", lazy.to_layout_index(0) ),
    Key([mod], "s", lazy.to_layout_index(1) ),
    Key([mod], "d", lazy.to_layout_index(2) ),
]




layout_theme = {
    "border_width": 1,
    "margin": 7,
    "border_focus": colors['color7'],
    "border_normal": colors['color0']
}

layouts = [
    layout.MonadTall(
        ratio = 0.55,
        single_margin = 0,
        new_at_current = True,
        **layout_theme
    ),
    layout.Max(),
    layout.Columns(
        border_width=1,
        margin=5,
        border_focus=colors['color7'],
        border_normal=colors['color0'],
        border_focus_stack=colors['color4'],
        grow_amount=6
    ),
    layout.Matrix(**layout_theme),
    ## Other layouts
    #layout.Tile(**layout_theme),
    #layout.Zoomy(),
    #layout.Stack(),
    #layout.TreeTab(),
    #layout.MonadWide( ),
    #layout.RatioTile(),
    #layout.VerticalTile(),
]

groups = [
    Group("1", position=1, layout="monadtall", matches=[Match(wm_class=['jetbrains-phpstorm'])]),
    Group("2", position=2, layout="max"),
    Group("3", position=3, layout="columns"),
    Group("4", position=4, layout="matrix"),
    Group("5", position=5, layout="monadtall"),
    Group("6", position=6, layout="monadtall"),
    Group("7", position=7, layout="monadtall"),
    Group("8", position=8, layout="monadtall", matches=[Match(wm_class=['discord'])]),
    Group("9", position=9, layout="columns"),
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="switch to & move focused window to group {}".format(i.name)),

        Key([mod, "control"], i.name, lazy.window.togroup(i.name),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])


# ScratchPad
groups.append(
        ScratchPad("scratchpad", [
          # define a drop down terminal.
          # it is placed in the upper third of screen by default.
          DropDown(
              "term", terminal,
              opacity=.98,
              height=.5, width=.5,
              y=.25, x=.25,
          ),

        Group("a"),
    ])
)

keys.extend([
    Key([mod], 'semicolon', lazy.group['scratchpad'].dropdown_toggle('term'))
])

widget_defaults = dict(
        font='Mono',
        fontsize=16,
        padding=6,
        antialias=True,
        autohint=True,
        background=colors['color0']
)

extension_defaults = widget_defaults.copy()

separator = {
    "foreground": "#333333",
    "padding": 12
}

def funk():
    return subprocess.check_output(
            ['curl', 'https://wttr.in/Foz+do+Iguacu?format=%c%f']
        ).decode('utf-8')

def uname():
    return subprocess.check_output(['uname', '-r']).decode('utf-8')

dnlBar = [
        widget.CurrentLayoutIcon(background=colors['color0'],scale=.7),

        widget.CurrentScreen(
            26,
            font="mono",
            active_color=colors['color8'],
            inactive_color=colors['color7'],
            padding=12
        ),

        widget.GroupBox(
            hide_unused=True,
            margin=2.5,
            highlight_method='block',
            urgent_alert_methods='block',
            this_current_screen_border=colors['color2'],
            this_screen_border=colors['color2']
        ),

        widget.WindowName(padding=12,background=colors['color0']),
        widget.Prompt(),

        widget.TextBox(text="🌡",padding=0),
        widget.ThermalSensor(update_interval=10),

        widget.Pomodoro(prefix_inactive="🍅", prefix_active="🍅 "),

        widget.GenPollText(
            func=funk,
            interval=4*60
        ),

        widget.CPU(
            format = "💻 {freq_current}Gz {load_percent}%",
            foreground = colors['color7'],
            interval = 4
            ),

        widget.DF(
            format="/{f}G",
            visible_on_warn=False,
            foreground=colors['color2']
        ),

        widget.DF(
            format="~{f}G",
            visible_on_warn=False,
            foreground=colors['color2'],
            partition="/home"
        ),

        widget.Memory(
            format = "::{MemUsed}M",
            foreground = colors['color7'],
        ),

        widget.Net(
            interface="wlp1s0",
            foreground=colors['color6'],
            format="{down} {up}"
            ),

        widget.Battery(foreground=colors['color5']),

        widget.Clock(format='%a %d/%m %H:%M', foreground=colors['color1']),

        #widget.TextBox(text="", foreground=colors['color7']),
        #widget.Volume(foreground=colors['color8']),

        #widget.CheckUpdates(
        #    foreground=colors[1],
        #    display_format='{updates}',
        #    no_update_string="0"
        #),

        widget.Systray(icon_size=12),
        ]

screens = [
    Screen( top=bar.Bar(dnlBar, 28) ),
    Screen( top=bar.Bar([
                widget.CurrentLayoutIcon(background=colors['color0'],scale=.8),

                widget.CurrentScreen(
                    26,
                    font="mono",
                    active_color=colors['color8'],
                    inactive_color=colors['color7'],
                    padding=12
                ),

                widget.GroupBox(
                    hide_unused=True,
                    highlight_method='block',
                    urgent_alert_methods='block',
                ),

                widget.WindowName(padding=12,background=colors['color0']),

                widget.Clock(format='%a %d/%m %H:%M', foreground=colors['color1']),

            ], 28
        )
    )
]

logger.warning(lazy.screen.info())


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.function(kick_to_next_screen)),
]

dgroups_key_binder = None

dgroups_app_rules = []

main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wname'  : 'branchdialog'},
    {'wname'  : 'pinentry'},
    {'wmclass': 'ssh-askpass'},
    {'wmclass': 'pavucontrol'},
], **layout_theme)

auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, Match, ScratchPad, DropDown
from libqtile.lazy import lazy

from margins import *

import pywal

colors = pywal.colors.file(".cache/wal/colors.json")['colors']

import socket,subprocess

print (colors['color0'])

#def kick_to_next_screen(qtile, direction=1):
#      other_scr_index = (qtile.screens.index(qtile.currentScreen) + direction) % len(qtile.screens)
#      othergroup = None
#      for group in qtile.cmd_groups().values():
#              if group['screen'] == other_scr_index:
#                      othergroup = group['name']
#                      break
#      if othergroup:
#              qtile.moveToGroup(othergroup)


# cmd_display_kb(*args)[source]

### Sets

#  colors = [
#      "#002642", "#840032",
#      "#e59500", "#e5dada",
#      "#02040f"
#  ]

layout_theme = {
    "border_width": 1,
    "margin": 6,
    "border_focus": colors['color7'],
    "border_normal": colors['color0']
}

mod = "mod4"
terminal = "alacritty"

keys = [
    # Function Keys
    Key([mod], "F1", lazy.spawn("pavucontrol"), desc="Pulse Audio GUI"),

    # QTile COnfig and documentation
    Key([mod], "p", lazy.spawn("st nvim .config/qtile/config.py"), desc="Edit config file"),
    Key([mod, "shift"], "p",
        lazy.spawn("google-chrome-stable --new-window http://docs.qtile.org/en/latest/"),
        desc="QTile documentation on the world wide web."
    ),

    Key([mod], "F2", lazy.spawn("emacsclient -c org/journal/October.org"),
        desc="Journal"),
    Key([mod], "F3", lazy.spawn("emacsclient -c ~/.config/fish/config.fish"),
        desc="Journal"),

    # Switch between windows in current stack pane
    Key([mod], "i", lazy.layout.grow(), desc="Increase Ratio"),
    Key([mod], "u", lazy.layout.shrink(),  desc="Decrease Ratio"),


    # Move windows up or down in current stack
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left(), lazy.layout.shuffle_left()),
    Key([mod], "l", lazy.layout.right(), lazy.layout.previous()),
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
    Key([mod], "Return", lazy.layout.toggle_split()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),

    # Maybe this is what I want
    Key(["shift"], "space", lazy.layout.shuffle_up()),

    Key([mod], "g", lazy.spawn("google-chrome-stable"),
        desc="Launch browser"),

    Key([mod], "slash", lazy.window.toggle_floating(),
        desc="Toggle Floating"),

    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"),

    Key([mod], "e", lazy.to_screen(1) ),
    Key([mod, "shift"], "e", lazy.window.toscreen(1), desc="To screen"),

    Key([mod], "w", lazy.to_screen(0) ),
    Key([mod, "shift"], "w", lazy.window.toscreen(0), desc="To screen"),

    Key([mod, "shift"], "o", lazy.layout.decrease_nmaster(),
        desc="Fullscreen window"),

    Key([mod], "o", lazy.layout.increase_nmaster(),
        desc="Fullscreen window"),


    Key([mod], "c",
        lazy.spawn("scrcpy"),
        desc='Launch scrcpy'
    ),

    Key([mod], "b", lazy.hide_show_bar("top"), desc='Toggle bar' ),
    Key([mod], "a", lazy.function(toggleMargins)),
    Key([mod], "z", lazy.function(incMargins)),
    Key([mod, "shift"], "z", lazy.function(decMargins)),

    # Screens
    Key([mod], "m", lazy.screen.toggle_group(), ),
    Key([mod], "comma", lazy.screen.prev_group() ),
    Key([mod], "period", lazy.screen.next_group() ),


    Key([mod], "r", lazy.spawn("st -e fish -c 'dvtm nnn nnn'"),
        desc="Launch browser"),

    Key([mod, "shift"], "r", lazy.spawn("st fish -c ranger"),
        desc="Launch browser"),

    Key([mod], "d", lazy.spawn("dmenu_run"),
        desc="Launch browser"),

    Key([mod], "v", lazy.spawn("emacsclient -c"),
        desc="Launch Emacs"),

    Key([mod], "n", lazy.spawn("nvim-qt"),
        desc="Launch Emacs"),

    Key([mod], "Tab", lazy.next_layout(),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod, "shift"], "Tab", lazy.prev_layout(),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod], "apostrophe", lazy.spawn("search"),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod], "BackSpace", lazy.spawn('st -c pulsemixer pulsemixer'),
        desc="Adjust volume using pulsemixer"),

    Key([mod], "backslash", lazy.spawn("exeq"), desc="Swap panes of split stack"),

    # Swap panes of split stack

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key(["mod1"], "space", lazy.spawn("rofi -show window")),

    Key([mod], "equal", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show")),

    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "grave", lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),

    #### Layouts Index
    Key([mod, "shift"], "a", lazy.to_layout_index(0) ),
    Key([mod, "shift"], "s", lazy.to_layout_index(1) ),
    Key([mod, "shift"], "d", lazy.to_layout_index(2) ),
]

groups = [Group(i, position=i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),

        Key([mod, "control"], i.name, lazy.window.togroup(i.name),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# ScratchPad
groups.append(
        ScratchPad("scratchpad", [
          # define a drop down terminal.
          # it is placed in the upper third of screen by default.
          DropDown(
              "term", "st",
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



#Group("7", matches=[Match(wm_class=["discord"])])


layouts = [
    layout.MonadTall(
        ratio = 0.55,
        border_width=1,
        margin=8,
        border_focus= "#ededed",
        border_normal= colors['color0'],
        single_margin = 0,
        new_at_current = True
    ),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Stack(
        num_stacks=2,
        margin=3,
        border_focus = "#ececec",
        border_normal = "#222222"
        ),
    layout.TreeTab(**layout_theme),
    ## Other layouts
    #layout.Columns(),
    #layout.MonadWide( ),
    #layout.Tile(),
    #layout.Matrix(),
    #layout.RatioTile(margin=4),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]


widget_defaults = dict(
        font='Mono',
        fontsize=12,
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
            this_current_screen_border=colors['color1'],
            this_screen_border=colors['color2']
        ),

        widget.WindowName(padding=12,background=colors['color0']),

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
        widget.PulseVolume(foreground=colors['color8']),

        #widget.CheckUpdates(
        #    foreground=colors[1],
        #    display_format='{updates}',
        #    no_update_string="0"
        #),

        widget.Systray(icon_size=12),
        ]

if socket.gethostname() == 'sashimi':
    screens = [
        Screen( top=bar.Bar(dnlBar, 28) ),
        Screen( top=bar.Bar([
                    widget.CurrentLayoutIcon(background=colors['color0'],scale=.8),

                    widget.CurrentScreen(
                        26,
                        font="mono",
                        active_color=colors['color8'],
                        inactive_color=colors['color8'],
                        padding=12
                    ),

                    widget.Sep(**separator),

                    widget.GroupBox(
                        hide_unused=True,
                        highlight_method='block',
                        urgent_alert_methods='block',
                    ),

                    widget.Clock(format='%a %d/%m %H:%M', foreground=colors['color1']),

                ], 28
            )
        )
    ]
else:
    screens = [
        Screen( top=bar.Bar(dnlBar, 28) ),
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toscreen(0))
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'pulsemixer'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **layout_theme)

auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"

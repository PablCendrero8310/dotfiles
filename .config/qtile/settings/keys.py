# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.lazy import lazy

from .menus import show_power_menu

mod = "mod4"

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
        # ------------ Window Configs ------------
        # Switch between windows in current stack pane
        ([mod], "j", lazy.layout.down()),
        ([mod], "k", lazy.layout.up()),
        ([mod], "h", lazy.layout.left()),
        ([mod], "l", lazy.layout.right()),
        # Change window sizes (MonadTall)
        ([mod, "shift"], "l", lazy.layout.grow()),
        ([mod, "shift"], "h", lazy.layout.shrink()),
        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Move windows up or down in current stack
        ([mod, "shift"], "j", lazy.layout.shuffle_down()),
        ([mod, "shift"], "k", lazy.layout.shuffle_up()),
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        # Kill window
        ([mod], "w", lazy.window.kill()),
        # Switch focus of monitors
        ([mod], "period", lazy.next_screen()),
        ([mod], "comma", lazy.prev_screen()),
        # Restart Qtile
        ([mod, "control"], "r", lazy.restart()),
        ([mod, "control"], "q", lazy.shutdown()),
        ([mod, "control"], "p", lazy.function(show_power_menu)),
        ([mod], "r", lazy.spawncmd()),
        # ------------ App Configs ------------
        # Menu
        ([mod], "m", lazy.spawn("rofi -show drun -show-icons -b")),
        # Window Nav
        ([mod, "shift"], "m", lazy.spawn("rofi -show")),
        # Browser
        ([mod], "b", lazy.spawn("brave")),
        # School browser
        ([mod, "shift"], "b", lazy.spawn("google-chrome-stable")),
        # File Explorer
        ([mod], "e", lazy.spawn("thunar")),
        # Onlyoffice
        ([mod], "o", lazy.spawn("onlyoffice-desktopeditors")),
        # Terminal
        ([mod], "Return", lazy.spawn("kitty")),
        # Redshift
        ([mod], "r", lazy.spawn("redshift -O 2400")),
        ([mod, "shift"], "r", lazy.spawn("redshift -x")),
        # Screenshot
        (
            [mod],
            "s",
            lazy.spawn(
                "scrot 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mkdir -p ~/images/screenshots/ | mv $f ~/images/screenshots/'"
            ),
        ),
        ([mod, "shift"], "s", lazy.spawn("scrot -s")),
        # ------------ Hardware Configs ------------
        # Volume
        (
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        ),
        (
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        ),
        ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        # Brightness
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ]
]

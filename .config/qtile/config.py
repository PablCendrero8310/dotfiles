# Qtile Config File
# http://www.qtile.org/

# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles


import subprocess
from os import environ, path

from libqtile import hook

from settings.groups import groups
from settings.keys import keys, mod
from settings.layouts import floating_layout, layouts
from settings.mouse import mouse
from settings.path import qtile_path
from settings.screens import screens
from settings.widgets import extension_defaults, widget_defaults

environ["XCURSOR_THEME"] = "Breeze_Default"  # Reemplaza con el nombre del tema
environ["XCURSOR_SIZE"] = "16"  # Tamaño opcional


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, "autostart.sh")])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "urgent"
wmname = "LG3D"

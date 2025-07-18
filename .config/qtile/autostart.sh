#!/bin/sh
xsetroot -cursor_name left_ptr
picom --config ~/.config/picom/picom.conf &
# systray battery icon
dunst &
feh --bg-scale /usr/share/backgrounds/arch-wallpaper.png &
cbatticon -u 5 &
# systray volume
volumeicon &

nm-applet &

udiskie -t &
xautolock -time 1 -locker dm-tool lock &

xfce4-clipman &

kbanish &

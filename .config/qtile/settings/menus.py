from libqtile.lazy import lazy
from qtile_extras.popup import PopupImage, PopupRelativeLayout, PopupText

from .theme import colors


def show_power_menu(qtile):
    # Posiciones X para 5 elementos bien distribuidos
    positions_x = [0.1, 0.3, 0.5, 0.7, 0.9]

    controls = [
        # ICONOS
        PopupImage(
            filename="/usr/share/icons/Papirus-Dark/24x24/actions/system-lock-screen.svg",
            pos_x=positions_x[0] - 0.05,
            highlight=colors["focus"],
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    "bash -c '/home/pablo/.local/bin/lock'"
                )
            },
        ),
        PopupImage(
            filename="/usr/share/icons/Papirus-Dark/24x24/actions/system-suspend.svg",
            pos_x=positions_x[1] - 0.05,
            highlight=colors["focus"],
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(
                    "bash -c '/home/pablo/.local/bin/lock && systemctl suspend'"
                )
            },
        ),
        PopupImage(
            filename="/usr/share/icons/Papirus-Dark/24x24/actions/system-reboot.svg",
            pos_x=positions_x[2] - 0.05,
            highlight=colors["focus"],
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={"Button1": lazy.spawn("systemctl reboot")},
        ),
        PopupImage(
            filename="/usr/share/icons/Papirus-Dark/24x24/actions/system-shutdown.svg",
            pos_x=positions_x[3] - 0.05,
            highlight=colors["focus"],
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={"Button1": lazy.spawn("systemctl poweroff")},
        ),
        PopupImage(
            filename="/usr/share/icons/Papirus-Dark/24x24/actions/system-log-out.svg",
            pos_x=positions_x[4] - 0.05,
            highlight=colors["focus"],
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={"Button1": lazy.logout()},
        ),
        # TEXTOS (alineados justo debajo de cada icono)
        PopupText(
            text="Bloquear",
            pos_x=positions_x[0] - 0.05,
            highlight=colors["focus"],
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center",
        ),
        PopupText(
            text="Suspender",
            pos_x=positions_x[1] - 0.05,
            highlight=colors["focus"],
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center",
        ),
        PopupText(
            text="Reiniciar",
            pos_x=positions_x[2] - 0.05,
            highlight=colors["focus"],
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center",
        ),
        PopupText(
            text="Apagar",
            pos_x=positions_x[3] - 0.05,
            highlight=colors["focus"],
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center",
        ),
        PopupText(
            text="Cerrar Sesión",
            pos_x=positions_x[4] - 0.05,
            highlight=colors["focus"],
            pos_y=0.7,
            width=0.1,
            height=0.2,
            h_align="center",
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)

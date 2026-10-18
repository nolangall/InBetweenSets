"""InBetween Sets: app entry point.

Opens a phone-sized window with a bottom navigation bar that switches
between the four main views. Each view is a placeholder for now.
"""

import flet as ft

from views.feed_view import feed_view
from views.history_view import history_view
from views.log_view import log_view
from views.timer_view import timer_view

VIEWS = [log_view, timer_view, feed_view, history_view]


def main(page: ft.Page) -> None:
    page.title = "InBetween Sets"
    page.window.width = 390   # roughly an iPhone-sized screen
    page.window.height = 844
    page.theme_mode = ft.ThemeMode.DARK

    body = ft.Container(content=VIEWS[0](), expand=True, padding=20)

    def on_nav_change(e: ft.ControlEvent) -> None:
        index = int(e.control.selected_index)
        body.content = VIEWS[index]()
        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EDIT_NOTE, label="Log"),
            ft.NavigationBarDestination(icon=ft.Icons.TIMER, label="Rest"),
            ft.NavigationBarDestination(icon=ft.Icons.PLAY_CIRCLE, label="Feed"),
            ft.NavigationBarDestination(icon=ft.Icons.SHOW_CHART, label="History"),
        ],
    )
    page.add(body)


if __name__ == "__main__":
    # Newer Flet versions use ft.run(); older ones use ft.app().
    if hasattr(ft, "run"):
        ft.run(main)
    else:
        ft.app(target=main)

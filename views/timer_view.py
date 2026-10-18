"""Rest timer view. Placeholder; the timer and banner are planned for Weeks 5-6."""

import flet as ft


def timer_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Rest Timer", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Your rest countdown will show here.", size=16),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )

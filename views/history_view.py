"""History view. Placeholder; charts are planned for Weeks 7-8."""

import flet as ft


def history_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("History", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Progress charts for each exercise will show here.", size=16),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )

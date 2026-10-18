"""Video feed view. Placeholder; the Pexels feed is planned for Weeks 5-6."""

import flet as ft


def feed_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Feed", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Short fitness clips will play here while you rest.", size=16),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )

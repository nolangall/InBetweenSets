"""Log view. Placeholder; the real logger is planned for Weeks 3-4."""

import flet as ft


def log_view() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Log a Set", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Exercise, weight and reps will be entered here.", size=16),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )

from dash import html
import dash_bootstrap_components as dbc

icon_left = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
icon_up = html.I(className="fa-solid fa-hand-point-up fs-5 me-2")


def change_theme_alert(text=None, auto_dismiss=True):
    if text is None:
        intro_text = "Use the Change Theme button to see examples with all 26 themes."
        text = html.Span([icon_left, intro_text])

    if auto_dismiss:
        return dbc.Alert(
            text, is_open=True, duration=4000, style={"maxWidth": 300}, className="py-2"
        )

    return dbc.Alert(
        text, is_open=True, dismissable=True, style={"maxWidth": 300}, className="py-2"
    )

bootstrap_utils_alert = dbc.Alert(
        html.Span([icon_up, "Use the Bootstrap Cheatsheet button to open a cheatsheet in a new window"]),
        is_open=True, dismissable=True, style={"maxWidth": 300}, className="py-2", color="primary"
    )
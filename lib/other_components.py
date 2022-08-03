from dash import html
import dash_bootstrap_components as dbc


def change_theme_alert(text=None, auto_dismiss=True):
    if text is None:
        intro_text = "Use the 'Change Theme' button to see examples with all 26 themes."
        icon = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
        text = html.Span([icon, intro_text])

    if auto_dismiss:
        return dbc.Alert(
            text, is_open=True, duration=4000, style={"maxWidth": 300}, className="py-2"
        )

    return dbc.Alert(
        text, is_open=True, dismissable=True, style={"maxWidth": 300}, className="py-2"
    )

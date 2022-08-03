import dash
from dash import html
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_app_first


dash.register_page(__name__, path="/", order=1, name="Sample App", description="")

filename = "theme_explorer_sample_app"

notes = """


"""


icon = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
icon_text = html.Span(
    [
        icon,
        "Use 'Change Theme' button to see this app with all 26 themes! ",
    ]
)

layout = html.Div(
    [
        html.Div(
            dbc.Alert(
                icon_text, is_open=True, dismissable=True, style={"maxWidth": 350}
            ),
        ),
        example_app(filename, notes_first=notes, make_layout=make_app_first),
    ],
    className="dbc",
)

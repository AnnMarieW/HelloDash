import dash
from dash import html
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_app_first
from lib.utils import app_description

dash.register_page(
    __name__,
    path="/",
    order=1,
    name="Sample App",
    description=app_description,
    title="Theme Explorer",
    redirect_from=["/theme_explorer"],
)

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
        example_app("sample_app", notes_first=notes, make_layout=make_app_first),
    ],
    className="dbc",
)

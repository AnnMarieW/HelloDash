import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, callback

from .util import make_subheading

COOKIE = "https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png"  # noqa
modal = html.Div(
    [
        make_subheading("dbc.Modal", "modal"),
        html.P(
            [
                dbc.Button("Show the cookie monster", id="button"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Cookies!"),
                        dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                    ],
                    id="modal",
                    is_open=False,
                ),
            ]
        ),
    ],
    className="mb-4",
)


@callback(
    Output("modal", "is_open"),
    [Input("button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open

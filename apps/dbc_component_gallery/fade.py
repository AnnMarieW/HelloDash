import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, callback

from .util import make_subheading

fade = html.Div(
    [
        make_subheading("dbc.Fade", "fade"),
        html.Div(
            [
                dbc.Button(
                    "Toggle fade", id="fade-button", style={"marginBottom": "1rem"},
                ),
                dbc.Fade(
                    dbc.Card(
                        dbc.CardBody(
                            html.P(
                                "This content fades in and out", className="card-text",
                            )
                        )
                    ),
                    id="fade",
                    is_in=True,
                ),
            ]
        ),
    ],
)


@callback(
    Output("fade", "is_in"),
    [Input("fade-button", "n_clicks")],
    [State("fade", "is_in")],
)
def toggle_fade(n, is_in):
    if n:
        return not is_in
    return is_in

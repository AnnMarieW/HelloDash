import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, callback

from .util import make_subheading

collapse = html.Div(
    [
        make_subheading("dbc.Collapse", "collapse"),
        html.Div(
            [
                dbc.Button("Open collapse", id="collapse-button", className="mb-2"),
                dbc.Collapse(
                    dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                    id="collapse",
                ),
            ]
        ),
    ],
    className="mb-4",
)


@callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

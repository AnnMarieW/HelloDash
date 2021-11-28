import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, callback

from .util import make_subheading

popover = html.Div(
    [
        make_subheading("dbc.Popover", "popover"),
        dbc.Button("Click to toggle popover", id="popover-target", color="danger"),
        dbc.Popover(
            [dbc.PopoverHeader("Popover header"), dbc.PopoverBody("Popover body"),],
            id="popover",
            is_open=False,
            target="popover-target",
        ),
    ],
    className="mb-4",
)


@callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

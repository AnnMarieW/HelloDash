import dash_bootstrap_components as dbc
from dash import html, dcc

from .util import dcc_make_subheading


dropdown = html.Div(
    [
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="MTL",
        )
    ],
    className="mb-2",
)

multi_dropdown = html.Div(
    [
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Montréal", "value": "MTL"},
                {"label": "San Francisco", "value": "SF"},
            ],
            multi=True,
            value="MTL",
        )
    ]
)


dcc_dropdowns = html.Div(
    [
        dcc_make_subheading("dcc.Dropdown", "dropdown"),
        dbc.Row([dropdown, multi_dropdown]),
    ],
    className="mb-4",
)

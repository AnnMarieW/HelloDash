
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app, header
from .components import layout as components_layout
from .dcc_components import layout as dcc_components_layout


layout = dbc.Container(
    [
        header,
        dbc.Card(
            [
                html.H2(
                    "Dash Component Gallery",
                    className="bg-primary text-white m-1 mb-4 p-2",
                ),
                html.Div(
                    dbc.Tabs(
                        [
                            dbc.Tab(
                                components_layout,
                                label="Dash Bootstrap Components",
                                label_style={"fontSize": 25},
                            ),
                            dbc.Tab(
                                dcc_components_layout,
                                label="Dash Core Components",
                                label_style={"fontSize": 25},
                            ),
                            dbc.Tab(
                                html.Div("Coming Soon"),
                                style={"height": 400},
                                label="DataTable",
                                label_style={"fontSize": 25},
                            ),
                            dbc.Tab(
                                html.Div("Coming Soon"),
                                style={"height": 400},
                                label="DAQ Components",
                                label_style={"fontSize": 25},
                            ),
                        ]
                    ),
                    className="bg-light",
                ),
            ],
            className="m-4 shadow-lg p-2",
        ),
    ],
    fluid=True,
)

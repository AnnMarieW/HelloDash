import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
from .components import layout as components_layout
from .dcc_components import layout as dcc_components_layout
from .DataTable import layout as table_layout

layout = dbc.Card(
    [
        html.H2(
            "Dash Component Gallery", className="bg-secondary text-white m-1 mb-4 p-2",
        ),
        dbc.Card(
            [
                dbc.Card(
                    dbc.Tabs(
                        [
                            dbc.Tab(
                                children=components_layout,
                                label="Dash Bootstrap Components",
                            ),
                            dbc.Tab(
                                children=dcc_components_layout,
                                label="Dash Core Components",
                            ),
                            dbc.Tab(children=table_layout, label="DataTable",),
                            dbc.Tab(
                                children="Coming Soon",
                                style={"height": 400},
                                label="DAQ Components",
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ],
    className="my-4 shadow-lg p-2",
)

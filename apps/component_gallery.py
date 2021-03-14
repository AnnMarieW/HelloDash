import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import app
from .components import layout as components_layout
from .dcc_components import layout as dcc_components_layout
from .DataTable import layout as table_layout
from .html_components import layout as html_layout

layout = dbc.Card(
    [
        dbc.Jumbotron(
            dcc.Markdown(
                """
            ## Dash Component Gallery     
             *A design guide*   
            """
            ),
            className="m-1 mb-4 p-2",
        ),
        dbc.Card(
            [
                dbc.Card(
                    dcc.Tabs(
                        [
                            dcc.Tab(
                                children=components_layout,
                                label="Dash Bootstrap Components",
                                style={"backgroundColor": "transparent"},
                                selected_className="bg-light text-dark border-primary",
                            ),
                            dcc.Tab(
                                children=html_layout,
                                label="Dash HTML Components",
                                style={"backgroundColor": "transparent"},
                                selected_className="bg-light text-dark border-primary",
                            ),
                            dcc.Tab(
                                children=table_layout,
                                label="DataTable",
                                style={"backgroundColor": "transparent"},
                                selected_className="bg-light text-dark border-primary",
                            ),
                            dcc.Tab(
                                children=dcc_components_layout,
                                label="Dash Core Components",
                                style={"backgroundColor": "transparent"},
                                selected_className="bg-light text-dark border-primary",
                            ),
                            dcc.Tab(
                                children="Coming Soon",
                                label="DAQ Components",
                                style={"backgroundColor": "transparent"},
                                selected_className="bg-light text-dark border-primary",
                            ),
                            dcc.Tab(
                                children="Coming Soon",
                                label="Cheatsheet",
                                style={"backgroundColor": "transparent"},
                                selected_className="bg-light text-dark border-primary",
                            ),
                        ],
                        vertical=True,
                    ),
                ),
            ],
        ),
    ],
    className="my-4 shadow p-2",
)

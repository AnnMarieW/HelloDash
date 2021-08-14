"""
This module is imported in the component_gallery.py and demonstrates how to style a
Dash DataTable to look better with Bootstrap themes.

To keep things organized:
    long descriptions and code examples are in text.py
    cards like a list of links are created in cheatsheet.py and imported here

Cards for a light (dark)  theme are displayed only when a light (dark) theme is selected


"""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


from apps import text, cheatsheet

TABLE_DOCS = "https://dash.plotly.com/datatable/"

from app import app

"""
=====================================================================
Bootstrap style details
"""

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")


"""
=====================================================================
Helper functions
"""


def make_btn_with_modal(id, title, content):
    """
     This makes a button that opens a modal for content
     note: The modal callback is located in the app_galery.py

     id:  unique identifier
     title:  what appears on the button
     content:
        To display text, use dcc.Markdown("my text")
        To display a codebox that looks better with dark themes:
          html.Div(html.Pre(html.Code(" enter code here" )), className="codebox",)

    """
    return html.Div(
        [
            dbc.Button(
                title,
                id={"type": "modal_btn", "index": id},
                color="primary",
                size="sm",
                outline=True,
                className="my-2",
            ),
            dbc.Modal(
                dbc.ModalBody(content),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="lg",
            ),
        ]
    )


default_table = dash_table.DataTable(
    columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
    data=df.to_dict("records"),
    page_size=4,
    editable=True,
    cell_selectable=True,
    filter_action="native",
    sort_action="native",
    style_table={"overflowX": "auto"},
)


light_table = html.Div(
    dash_table.DataTable(
        columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
        data=df.to_dict("records"),
        editable=True,
        page_size=4,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
        style_data_conditional=[
            {
                "if": {"state": "active"},
                "border": "1px solid var(--primary)",
                "opacity": 0.75,
            },
            {"if": {"state": "selected"}, "border": "1px solid", "opacity": 0.75,},
        ],
    ),
    className="dbc_light",
)


dark_table = html.Div(
    dash_table.DataTable(
        columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
        data=df.to_dict("records"),
        editable=True,
        page_size=4,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
        style_data_conditional=[
            {
                "if": {"state": "active"},
                "border": "1px solid var(--primary)",
                "opacity": 0.75,
            },
            {"if": {"state": "selected"}, "border": "1px solid", "opacity": 0.75,},
        ],
        tooltip_conditional=[
            {
                "if": {"row_index": "odd"},
                "type": "markdown",
                "value": "odd rows have a sample tooltip",
            }
        ],
    ),
    className="dbc_dark",
)


"""
=====================================================================
content
"""

default_table_card = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - default style")),
        dbc.CardBody([dcc.Markdown(text.datatable_default_text), default_table]),
    ],
    className="m-4",
)

light_theme_card = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - styled for light themes")),
        dbc.CardBody(
            [
                dcc.Markdown(text.datatable_light_text),
                light_table,
                make_btn_with_modal(
                    "light_theme_code",
                    "see code",
                    dcc.Markdown(text.datatable_light_code),
                ),
            ]
        ),
    ],
    id="light_theme_table",
    className="m-4",
)


dark_theme_card = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - styled for dark themes")),
        dbc.CardBody(
            [
                dcc.Markdown(text.datatable_dark_text),
                dark_table,
                make_btn_with_modal(
                    "dark_theme_code",
                    "see code",
                    dcc.Markdown(text.datatable_dark_code),
                ),
            ]
        ),
    ],
    id="dark_theme_table",
    className="m-4",
)


hover_light = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - light theme with hover row")),
        dbc.CardBody([dcc.Markdown(text.datatable_light_hover_text), default_table]),
    ],
    className="m-4 dbc_row_hover dbc_light",
)


hover_dark = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - dark theme with hover row")),
        dbc.CardBody([dcc.Markdown(text.datatable_dark_hover_text), default_table]),
    ],
    className="m-4 dbc_row_hover dbc_dark",
)


layout = (
    dbc.Container(
        [
            dbc.Card(
                [
                    dcc.Markdown(text.datatable_intro_text),
                    default_table_card,
                    light_theme_card,
                    hover_light,
                    dark_theme_card,
                    hover_dark,
                    html.Div(cheatsheet.how_to_datatable, className="mx-4"),
                ],
                # className="my-2 p-4",
            ),
        ],
        fluid=True,
    ),
)

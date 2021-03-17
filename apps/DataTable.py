"""
This module is imported in the component_gallery.py and demonstrates how to style a
Dash DataTable to look better with Bootstrap themes.

To keep things organized:
    put long descriptions and code examples in text.py and import them here
    cards organized like a list of links are created in cheatsheet.py and imported here

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

# todo - move this to mycss do the same for html_components.py
codebox = {
    "backgroundColor": "transparent",
    "borderStyle": "groove",
    "borderRadius": 15,
    "maxWidth": 900,
    "marginTop": 0,
    "marginBottom": 20,
}

"""
=====================================================================
Bootstrap style details
"""


# https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.css
BOOTSTRAP = {
    "primary": "#007bff",
    "secondary": "#6c757d",
    "selected": "rgba(0, 0, 0, 0.075)",
    "font_color": "black",
    "font": "sans-serif",
}


# https://bootswatch.com/4/cyborg/bootstrap.css
CYBORG = {
    "primary": "#2a9fd6",
    "secondary": "#555",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "white",
    "font": "Roboto",
}
THEMES = {
    "CYBORG": CYBORG,
    "BOOTSTRAP": BOOTSTRAP,
}


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
        To display a codebox:
          html.Div(html.Pre(html.Code(" enter code here" )), style=codebox,)

    """
    return html.Div(
        [
            dbc.Button(
                title,
                id={"type": "modal_btn", "index": id},
                color="secondary",
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


def make_table(theme):
    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        editable=True,
        page_size=4,
        css=[
            {"selector": "input", "rule": f"color:{theme['font_color']}"},
            {"selector": "tr:hover", "rule": "background-color:transparent"},
            {"selector": ".dash-table-tooltip", "rule": "color:black"},
        ],
        style_cell={
            "backgroundColor": "transparent",
            "fontFamily": theme["font"],
            "color": theme["font_color"],
        },
        style_data_conditional=[
            {
                "if": {"state": "active"},
                "backgroundColor": theme["selected"],
                "border": "1px solid " + theme["primary"],
                "color": theme["font_color"],
            },
            {
                "if": {"state": "selected"},
                "backgroundColor": theme["selected"],
                "border": "1px solid" + theme["secondary"],
                "color": theme["font_color"],
            },
        ],
        tooltip_conditional=[
            {
                "if": {"row_index": "odd"},
                "type": "markdown",
                "value": "This row is significant.",
            }
        ],
    )


"""
=====================================================================
"""


default_table_text = dcc.Markdown(
    """
    Dash DataTable is an interactive table component designed for viewing, editing, and exploring large datasets. See
    the full documentation [here](https://dash.plotly.com/datatable)

     Unlike a standard HTML table, the Dash DataTable does not respond to Bootstrap themes automatically.  The first table shows
     the default style for the DataTable.  Try changing the Bootstrap theme in the App Design Selections panel to see how
     the DataTable responds to  different themes.

     As you will see, the default style for the DataTable functions well with light themes. However, with
     dark themes, the font color changes to white and the background stays unchanged,  making the text unreadable.  The
     good news is that the DashTable is highly customizable so you can make it look great with any of the Boostrap themes.
     
     See more information on styling the DataTable in the [Dash Documentation](https://dash.plotly.com/datatable/style). 

"""
)

default_table_card = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - default style")),
        dbc.CardBody(
            dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
                page_size=4,
            ),
        ),
    ],
    className="m-4",
)

light_theme_card = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - styled for light BOOTSTRAP theme")),
        dbc.CardBody(
            [
                dcc.Markdown(text.datatable_light_text),
                make_table(THEMES["BOOTSTRAP"]),
                make_btn_with_modal(
                    "light_theme_code",
                    "see code",
                    html.Div(
                        html.Pre(html.Code(text.datatable_light_code)), style=codebox,
                    ),
                ),
                "Change to a dark theme to see more about styling the table for a dark theme",
            ]
        ),
    ],
    id="light_theme_table_v03",
    className="m-4",
)


dark_theme_card = dbc.Card(
    [
        dbc.CardHeader(html.H5("Dash DataTable - styled for dark CYBORG theme")),
        dbc.CardBody(
            [
                dcc.Markdown(text.datatable_dark_text),
                make_table(THEMES["CYBORG"]),
                make_btn_with_modal(
                    "dark_theme_code",
                    "see code",
                    html.Div(
                        html.Pre(html.Code(text.datatable_dark_code)), style=codebox,
                    ),
                ),
                "Change to a dark theme to see more about styling the table for a dark theme",
            ]
        ),
    ],
    id="dark_theme_table_v03",
    className="m-4",
)


layout = (
    dbc.Container(
        [
            dbc.Card(
                [
                    default_table_text,
                    default_table_card,
                    light_theme_card,
                    dark_theme_card,
                    html.Div(cheatsheet.how_to_datatable, className="mx-4"),
                ],
                className="my-2 p-4",
            ),
        ],
        fluid=True,
    ),
)


@app.callback(
    Output("light_theme_table_v03", "className"),
    Output("dark_theme_table_v03", "className"),
    Input("light_dark_v03", "value"),
)
def hide_show_table(theme):
    return ("m-4", "m-4 d-none") if theme == "Light Themes" else ("m-4 d-none", "m-4")

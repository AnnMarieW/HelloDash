"""
This module is imported in the component_gallery.py
"""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

TABLE_DOCS = "https://dash.plotly.com/datatable/"

from app import app


"""
=====================================================================
Change the Bootstrap style details
"""

# https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.css
BOOTSTRAP = {
    "primary": "#007bff",
    "secondary": "#6c757d",
    "selected": "rgba(0, 0, 0, 0.075)",
    "font_color": "black",
    "font": "sans-serif",
}


# https://bootswatch.com/4/cerulean/bootstrap.css
SUPERHERO = {
    "primary": "#df691a",
    "secondary": "#4e5d6c",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "white",
    "font": "Lato",
}

# https://bootswatch.com/4/cyborg/bootstrap.css
CYBORG = {
    "primary": "#2a9fd6",
    "secondary": "#555",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "white",
    "font": "Roboto",
}

# https://bootswatch.com/4/cerulean/bootstrap.css
CERULEAN = {
    "primary": "#2fa4e7",
    "secondary": "#e9ecef",
    "selected": "rgba(0, 0, 0, 0.075)",
    "font_color": "black",
    "font": "Segoe UI",
}

# https://bootswatch.com/4/journal/bootstrap.css
JOURNAL = {
    "primary": "#eb6864",
    "secondary": "#aaa",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "black",
    "font": "Segoe UI",
}
THEMES = {
    "SUPERHERO": SUPERHERO,
    "CYBORG": CYBORG,
    "BOOTSTRAP": BOOTSTRAP,
    "JOURNAL": JOURNAL,
    "CERULEAN": CERULEAN,
}


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

header = dcc.Markdown(
    """ 
     This is the Dash `DataTable`.  Change the Boostrap theme in the App Design Selections panel to see how the 
     DataTable responds to  different Boostrap themes. See more on how to style the DataTable [here](https://dash.plotly.com/datatable/style)
     
     See the code for Dash DataTables with different themes in the App Gallery
"""
)


def make_subheading(label, link):
    return html.H4(
        dcc.Link(label, href=TABLE_DOCS + link, target="_blank"),
        style={"textDecoration": "underline"},
        className="mb-2",
    )


def make_table(theme):
    return (
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            editable=True,
            css=[
                {"selector": "input", "rule": f"color:{theme['font_color']}"},
                {"selector": "tr:hover", "rule": "background-color:transparent"},
                {"selector": ".dash-table-tooltip", "rule": "color:black"},
            ],
            style_cell={"backgroundColor": "transparent", "fontFamily": theme["font"]},
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
        ),
    )


layout = (
    dbc.Container(
        dbc.Card(
            [
                header,
                html.Hr(),
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4(id="theme_table_title_v03")),
                        dbc.CardBody(id="theme_table_v03"),
                    ],
                    className="my-4",
                ),
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4("Dash Default Table style")),
                        dbc.CardBody(
                            dash_table.DataTable(
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict("records"),
                            )
                        ),
                    ],
                ),
            ],
            className="my-2 p-4",
        ),
        fluid=True,
    ),
)


@app.callback(
    Output("theme_table_v03", "children"),
    Output("theme_table_title_v03", "children"),
    Input("themes_v03", "value"),
    Input("light_dark_v03", "value"),
)
def update_theme_table(theme, light):
    if theme in ["SUPERHERO", "CERULEAN", "JOURNAL"]:
        table = make_table(THEMES[theme]), f"Table Styled for {theme} theme"
    else:
        if light == "Light Themes":
            table = make_table(THEMES["BOOTSTRAP"]), "Table Styled for BOOTSTRAP theme"
        else:
            table = make_table(THEMES["CYBORG"]), "Table Styled for CYBORG theme"
    return table

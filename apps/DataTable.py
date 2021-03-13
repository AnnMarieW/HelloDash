"""
This module is imported in the component_gallery.py and demonstrates how to style a
Dash DataTable to look better with Bootstrap themes.
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
codebox = {
    "backgroundColor": "transparent",
    "borderStyle": "double",
    "borderRadius": 15,
    "maxWidth": 900,
    "marginTop": 10,
    "marginBottom": 20,
}

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

default_table_text = dcc.Markdown(
    """ 
     The Dash `DataTable` does not respond to Bootstrap themes automatically.  The first table shows the default style.
     Try changing the Bootstrap theme in the 
      App Design Selections panel to see how the DataTable responds to  different Bootstrap themes.      
"""
)

light_theme_text = dcc.Markdown(
    """
    #### DataTable with Bootstrap light themes
    
    As you can see in the table above, the default style for the Dash table works fine with Bootstrap light themes - but not
    with dark themes.  To make the table look even better with light themes you can:  
    
    -  Change the font to be the same font as in your selected theme.
    -  Change the active and selected cells to colors from the Bootstrap theme rather than the default "hotpink". 
    
    Try selecting cells in this table and in the default table above to see the style difference.
""",
    className="my-4",
)

light_theme_code = html.Div(
    html.Pre(
        html.Code(
            """ 
        #You can find the details of the colors and fonts here:
        # https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.css
        
        font = "sans-serif"
        primary = "#007bff"
        secondary = "#6c757d"
        selected = "rgba(0, 0, 0, 0.075)"

        datatable = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            style_cell={"fontFamily": font},
            style_data_conditional=[
                {
                    "if": {"state": "active"},
                    "backgroundColor": selected,
                    "border": "1px solid " + primary,
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": selected,
                    "border": "1px solid" + secondary,
                },
            ],
        )   
""",
        )
    ),
    style=codebox,
    #  className='codebox'
)

dark_theme_text = dcc.Markdown(
    """
    #### DataTable with Bootstrap dark themes
    
    When you change to a dark theme, you will need to make more changes to the DataTable style.
    
    -  Set the table background color to transparent to make it the same as the Bootstrap background color.
    -  Set the font color to white to make text visible when cells are selected or the table is editable.
    -  Use the CSS parameter to remove the hover color. The default is white which looks bad and makes the text disappear.
    -  Use the CSS parameter to change the text color of tooltips (if used).
    
    #### Be sure to change to a Dark theme to see the table with the CYBORG style.
"""
)

dark_theme_code = html.Div(
    html.Pre(
        html.Code(
            """       
    # https://bootswatch.com/4/cyborg/bootstrap.css    
    primary = "#2a9fd6"
    secondary = "#555"
    selected = "rgba(255, 255, 255, 0.075)"
    font_color = "white"
    font = "Roboto"    
    
    datatable =dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        editable=True,
        page_size=4,
        css=[
            {"selector": "input", "rule": f"color:{font_color}"},
            {"selector": "tr:hover", "rule": "background-color:transparent"},
            {"selector": ".dash-table-tooltip", "rule": "color:black"},
        ],
        style_cell={"backgroundColor": "transparent", "fontFamily": font},
        style_data_conditional=[
            {
                "if": {"state": "active"},
                "backgroundColor": selected,
                "border": "1px solid " + primary,
                "color": font_color,
            },
            {
                "if": {"state": "selected"},
                "backgroundColor": "selected",
                "border": "1px solid" + secondary,
                "color": font_color,
            },
        ],
    ),    
    """,
        )
    ),
    style=codebox,
)

more_text = dcc.Markdown(
    """ #### See more information on styling the DataTable in the [Dash Documentation](https://dash.plotly.com/datatable/style). """,
)


def make_table(theme):
    return (
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            editable=True,
            page_size=4,
            css=[
                {"selector": "input", "rule": f"color:{theme['font_color']}"},
                {"selector": "tr:hover", "rule": "background-color:transparent"},
                {"selector": ".dash-table-tooltip", "rule": "color:black"},
            ],
            style_table={"maxwidth": 800},
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
                default_table_text,
                html.Div(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Dash DataTable - default style")),
                            dbc.CardBody(
                                dash_table.DataTable(
                                    columns=[{"name": i, "id": i} for i in df.columns],
                                    data=df.to_dict("records"),
                                    page_size=4,
                                    style_table={"maxwidth": 800},
                                ),
                            ),
                        ],
                    ),
                    style={"maxWidth": 900},
                ),
                html.Hr(),
                light_theme_text,
                dbc.Card(
                    [
                        dbc.CardHeader(
                            html.H4("Dash DataTable - styled for light BOOTSTRAP theme")
                        ),
                        dbc.CardBody(make_table(THEMES["BOOTSTRAP"])),
                    ],
                    style={"maxWidth": 900},
                ),
                light_theme_code,
                html.Hr(),
                dark_theme_text,
                dbc.Card(
                    [
                        dbc.CardHeader(
                            html.H4("Dash DataTable - styled for dark CYBORG theme")
                        ),
                        dbc.CardBody(make_table(THEMES["CYBORG"])),
                    ],
                    style={"maxWidth": 900},
                ),
                dark_theme_code,
                more_text,
            ],
            className="my-2 p-4",
        ),
        fluid=True,
    ),
)

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
    "borderStyle": "groove",
    "borderRadius": 15,
    "maxWidth": 900,
    "marginTop": 0,
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
    Dash DataTable is an interactive table component designed for viewing, editing, and exploring large datasets. See
    the full documentation [here](https://dash.plotly.com/datatable)

     Unlike a standard HTML table, the Dash DataTable does not respond to Bootstrap themes automatically.  The first table shows 
     the default style for the DataTable.  Try changing the Bootstrap theme in the App Design Selections panel to see how 
     the DataTable responds to  different themes.    
     
     As you will see, the default style for the DataTable functions well with light themes. However, with 
     dark themes, the font color changes to white and the background stays unchanged,  making the text unreadable.  The 
     good news is that the DashTable is highly customizable so you can make it look great with any of the Boostrap themes.  
          
"""
)

light_theme_text = dcc.Markdown(
    """
    #### DataTable with Bootstrap light themes
    
    With two simple style changes, the DataTable will look even better in your app with Bootstrap light themes:  
    
    -  Change the font to be the same font as your selected theme.
    -  Change the active and selected cells to Bootstrap theme colors rather than the Dash default of "hotpink". Try 
    selecting cells in this table and in the default table above to see the style difference.
""",
    className="my-4",
)

light_theme_code = html.Div(
    html.Pre(
        html.Code(
            """ 
        # DashTable updated with font and colors from the bootstrap theme:        
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
    
    When you use a dark theme, you will need to do a few more things to make the DataTable look nice.  The next table 
    has the following style changes:
    
    -  The table background color is transparent to make it the same as the Bootstrap background color.
    -  The font color is white when cells are selected or the table is editable. This makes text visible in a dark background.
    -  The hover color is changed to transparent.  This is done because the default hover background color is white 
    which looks bad and makes the text disappear.
    -  The text color of tooltips is changed to black.  The default background color is grey, which isn't bad -- but note
     that you can also use this same selector to change the background color and/or add other style changes to tooltips.
    
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
            {"selector": "input", "rule": f"color:{font_color}"},                # fixes text color for editable columns
            {"selector": "tr:hover", "rule": "background-color:transparent"},    # fixes hover bg color 
            {"selector": ".dash-table-tooltip", "rule": "color:black"},          # fixes text color of tooltip data
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
                            dbc.CardHeader(html.H5("Dash DataTable - default style")),
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
                            html.H5("Dash DataTable - styled for light BOOTSTRAP theme")
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
                            html.H5("Dash DataTable - styled for dark CYBORG theme")
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

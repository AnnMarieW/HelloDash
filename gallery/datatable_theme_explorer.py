"""
This app demonstrates how to style the Dash DataTable for various Bootstrap themes.
Define the theme details in the  Boostrap theme dictionary, then set the THEME

"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd

"""
Define Bootstrap style details for the table:
"""

# ------  App version 1  BOOTSTRAP theme  (light)  ------------
# https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.css
BOOTSTRAP = {
    "external_stylesheets": [dbc.themes.BOOTSTRAP],
    "primary": "#007bff",
    "secondary": "#6c757d",
    "selected": "rgba(0, 0, 0, 0.075)",
    "font_color": "black",
    "font": "sans-serif",
}


# ------  App version 2  CYBORG   (dark) ------------
# https://bootswatch.com/4/cyborg/bootstrap.css
CYBORG = {
    "external_stylesheets": [dbc.themes.CYBORG],
    "primary": "#2a9fd6",
    "secondary": "#555",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "white",
    "font": "Roboto",
}


"""
=====================================================================
Set Bootstrap theme here
"""
# THEME = BOOTSTRAP
THEME = CYBORG

# -------------------------------------------------------------------


app = dash.Dash(__name__, external_stylesheets=THEME["external_stylesheets"])

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

table = dash_table.DataTable(
    id="table",
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("records"),
    editable=True,
    css=[
        {"selector": "input", "rule": f"color:{THEME['font_color']}"},
        {"selector": "tr:hover", "rule": "background-color:transparent"},
        {"selector": ".dash-table-tooltip", "rule": "color:black"},
    ],
    style_cell={"backgroundColor": "transparent", "fontFamily": THEME["font"]},
    style_data_conditional=[
        {
            "if": {"state": "active"},
            "backgroundColor": THEME["selected"],
            "border": "1px solid " + THEME["primary"],
            "color": THEME["font_color"],
        },
        {
            "if": {"state": "selected"},
            "backgroundColor": THEME["selected"],
            "border": "1px solid" + THEME["secondary"],
            "color": THEME["font_color"],
        },
    ],
)


app.layout = dbc.Container(
    [
        html.H1("DataTable Theme Explorer", className="bg-primary text-white"),
        html.Hr(),
        dbc.Row(
            dbc.Col(
                dbc.Card([html.H4("Dash DataTable Styled for Boostrap themes"), table])
            )
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

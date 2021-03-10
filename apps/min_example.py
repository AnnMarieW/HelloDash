import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


themes_list = [
    "BOOTSTRAP",
    "CYBORG",
    "DARKLY",
    "SLATE",
    "SOLAR",
    "SUPERHERO",
    "CERULEAN",
    "COSMO",
    "FLATLY",
    "JOURNAL",
    "LITERA",
    "LUMEN",
    "LUX",
    "MATERIA",
    "MINTY",
    "PULSE",
    "SANDSTONE",
    "SIMPLEX",
    "SKETCHY",
    "SPACELAB",
    "UNITED",
    "YETI",
]


dropdown = dcc.Dropdown(
    id="themes",
    options=[{"label": str(i), "value": i} for i in themes_list],
    value="BOOTSTRAP",
    clearable=False,
)

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ]
)

alerts = html.Div(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
    ]
)

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(["Select Theme", dropdown], width=3),
            dbc.Col([buttons, alerts]),
            html.Div(id="blank_output"),
        ],
    ),
    className="m-4",
    fluid=True,
)


app.clientside_callback(
    """
    function(theme) {
        var stylesheet = document.querySelector('link[rel=stylesheet][href^="https://stackpath"]')
        var name = theme.toLowerCase()
        if (name === 'bootstrap') {
            var link = 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css'
          } else {
            var link = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/" + name + "/bootstrap.min.css"
        }
        stylesheet.href = link
    }
    """,
    Output("blank_output", "children"),
    Input("themes", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True)

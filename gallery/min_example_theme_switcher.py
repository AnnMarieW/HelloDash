"""
This is a minimal example of the theme switcher clientside callback

"""


import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


dbc_themes_url = {
    "BOOTSTRAP": dbc.themes.BOOTSTRAP,
    "CERULEAN": dbc.themes.CERULEAN,
    "COSMO": dbc.themes.COSMO,
    "FLATLY": dbc.themes.FLATLY,
    "JOURNAL": dbc.themes.JOURNAL,
    "LITERA": dbc.themes.LITERA,
    "LUMEN": dbc.themes.LUMEN,
    "LUX": dbc.themes.LUX,
    "MATERIA": dbc.themes.MATERIA,
    "MINTY": dbc.themes.MINTY,
    "PULSE": dbc.themes.PULSE,
    "SANDSTONE": dbc.themes.SANDSTONE,
    "SIMPLEX": dbc.themes.SIMPLEX,
    "SKETCHY": dbc.themes.SKETCHY,
    "SPACELAB": dbc.themes.SPACELAB,
    "UNITED": dbc.themes.UNITED,
    "YETI": dbc.themes.YETI,
    "CYBORG": dbc.themes.CYBORG,
    "DARKLY": dbc.themes.DARKLY,
    "SLATE": dbc.themes.SLATE,
    "SOLAR": dbc.themes.SOLAR,
    "SUPERHERO": dbc.themes.SUPERHERO,
}

dropdown = dcc.Dropdown(
    id="themes",
    options=[{"label": str(i), "value": dbc_themes_url[i]} for i in dbc_themes_url],
    value=dbc_themes_url["BOOTSTRAP"],
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
    ],
    className="m-4",
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
        ]
    ),
    className="m-4",
    fluid=True,
)


# Using 2 stylesheets with the delay reduces the  flicker when the theme changes
app.clientside_callback(
    """
    function(url) {
        // Select the stylesheets.
        var stylesheets = document.querySelectorAll('link[rel=stylesheet][href^="https://stackpath"]')
        // Update the url of the main stylesheet.
        stylesheets[stylesheets.length - 1].href = url
        // Delay update of the url of the buffer stylesheet.
        setTimeout(function() {stylesheets[0].href = url;}, 100);
    }
    """,
    Output("blank_output", "children"),
    Input("themes", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True)

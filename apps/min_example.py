

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
        className='m-4',
        style={"width": 200}
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
    [
        dropdown,
        dbc.Col(buttons,width={"size": 9,  "offset": 2}),
        dbc.Col(alerts,width={"size": 3,  "offset": 2}),
        html.Div(id="blank_output")
    ],
    fluid=True,
)


app.clientside_callback(
    """
    function(theme) {

        // select external stylesheets only - not custom css in the assets folder
        var elements = document.querySelectorAll('link[rel=stylesheet][href^="https"]');

         // add new  stylesheet based on  dropdown
        var name = theme.toLowerCase()
        var link = document.createElement("link")
        link.rel = "stylesheet"
        link.type = "text/css"
        if (name === 'bootstrap') {
            link.href = 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css'
          } else {
            link.href = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/" + name + "/bootstrap.min.css"
        }
        document.getElementsByTagName("head")[0].appendChild(link);

        // delete old stylesheets
        for(var i=0; i<elements.length;i++){
            // don't remove if it's the default - bootstsrap
            if (theme === 'BOOTSTRAP' && elements[i].href.startsWith('https://stackpath.bootstrapcdn.com/bootstrap')) {
                return
            }
            elements[i].remove()
        }

    }
    """,
    Output("blank_output", "children"),
    Input("themes", "value"),
)


if __name__ == "__main__":
     app.run_server(debug=True)


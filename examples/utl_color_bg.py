from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


title = dcc.Markdown(
    """
### Color - Background
------------
"""
)

color_bg = html.Div(
    [
        html.P("bg-primary", className="bg-primary"),
        html.P("bg-secondary", className="bg-secondary"),
        html.P("bg-success", className="bg-success"),
        html.P("bg-danger", className="bg-danger"),
        html.P("bg-warning", className="bg-warning"),
        html.P("bg-info", className="bg-info"),
        html.P("bg-light", className="bg-light"),
        html.P("bg-dark", className="bg-dark"),
        html.P("bg-transparent", className="bg-transparent"),
    ]
)

color_bg_gradient = html.Div(
    [
        html.P("bg-primary text-white py-4", className="bg-primary text-white py-4"),
        html.P(
            "bg-primary  bg-gradient text-white py-4",
            className="bg-primary bg-gradient text-white py-4",
        ),
    ],
)

app.layout = html.Div([title, color_bg, color_bg_gradient])

if __name__ == "__main__":
    app.run(debug=True)

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


title = dcc.Markdown(
    """
### Opacity - Background
------------
"""
)

color_bg_opacity = html.Div(
    [
        html.Div("default", className="p-2 m-1 bg-primary text-light"),
        html.Div("75%", className="bg-opacity-75 p-2 m-1 bg-primary text-light "),
        html.Div("50%", className="bg-opacity-50 p-2 m-1 bg-primary text-light "),
        html.Div("25%", className="bg-opacity-25 p-2 m-1 bg-primary text-light "),
        html.Div("10%", className="bg-opacity-10 p-2 m-1 bg-primary text-light "),
    ]
)


app.layout = html.Div(
    [
        title,
        color_bg_opacity,
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

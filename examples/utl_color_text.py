from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

title = dcc.Markdown(
    """
### Color - Text  
------------
"""
)

color_text = html.Div(
    [
        html.P("default text color"),
        html.P("text-primary", className="text-primary"),
        html.P("text-secondary", className="text-secondary"),
        html.P("text-success", className="text-success"),
        html.P("text-danger", className="text-danger"),
        html.P("text-warning", className="text-warning"),
        html.P("text-info", className="text-info"),
        html.P("text-light", className="text-light"),
        html.P("text-dark", className="text-dark"),
        html.P("text-body", className="text-body"),
        html.P("text-muted", className="text-muted"),
    ]
)

app.layout = html.Div([title, color_text])

if __name__ == "__main__":
    app.run(debug=True)

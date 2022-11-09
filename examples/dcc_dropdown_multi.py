from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])


with_theme = html.Div(
    [
        html.H3("Dropdowns - Multi"),
        dbc.Label("dcc.Dropdown multi with Bootstrap theme"),
        dcc.Dropdown(
            ["Apple", "Carrots", "Chips", "Cookies"], ["Cookies", "Carrots"], multi=True
        ),
    ],
    className="dbc",
)


without_theme = html.Div(
    [
        dbc.Label("Without theme", className="mt-4"),
        dcc.Dropdown(
            ["Apple", "Carrots", "Chips", "Cookies"], ["Cookies", "Carrots"], multi=True
        ),
    ]
)


app.layout = dbc.Container([with_theme, without_theme])

if __name__ == "__main__":
    app.run_server(debug=True)

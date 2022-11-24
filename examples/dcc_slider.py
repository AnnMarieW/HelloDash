from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

sliders = html.Div(
    [
        dcc.RangeSlider(0, 20, value=[5, 15], className="mb-2"),
        dcc.Slider(min=0, max=20, step=5, value=10, className="mb-2"),
        dcc.Slider(
            min=0,
            max=10,
            step=1,
            value=5,
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ]
)


with_theme = html.Div(
    [
        html.H3("Sliders"),
        dbc.Label("dcc.Slider and dcc.RangeSlider with Bootstrap theme"),
        sliders,
    ],
    className="dbc",
)


without_theme = html.Div([dbc.Label("Without theme", className="mt-4"), sliders])

app.layout = dbc.Container([with_theme, without_theme])

if __name__ == "__main__":
    app.run_server(debug=True)

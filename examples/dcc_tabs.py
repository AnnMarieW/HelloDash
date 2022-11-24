from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])


tabs = html.Div(
    [
        dcc.Tabs(
            value="tab-1",
            children=[
                dcc.Tab(
                    label="Tab one",
                    value="tab-1",
                    children=html.Div("Tab 1 Content", className="p-4 border"),
                ),
                dcc.Tab(
                    label="Tab two",
                    value="tab-2",
                    children=html.Div("Tab 2 Content", className="p-4 border"),
                ),
            ],
        ),
    ]
)


with_theme = html.Div(
    [html.H3("Tabs"), dbc.Label("dcc.Tabs with Bootstrap theme"), tabs], className="dbc"
)


without_theme = html.Div([dbc.Label("Without theme", className="mt-4"), tabs])

app.layout = dbc.Container([with_theme, without_theme])

if __name__ == "__main__":
    app.run_server(debug=True)

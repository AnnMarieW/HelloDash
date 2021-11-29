#
"""

This is a minimal example of changing themes with the ThemeSwitchAIO component
Note - this requires dash-bootstrap-components>=1.0.0  dash>=2.0 dash-bootstrap-templates>=1.0.2.

"""

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

# select the Bootstrap stylesheets and figure templates for the theme toggle here:
template_theme1 = "pulse"
template_theme2 = "vapor"
url_theme1 = dbc.themes.PULSE
url_theme2 = dbc.themes.VAPOR


dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[url_theme1, dbc.icons.BOOTSTRAP, dbc_css])

df = px.data.gapminder()

header = html.H4("ThemeSwitchAIO Demo", className="bg-primary text-white p-4 mb-2")
buttons = html.Div(
    [
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ],
    className="m-4",
)
graph = html.Div(dcc.Graph(id="graph"), className="m-4")

"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    header,
                    ThemeSwitchAIO(
                        aio_id="theme",
                        icons={"left": "bi bi-moon", "right": "bi bi-sun"},
                        themes=[url_theme1, url_theme2],
                    ),
                    buttons,
                    graph,
                ]
            )
        ]
    ),
    className="m-4",
    fluid=True,
)


@app.callback(
    Output("graph", "figure"), Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    template = template_theme1 if toggle else template_theme2
    return px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
        title="Gapminder 2007: '%s' theme" % template,
    )


if __name__ == "__main__":
    app.run_server(debug=True)

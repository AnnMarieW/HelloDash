
from dash import Dash, html, dcc, Input, Output, Patch, clientside_callback, callback
import plotly.express as px
import plotly.io as pio
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template

# Load data and figure templates
gapminder = px.data.gapminder().query("year==2007")
load_figure_template(["vizro", "vizro_dark"])

vizro_bootstrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@main/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[vizro_bootstrap])

light = dcc.Graph(
    figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", size_max=60, color="continent")
)


dark = dcc.Graph(
    figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", size_max=60, color="continent", template="vizro_dark")
)

tabs = dbc.Tabs(
    [
        dbc.Tab(light, label="vizro_light"),
        dbc.Tab(dark, label="vizro_dark"),
    ]
)


app.layout = dbc.Container(
    [html.H1("Vizro Bootstrap Template Demo", className="bg-primary p-2 mt-4"),  tabs],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)

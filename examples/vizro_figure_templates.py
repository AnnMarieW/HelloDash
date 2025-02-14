
from dash import Dash, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

# preferred method:
# import vizro
# app = Dash(__name__, external_stylesheets=[vizro.bootstrap])

# if not using import vizro:
from dash_bootstrap_templates import load_figure_template
load_figure_template(["vizro", "vizro_dark"])
vizro_bootstrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@main/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css?v=2"
app = Dash(__name__, external_stylesheets=[vizro_bootstrap])

gapminder = px.data.gapminder().query("year==2007")
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

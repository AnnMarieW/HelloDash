import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dash.register_page(__name__, theme=dbc.themes.PULSE)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np

np.random.seed(2020)


def make_figure(mean=0, std=1, template="pulse"):
    data = np.random.normal(mean, std, size=500)
    return px.histogram(data, nbins=30, range_x=[-10, 10], template=template)


layout = html.Div(
    [
        dcc.Graph(id="histograms-graph", figure=make_figure()),
        html.P("Mean:"),
        dcc.Slider(
            id="histograms-mean", min=-3, max=3, value=0, marks={-3: "-3", 3: "3"}
        ),
        html.P("Standard Deviation:"),
        dcc.Slider(id="histograms-std", min=1, max=3, value=1, marks={1: "1", 3: "3"}),
    ]
)


@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")
)
def display_color(mean, std, theme):
    return make_figure(mean, std, template_from_url(theme))

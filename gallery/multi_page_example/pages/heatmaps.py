import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

dash.register_page(__name__, path="/", theme=dbc.themes.SANDSTONE)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.medals_wide(indexed=True)

layout = html.Div(
    [
        html.P("Medals included:"),
        dbc.Checklist(
            id="heatmaps-medals",
            options=[{"label": x, "value": x} for x in df.columns],
            value=df.columns.tolist(),
        ),
        dcc.Graph(id="heatmaps-graph", figure= px.imshow(df)),
    ]
)


@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"), Input(ThemeChangerAIO.ids.radio("theme"), "value"))
def filter_heatmap(cols, theme):
    fig = px.imshow(df[cols], template=template_from_url(theme))
    return fig

import dash
from dash_bootstrap_templates import ThemeChangerAIO
import dash_bootstrap_components as dbc

# specify the theme for the page with the `theme` prop
dash.register_page(__name__, theme=dbc.themes.DARKLY)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
        ),
        dcc.Graph(id="bar-chart"),
    ]
)

# Figures need to be updated when the theme changes to apply the new bootstrap-themed figure template.
@callback(
    Output("bar-chart", "figure"),
    Input("dropdown", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_bar_chart(day, theme):
    mask = df["day"] == day
    fig = px.bar(
        df[mask],
        x="sex",
        y="total_bill",
        color="smoker",
        barmode="group",
        template="darkly",
    )
    return fig

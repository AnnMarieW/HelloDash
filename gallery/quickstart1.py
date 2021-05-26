# -*- coding: utf-8 -*-
"""
Bootstrap Quickstart app - Two graphs side by side
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.gapminder()

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig1 = px.line(df, x="year", y="gdpPercap", color="country")

dff = df.query("year==2007")
fig2 = px.scatter(
    dff, x="gdpPercap", y="lifeExp", size="pop", color="continent", size_max=60
)

app.layout = dbc.Container(
    [
        html.H1(
            "Two graphs side by side", className="bg-primary text-white text-center"
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=fig1), lg=6),
                dbc.Col(dcc.Graph(figure=fig2), lg=6),
            ]
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

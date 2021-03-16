"""
This is a "kitchen sink" quickstart

"""
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Datasets

#  https://plotly.com/python-api-reference/generated/plotly.data.html#module-plotly.data#
df = px.data.gapminder()

# Other datasets
# df = px.data.iris()
# df = px.data.tips()
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')#
# # random numbers
# df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))

# components and figures


def make_dropdown(id, option_list, option_val=0):
    return dcc.Dropdown(
        id=id,
        options=[{"label": str(i), "value": i} for i in option_list],
        value=option_list[option_val],
        clearable=False,
    )


def make_slider(id, slider_list, step=1):
    return dcc.Slider(
        id=id,
        min=slider_list[0],
        max=slider_list[-1],
        step=step,
        marks={int(i): str(i) for i in slider_list},
        value=slider_list[-1],
    )


def make_table(id, dff):
    return dash_table.DataTable(
        id=id,
        columns=[{"name": i, "id": i} for i in dff.columns],
        data=dff.to_dict("records"),
        editable=True,
        page_size=10,
    )


def make_graph(id, dff):
    # This callback uses dataset: px.data.gapminder() select 1 year: dff = df.query("year==2007")
    return dcc.Graph(
        id=id,
        figure=px.scatter(
            dff,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            log_x=True,
            size_max=60,
            title="Gapminder",
        ),
    )


app.layout = dbc.Container(
    [
        html.H1("Title"),
        html.Hr(),
        dbc.Row(
            [
                dbc.CardDeck(
                    [
                        dbc.Card(dcc.Graph(id="graph"),),
                        dbc.Card(make_table("table", df), className="p-4"),
                    ],
                    className="m-4",
                )
            ],
        ),
        dbc.Row(dbc.Col(make_slider("slider", df.year.unique()))),
    ],
    fluid=True,
)


@app.callback(
    Output("graph", "figure"), Input("slider", "value"),
)
def update_graph(slider_val):
    dff = df.query("year==" + str(slider_val))
    figure = px.scatter(
        dff,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        title=f"Gapminder {slider_val}",
    )
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)

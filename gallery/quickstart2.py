# -*- coding: utf-8 -*-
"""
Quickstart app Datatable with a callback
"""

import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


controls = html.Div(
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": i, "value": i} for i in df["country"].unique()],
        multi=True,
        value=[],
    ),
    className="m-4",
)

table = dash_table.DataTable(
    id="table",
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("records"),
    page_size=20,
)

app.layout = dbc.Container(
    [html.H1("Table with a Dropdown"), html.Hr(), dbc.Row(dbc.Col([controls, table]))],
    fluid=True,
)


@app.callback(Output("table", "data"), Input("dropdown", "value"))
def update_table(country_dd):
    dff = df.copy() if country_dd == [] else df[df["country"].isin(country_dd)]
    return dff.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)

"""
If you run this theme locally, you will see the "VAPOR" theme.  To change the theme,
update the theme in the `external_stylesheets`.  Or use one of the theme change components.

"""


import dash
from dash import html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR, dbc_css])

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

table = html.Div(
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        row_selectable="single",
        row_deletable=True,
        editable=True,
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
    ),
)


with_theme = html.Div(
    [
        html.H5("DataTable with Bootstrap theme"),
        table,
    ],
    className="dbc dbc-row-selectable",
)


without_theme = html.Div([html.H5("No theme", className="mt-4"), table])

app.layout = dbc.Container([with_theme, without_theme])


if __name__ == "__main__":
    app.run_server(debug=True)

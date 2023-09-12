"""
If you run this theme locally, you will see the "VAPOR" theme.  To change the theme,
update the theme in the `external_stylesheets`.  Or use one of the theme change components.

"""


import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import pandas as pd


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR, dbc_css])


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    {"field": "athlete", "checkboxSelection": True, "headerCheckboxSelection": True},
    {"field": "age", "maxWidth": 100},
    {"field": "country"},
    {"field": "year", "maxWidth": 120},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

grid = dag.AgGrid(
    id="selection-checkbox-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    defaultColDef={"flex": 1, "minWidth": 150, "sortable": True, "resizable": True, "filter": True},
    dashGridOptions={"rowSelection":"multiple"},
)

app.layout = dbc.Container(
    [
        html.H5("Dash AG Grid with Bootstrap theme"),
        grid,
    ],
    className="dbc dbc-ag-grid",
)

if __name__ == "__main__":
    app.run_server(debug=True)

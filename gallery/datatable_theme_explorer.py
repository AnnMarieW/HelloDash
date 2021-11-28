"""
This app demonstrates how to style the Dash DataTable for Bootstrap themes

"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd

"""
=====================================================================
Set Bootstrap theme here
"""

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


# -------------------------------------------------------------------

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

table = dash_table.DataTable(
    id="table",
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict("records"),
    editable=True,
    css=[
        {"selector": "tr:hover", "rule": "background-color:transparent"},
        {"selector": ".dash-table-tooltip", "rule": "color:black"},
    ],
    style_cell={
        "backgroundColor": "transparent",
        "fontFamily": "var(--font-family-monospace)",
    },
    style_data_conditional=[
        {
            "if": {"state": "active"},
            "backgroundColor": "var(--info)",
            "border": "1px solid var(--primary)",
        },
        {
            "if": {"state": "selected"},
            "backgroundColor": "var(--info)",
            "border": "1px solid var(--secondary)",
        },
    ],
)


app.layout = dbc.Container(
    [
        html.H1("DataTable Theme Explorer", className="bg-primary text-white"),
        html.Hr(),
        dbc.Row(
            dbc.Col(
                dbc.Card([html.H4("Dash DataTable Styled for Boostrap themes"), table])
            )
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

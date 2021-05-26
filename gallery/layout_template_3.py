#
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [dbc.CardHeader("Header"), dbc.CardBody("Body", style={"height": 250})],
    className="h-100 mt-4",
)

graph_card = dbc.Card(dbc.CardBody([dcc.Graph(style={"height": 200})] * 2))

app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(card, width=2),
            dbc.Col(
                [
                    dbc.CardDeck([card] * 3),
                    dbc.CardGroup([graph_card] * 2, className="mt-4"),
                ],
                width=8,
            ),
            dbc.Col(card, width=2),
        ]
    ),
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)

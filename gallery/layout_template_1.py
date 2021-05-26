# #
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [dbc.CardHeader("Header"), dbc.CardBody("Body", style={"height": 250})],
    className="h-100",
)

graph_card = dbc.Card([dbc.CardHeader("Here's a graph"), dbc.CardBody([dcc.Graph()])])

app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.CardDeck([card] * 4),
                    html.H2("Here is some important information to highlight..."),
                    dbc.CardDeck([graph_card] * 2),
                ],
                width=10,
            ),
            dbc.Col(card, width=2),
        ]
    ),
    fluid=True,
    className="m-3",
)

if __name__ == "__main__":
    app.run_server(debug=True)

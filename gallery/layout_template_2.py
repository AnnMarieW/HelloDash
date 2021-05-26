#

import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

LOGO = "https://user-images.githubusercontent.com/72614349/110689028-7523dd80-819f-11eb-8cc6-a62b25f99287.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(dbc.Button("Search", color="primary", className="ml-2"), width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://hellodash.pythonanywhere.com/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="dark",
    dark=True,
    className="mb-4",
)

controls = dbc.Card([dcc.Slider(), dcc.Dropdown()], className="my-4 p-4")

card = dbc.Card([dbc.CardHeader("Header"), dbc.CardBody("Body", style={"height": 250})])

graph_card = dbc.Card(
    dbc.CardBody([html.H4("$1,000,000"), dcc.Graph(style={"height": 200})])
)

graph_card2 = dbc.Card(
    dbc.CardBody([dcc.Graph(style={"height": 400})]), className="my-4"
)

app.layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                dbc.Col([card, controls, controls], width=3),
                dbc.Col(
                    [
                        dbc.CardDeck([graph_card] * 2),
                        graph_card2,
                        dbc.CardDeck([graph_card] * 2),
                    ],
                    width=8,
                ),
            ]
        ),
    ],
    fluid=True,
)


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)

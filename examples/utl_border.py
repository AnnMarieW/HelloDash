from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

title = dcc.Markdown(
    """
### Border 
------------
"""
)


border_direction = dbc.Card(
    [
        dbc.CardHeader("Border Direction"),
        html.Div(
            [
                html.P("border ", className="border "),
                html.P("border-top ", className="border-top "),
                html.P("border-end ", className="border-end "),
                html.P("border-bottom ", className="border-bottom "),
                html.P("border-start ", className="border-start "),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


border_direction_0 = dbc.Card(
    [
        dbc.CardHeader("Border Direction 0"),
        html.Div(
            [
                html.P("border border-0", className="border border-0 "),
                html.P("border border-top-0 ", className="border border-top-0 "),
                html.P("border border-end-0 ", className="border border-end-0 "),
                html.P("border border-bottom-0 ", className="border border-bottom-0 "),
                html.P("border border-start-0 ", className="border border-start-0 "),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


border_color = dbc.Card(
    [
        dbc.CardHeader("Border Color"),
        html.Div(
            [
                html.P("border border-primary ", className="border border-primary "),
                html.P(
                    "border border-secondary ", className="border border-secondary "
                ),
                html.P("border border-success ", className="border border-success "),
                html.P("border border-danger ", className="border border-danter "),
                html.P("border border-warning ", className="border border-warning "),
                html.P("border border-info ", className="border border-info "),
                html.P("border border-light", className="border border-light "),
                html.P("border border-dark  ", className="border border-dark "),
                html.P("border border-white  ", className="border border-white "),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)

border_size = dbc.Card(
    [
        dbc.CardHeader("Border Size"),
        html.Div(
            [
                html.P("border border-1 ", className="border border-1 "),
                html.P("border border-2 ", className="border border-2 "),
                html.P("border border-3 ", className="border border-3 "),
                html.P("border border-4 ", className="border border-4 "),
                html.P("border border-5 ", className="border border-5 "),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)

border_rounded = dbc.Card(
    [
        dbc.CardHeader("Border Rounded"),
        html.Div(
            [
                html.P("border rounded ", className="border rounded "),
                html.P("border rounded-top ", className="border rounded-top "),
                html.P("border rounded-end ", className="border rounded-end "),
                html.P("border rounded-bottom ", className="border rounded-bottom "),
                html.P("border rounded-start ", className="border rounded-start "),
                html.P(
                    "border rounded-circle ",
                    className="border rounded-circle d-flex align-items-center justify-content-center",
                    style={"height": 200, "width": 200},
                ),
                html.P(
                    "border rounded-pill ",
                    className="border rounded-pill ",
                    style={"width": 200},
                ),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


app.layout = html.Div(
    [
        title,
        border_direction,
        border_direction_0,
        border_color,
        border_size,
        border_rounded,
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

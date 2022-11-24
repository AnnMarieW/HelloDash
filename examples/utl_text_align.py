from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

title = dcc.Markdown(
    """
### Text Alignment - responsive by screen size  

Try changing the size of your browser window.


------------
"""
)


text_start = dbc.Card(
    [
        dbc.CardHeader("text-*-start"),
        html.Div(
            [
                html.P(
                    "Start aligned text on all viewport sizes", className="text-start"
                ),
                html.P(
                    "Start aligned text on  viewport sized small or wider",
                    className="text-sm-start",
                ),
                html.P(
                    "Start aligned text on  viewport sized medium or wider",
                    className="text-md-start",
                ),
                html.P(
                    "Start aligned text on  viewport sized large or wider",
                    className="text-lg-start",
                ),
                html.P(
                    "Start aligned text on viewport sized extra large or wider",
                    className="text-xl-start",
                ),
                html.P(
                    "Start aligned text on viewport sized extra extra large",
                    className="text-xxl-start",
                ),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


text_center = dbc.Card(
    [
        dbc.CardHeader("text-*-center"),
        html.Div(
            [
                html.P(
                    "Center aligned text on all viewport sizes", className="text-center"
                ),
                html.P(
                    "Center aligned text on all viewport sized small or wider",
                    className="text-sm-center",
                ),
                html.P(
                    "Center aligned text on viewport sized medium or wider",
                    className="text-md-center",
                ),
                html.P(
                    "Center aligned text on viewport sized large or wider",
                    className="text-lg-center",
                ),
                html.P(
                    "Center aligned text on viewport sized extra large or wider",
                    className="text-xl-center",
                ),
                html.P(
                    "Center aligned text on viewport sized extra extra large",
                    className="text-xxl-center",
                ),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


text_end = dbc.Card(
    [
        dbc.CardHeader("text-*-end"),
        html.Div(
            [
                html.P("End aligned text on all viewport sizes", className="text-end"),
                html.P(
                    "End aligned text on viewport sized small or wider",
                    className="text-sm-end",
                ),
                html.P(
                    "End aligned text on viewport sized medium or wider",
                    className="text-md-end",
                ),
                html.P(
                    "End aligned text on viewport sized large or wider",
                    className="text-lg-end",
                ),
                html.P(
                    "End aligned text on viewport sized extra large or wider",
                    className="text-xl-end",
                ),
                html.P(
                    "End aligned text on viewport sized extra extra large",
                    className="text-xxl-end",
                ),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


app.layout = html.Div([title, text_start, text_center, text_end])

if __name__ == "__main__":
    app.run(debug=True)

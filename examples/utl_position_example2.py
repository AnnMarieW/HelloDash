from dash import Dash, dcc, html, Input, Output, State, ctx
import dash_bootstrap_components as dbc

OVERFLOW = 10

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


title = dcc.Markdown(
    """
### Position Examples - Interactive Indicators
------------
"""
)

badge = html.Div(
    [
        dcc.Store(id="utl_position_example2-x-counter", data=10),
        dbc.Button(
            [
                "Notifications",
                dbc.Badge(
                    color="danger",
                    pill=True,
                    text_color="white",
                    className="position-absolute top-0 start-100 translate-middle",
                    id="utl_position_example2-x-counter-display",
                ),
            ],
            color="primary",
            className="position-relative",
        ),
    ],
    className="my-2",
)

plus_minus_buttons = html.Div(
    [
        dbc.Button("+", id="utl_position_example2-x-plus", size="sm", className="me-2"),
        dbc.Button("-", id="utl_position_example2-x-minus", size="sm"),
    ]
)

app.layout = html.Div(
    [title, html.Div("Demo of counter overflow set to 10"), badge, plus_minus_buttons]
)


@app.callback(
    Output("utl_position_example2-x-counter-display", "children"),
    Output("utl_position_example2-x-counter", "data"),
    Input("utl_position_example2-x-plus", "n_clicks"),
    Input("utl_position_example2-x-minus", "n_clicks"),
    State("utl_position_example2-x-counter", "data"),
)
def update_counters(n_plus, n_minus, counter):
    if ctx.triggered_id == "utl_position_example2-x-plus":
        counter += 1
    if ctx.triggered_id == "utl_position_example2-x-minus":
        counter -= 1
    counter_display = f"{OVERFLOW}+" if counter >= OVERFLOW else counter
    return counter_display, counter


if __name__ == "__main__":
    app.run_server(debug=True)

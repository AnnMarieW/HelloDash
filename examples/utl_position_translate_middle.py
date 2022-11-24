from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

square = html.I(className="fas fa-square fs-3")

translate_middle = dbc.Card(
    [
        html.Div(square, className="position-absolute translate-middle top-0 start-0 "),
        html.Div(square, className="position-absolute translate-middle top-0 start-50"),
        html.Div(
            square, className="position-absolute translate-middle top-0 start-100"
        ),
        html.Div(square, className="position-absolute translate-middle top-50 start-0"),
        html.Div(
            square, className="position-absolute translate-middle top-50 start-50"
        ),
        html.Div(
            square, className="position-absolute translate-middle top-50 start-100"
        ),
        html.Div(
            square, className="position-absolute translate-middle top-100 start-0"
        ),
        html.Div(
            square, className="position-absolute translate-middle top-100 start-50"
        ),
        html.Div(
            square, className="position-absolute translate-middle top-100 start-100"
        ),
    ],
    className="position-relative m-4 p-4",
    style={"height": 400, "width": 400},
)


app.layout = html.Div(translate_middle)

if __name__ == "__main__":
    app.run(debug=True)

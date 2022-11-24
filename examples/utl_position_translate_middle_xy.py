from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

square = html.I(className="fas fa-square fs-3")

translate_middle_xy = dbc.Card(
    [
        html.Div(square, className="position-absolute top-0 start-0 "),
        html.Div(
            square, className="position-absolute  top-0 start-50 translate-middle-x"
        ),
        html.Div(square, className="position-absolute  top-0 end-0"),
        html.Div(
            square, className="position-absolute  top-50 start-0 translate-middle-y"
        ),
        html.Div(
            square, className="position-absolute top-50 start-50 translate-middle"
        ),
        html.Div(
            square, className="position-absolute  top-50 end-0 translate-middle-y"
        ),
        html.Div(square, className="position-absolute  bottom-0 start-0"),
        html.Div(
            square, className="position-absolute  bottom-0 start-50 translate-middle-x"
        ),
        html.Div(square, className="position-absolute  bottom-0 end-0"),
    ],
    className="position-relative m-4 p-4",
    style={"height": 400, "width": 400},
)

app.layout = html.Div(translate_middle_xy)

if __name__ == "__main__":
    app.run(debug=True)

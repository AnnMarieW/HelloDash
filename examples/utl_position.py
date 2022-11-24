from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)

square = html.I(className="fas fa-square fs-3")

arrange_elements = dbc.Card(
    [
        html.Div(square, className="position-absolute top-0 start-0 "),
        html.Div(square, className="position-absolute top-0 end-0"),
        html.Div(square, className="position-absolute top-50 start-50"),
        html.Div(square, className="position-absolute  bottom-50 end-50"),
        html.Div(square, className="position-absolute bottom-0 start-0"),
        html.Div(square, className="position-absolute bottom-0 end-0"),
    ],
    className="position-relative p-4",
    style={"height": 400, "width": 400},
)

app.layout = html.Div(arrange_elements)

if __name__ == "__main__":
    app.run(debug=True)

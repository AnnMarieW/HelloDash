from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])

buttons = html.Div(
    [
        dbc.Button("Primary", className="m-1"),
        dbc.Button("Secondary", color="secondary", className="m-1"),
        dbc.Button("Warning", color="warning", className="m-1"),
        dbc.Button("Danger", color="danger", outline=True, className="m-1"),
        dbc.Button(
            ["Info - with icon", html.I(className="fa-solid fa-cloud-arrow-down ms-2")],
            color="info",
            className="m-1",
        ),
    ]
)

app.layout = dbc.Container(dbc.Row(dbc.Col(buttons)), fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)

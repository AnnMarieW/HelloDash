import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H1("Title"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col("row 1, column 1 content", md=6),
                dbc.Col("row 1, column 2 content", md=6),
            ],
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)

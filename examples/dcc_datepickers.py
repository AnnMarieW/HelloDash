from datetime import date
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

datepicker_single = html.Div(
    dcc.DatePickerSingle(date=date(2022, 8, 5), className="mb-2")
)
datepicker_range = html.Div(
    dcc.DatePickerRange(
        start_date=date(2022, 8, 5), end_date=date(2022, 8, 25), className="mb-2"
    )
)

with_theme = html.Div(
    [
        html.H3("Datepickers"),
        html.H5("Select a date to see the theme applied to the calendar"),
        dbc.Label("dcc.DatePickerSingle and dcc.DatePickerRange with Bootstrap theme"),
        datepicker_single,
        datepicker_range,
    ],
    className="dbc",
)


without_theme = html.Div(
    [dbc.Label("Without theme", className="mt-4"), datepicker_single, datepicker_range]
)

app.layout = dbc.Container([with_theme, without_theme])

if __name__ == "__main__":
    app.run_server(debug=True)

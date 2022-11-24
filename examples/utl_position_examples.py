from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME]
)


title = dcc.Markdown(
    """
### Position Examples - Indicators
------------
"""
)


indicator = dbc.Button(
    [
        "Notifications",
        dbc.Badge(
            "5",
            color="danger",
            pill=True,
            text_color="white",
            className="position-absolute top-0 start-100 translate-middle",
        ),
    ],
    color="primary",
    className="position-relative",
)


indicator_circle = dbc.Button(
    [
        "Profile",
        html.Div(
            className="position-absolute top-0 start-100 translate-middle p-2 bg-danger rounded-circle"
        ),
    ],
    color="primary",
    className="position-relative",
)


indicator_icon = dbc.Button(
    [
        "Notifications",
        dbc.Badge(
            [html.I(className="fas fa-triangle-exclamation")],
            color="danger",
            pill=True,
            text_color="white",
            className="position-absolute top-0 start-100 translate-middle",
        ),
    ],
    color="primary",
    className="position-relative",
)


indicator_icon2 = dbc.Button(
    [
        html.Div([html.I(className="fas fa-envelope fa-2x")]),
        dbc.Badge(
            "New",
            color="danger",
            pill=True,
            text_color="white",
            className="position-absolute top-0 start-100 translate-middle",
        ),
    ],
    color="primary",
    className="position-relative",
)


indicator_badge_badge = dbc.Badge(
    [
        html.I(className="fas fa-bell fs-3"),
        dbc.Badge(
            "5",
            color="danger",
            pill=True,
            text_color="white",
            className="position-absolute top-0 start-100 translate-middle",
        ),
    ],
    color="primary",
    text_color="white",
    className="position-relative",
)


badge_card = dbc.Card(
    [
        html.Div("Employee of the Month", className="text-center"),
        html.Img(
            src="https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png",
            style={"height": 65},
            className="position-absolute top-0 start-0 translate-middle rounded-circle img-fluid",
        ),
    ],
    body=True,
    color="success",
    className="position-relative text-white",
    style={"width": 200, "height": 75},
)


app.layout = html.Div(
    [
        title,
        html.Div(indicator, className="p-2"),
        html.Div(indicator_circle, className="p-2"),
        html.Div(indicator_icon, className="p-2"),
        html.Div(indicator_icon2, className="p-2"),
        html.Div(indicator_badge_badge, className="p-2"),
        html.Div(badge_card, className="my-4 p-4"),
    ],
    className="",
)

if __name__ == "__main__":
    app.run_server(debug=True)

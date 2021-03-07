import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server


header = dbc.Jumbotron(
    [
        html.H1("Dash Bootstrap Theme Explorer", className="display-3"),
        html.P(
            "The easy way to see Boostrap themes and Plotly  graph templates and colors in a Dash app.",
            className="lead",
        ),
        html.P(
            " Creating a beautiful design for your app starts here!",
            className=" font-italic",
        ),
        html.Hr(className="my-2"),
        html.Div(
            [
                dbc.Button(
                    "Theme Explorer",
                    color="primary",
                    #  outline=True,
                    href="/theme_explorer",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "App Gallery",
                    id="app_gallery_v03",
                    color="primary",
                    #    outline=True,
                    href="/app_gallery",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "Dash Bootstrap Components",
                    color="primary",
                    outline=True,
                    target="_blank",
                    className="mr-2",
                    href="https://dash-bootstrap-components.opensource.faculty.ai/",
                    size="sm",
                ),
                dbc.Button(
                    "Dash Documentation",
                    color="primary",
                    outline=True,
                    target="_blank",
                    href="https://dash.plotly.com/",
                    size="sm",
                ),
            ],
            className="mt-2",
        ),
    ]
)

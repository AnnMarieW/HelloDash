import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


bootswatch = [
    "CERULEAN",
    "COSMO",
    "FLATLY",
    "JOURNAL",
    "LITERA",
    "LUMEN",
    "LUX",
    "MATERIA",
    "MINTY",
    "PULSE",
    "SANDSTONE",
    "SIMPLEX",
    "SKETCHY",
    "SPACELAB",
    "UNITED",
    "YETI",
    "CYBORG",
    "DARKLY",
    "SLATE",
    "SOLAR",
    "SUPERHERO",
]

urls = {}
urls[
    "BOOTSTRAP"
] = "https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
for theme in bootswatch:
    urls[
        theme
    ] = f"https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/{theme.lower()}/bootstrap.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

# loading 2 stylesheets reduces the flicker when changing themes
external_stylesheets = [urls["BOOTSTRAP"], urls["BOOTSTRAP"], FONT_AWESOME]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server


header = dbc.Jumbotron(
    [
        html.H1("Dash Bootstrap Theme Explorer", className="display-3"),
        html.P(
            "The easy way to see Boostrap themes and Plotly  graph templates and colors in a Dash app.",
            className="lead",
        ),
        html.P("Your app design starts here!", className=" font-italic",),
        html.Hr(className="my-2"),
        html.Div(
            [
                dbc.Button(
                    "Theme Explorer",
                    color="primary",
                    outline=True,
                    href="/theme_explorer",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "App Gallery",
                    id="app_gallery",
                    color="primary",
                    outline=True,
                    href="/app_gallery",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "Cheatsheet",
                    id="cheatsheet",
                    color="primary",
                    outline=True,
                    href="/cheatsheet",
                    className="mr-2",
                    size="sm",
                ),
                # dbc.Button(
                #     "Dash Bootstrap Components",
                #     color="primary",
                #     outline=True,
                #     target="_blank",
                #     className="mr-2",
                #     href="https://dash-bootstrap-components.opensource.faculty.ai/",
                #     size="sm",
                # ),
                # dbc.Button(
                #     "Dash Documentation",
                #     color="primary",
                #     outline=True,
                #     target="_blank",
                #     href="https://dash.plotly.com/",
                #     size="sm",
                # ),
            ],
            className="mt-2",
        ),
    ]
)

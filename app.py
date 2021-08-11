import dash
import dash_bootstrap_components as dbc
import dash_labs as dl


FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

# loading 2 stylesheets reduces the flicker when changing themes
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.themes.BOOTSTRAP, FONT_AWESOME]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    title="HelloDash",
)

server = app.server

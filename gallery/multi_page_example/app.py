"""
This is a demo of how to set a different theme for pages in a multi-page app
See more about multi-page apps in `dash-labs`

requires:  dash-labs>=1.01 dash-bootstrap-components>=1.0 dash-bootstrap-templates>=1.04

"""

import dash
from dash import html, dcc, Input, Output
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO

# This stylesheet defines the `dbc` class.  Add `className="dbc"` to style `dash-core-components`
# and the `DataTable` with a Bootstrap theme.
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
)

app = dash.Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css],
)

# The theme is specified for each page in `dash.register_page()`
# If no theme is specified, it defaults to dbc.themes.BOOTSTRAP
path_to_theme = {
    page["path"]: page.get("theme", dbc.themes.BOOTSTRAP)
    for page in dash.page_registry.values()
}

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

# Note the theme change button is added to the layout, but it's hidden with `className="d-none".
# Rather than the user selecting the theme, it's updated in the callback below.
theme_changer = html.Div(
    ThemeChangerAIO(aio_id="theme", radio_props={"value": dbc.themes.FLATLY}),
    className="d-none",
)


app.layout = dbc.Container(
    [navbar, dl.plugins.page_container, theme_changer, dcc.Location(id="location")],
    fluid=True,
    className="dbc",
)


@app.callback(
    Output(ThemeChangerAIO.ids.radio("theme"), "value"), Input("location", "pathname")
)
def update_theme(path):
    return path_to_theme[path]


if __name__ == "__main__":
    app.run_server(debug=True)
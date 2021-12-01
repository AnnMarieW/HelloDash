
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import util
from apps import app_dcc_gallery, app_figure_templates, app_dbc_gallery, app_theme_change_components


# specify version or latest version
#dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")
dbc_css1 = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP,
                          dbc_css1,
                          ],
                suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                    title="Theme-Explorer",
          )

app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),
        util.theme_explorer_header,
        dbc.Row(
            [
                dbc.Col(util.side_nav,width=4, lg=2),
                dbc.Col(id="page-content", width=8, lg=10)
            ]
        )
    ],
    fluid=True
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname.startswith("/theme_explorer"):
        return app_dbc_gallery.layout
    if pathname == "/figure_templates":
        return app_figure_templates.layout
    if pathname == "/about_dbc_css":
        return app_dcc_gallery.layout
    if pathname == "/theme_change_components":
        return app_theme_change_components.layout
    # elif pathname == "/cheatsheet":
    #     return cheatsheet.layout
    #     Note - the cheatsheet is an external site and is
    #     controlled in the button and the link directly
    if pathname == "/dash_labs":
        return html.H2(
            "Dash Labs Explorer is being moved to a new site.  Please check back later"
        )
    if pathname == "/gallery":
        return html.H2(
            "The app gallery is being updated - please check back later"
        )
    else:
        return app_dbc_gallery.layout


if __name__ == "__main__":
    app.run_server(debug=True)

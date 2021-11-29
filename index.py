
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import util
from apps import component_gallery, figure_templates


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

app.layout = html.Div(
    [
        util.theme_explorer_header,
        dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/theme_explorer":
        return component_gallery.layout
    if pathname == "/figure_templates":
        return figure_templates.layout
    # # elif pathname == "/app_gallery":
    #     return app_gallery.layout
    # elif pathname == "/cheatsheet":
    #     return cheatsheet.layout
    #     Note - the cheatsheet is an external site and is
    #     controlled in the button and the link directly
    elif pathname == "/dash_labs":
        return html.H2(
            "Dash Labs Explorer is being moved to a new site.  Please check back later"
        )
    else:
        return component_gallery.layout


if __name__ == "__main__":
    app.run_server(debug=True)

from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import util
from apps import (
    app_dcc_gallery,
    app_figure_templates,
    app_dbc_gallery,
    app_theme_change_components,
)


# specify version or latest version
# dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css")
dbc_css1 = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app_description = """
A guide for styling Plotly Dash apps with a Bootstrap theme.  Shows how to include Bootstrap-themed Plotly figure templates,
apply Bootstrap themes to Plotly Dash components and switch themes with a theme change component.
"""
app_title = "Dash Bootstrap Theme Explorer"

metas = [
    {"property":"twitter:card", "content":app_description},
    {"property":"twitter:url", "content":"https://metatags.io/"},
    {"property":"twitter:title", "content":app_title},
    {"property":"twitter:description", "content":app_description},
    {"property":"twitter:image", "content":"/assets/home.jpeg"},

    {"property":"og:title", "content":app_title},
    {"property":"og:type", "content":"website"},
    {"property":"og:description", "content":app_description},
    {"property":"og:image", "content":"/assets/home.jpeg"}
]




app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.SPACELAB,
        dbc.icons.BOOTSTRAP,
        dbc_css1,
    ],
    suppress_callback_exceptions=True,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        {"name": "description", "content": app_description},
    ] + metas,
    title="Dash Bootstrap Theme Explorer",
)

app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh=False),
        util.theme_explorer_header,
        dbc.Row(
            [
                dbc.Col(util.side_nav, width=4, lg=2),
                dbc.Col(id="page-content", width=8, lg=10),
            ]
        ),
    ],
    fluid=True,
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
        return html.Div(
            """
        The Dash Labs Explorer was originally created as a live demo of the templates being developed in version 0.4.0.
          Based on community feedback, these templates are not longer being developed. 
          This page is a placeholder for now -- it will be used to showcase other Dash Labs features in the future. 
        """
        )
    if pathname == "/gallery":
        return html.H2("The app gallery is being updated - please check back later")
    else:
        return app_dbc_gallery.layout


if __name__ == "__main__":
    app.run_server(debug=True)

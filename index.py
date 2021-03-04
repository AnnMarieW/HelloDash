import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import Input, Output
from apps import (
    theme_explorer_v03,
    app_gallery,
)


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/theme_explorer":
        return theme_explorer_v03.layout
    elif pathname == "/app_gallery":
        return app_gallery.layout
    else:
        return theme_explorer_v03.layout


if __name__ == "__main__":
    app.run_server(debug=True)

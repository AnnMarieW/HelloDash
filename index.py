import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import Input, Output
from apps import (
    theme_explorer,
    app_gallery,
    cheatsheet,
)


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/theme_explorer":
        return theme_explorer.layout
    elif pathname == "/app_gallery":
        return app_gallery.layout
    elif pathname == "/cheatsheet":
        return cheatsheet.layout
    else:
        return theme_explorer.layout


if __name__ == "__main__":
    app.run_server(debug=True)

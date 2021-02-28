import dash_core_components as dcc
import dash_html_components as html

from app import app
from dash.dependencies import Input, Output
from apps import theme_explorer, theme_explorer_v02, theme_explorer_v03, learn_more


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/apps/theme_explorer":
        return theme_explorer_v03.layout
    elif pathname == "/v01":
        return theme_explorer.layout
    elif pathname == "/v02":
        return theme_explorer_v02.layout
    elif pathname == "/v03":
        return theme_explorer_v03.layout
    elif pathname == "/learn_more":
        return learn_more.layout
    else:
        return theme_explorer_v03.layout


if __name__ == "__main__":
    app.run_server(debug=True)

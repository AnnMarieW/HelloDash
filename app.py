import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

from lib.utils import example_apps

from lib.nav import theme_explorer_header, make_side_nav


# syntax highlighting light or dark
light_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-light.min.css"
dark_hljs = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/stackoverflow-dark.min.css"


# stylesheet with the .dbc class
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
)

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.SPACELAB,
        dbc.icons.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        dbc_css,
        dark_hljs,
    ],
    suppress_callback_exceptions=True,
)


for k in example_apps:
    new_callback_map = example_apps[k].callback_map
    new_callback_list = example_apps[k]._callback_list

    app.callback_map.update(new_callback_map)
    app._callback_list.extend(new_callback_list)


app.layout = dbc.Container(
    [
        theme_explorer_header,
        dcc.Location(id="url", refresh=True),
        dbc.Row(
            [
                dbc.Col(make_side_nav(), xs=5, md=3, xl=2, id="sidebar"),
                dbc.Col(
                    html.Div(
                        dash.page_container, className="p-2", style={"minWidth": 600},
                    ),
                    xs=7,
                    md=9,
                    xl=10,
                    id="content"
                ),
            ],

        ),
    ],
    fluid=True,
)

#
# @app.callback(
#     Output("header", "style"),
#     Output("sidebar", "style"),
#     Output("content", "xs"),
#     Output("content", "md"),
#     Output("content", "xl"),
#     Output("content", "children"),
#     Input("url", "pathname")
# )
# def hide_nav(path):
#     # Hide header and sidebar if james webb telescope page
#     if path.startswith("/webb") or path.startswith("/james"):
#         return {"display":"none"}, {"display":"none"}, 12, 12, 12, dash.page_container
#     return {"minHeight": 375}, {}, 6, 9, 10, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)

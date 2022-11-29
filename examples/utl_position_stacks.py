from dash import Dash, dcc, html, Input, Output, ctx
import dash_bootstrap_components as dbc


app = Dash(
    __name__, external_stylesheets=[dbc.themes.BOOTSTRAP]
)


title = dcc.Markdown(
    """
    

### Position - Vertical Layouts 

Use `"vstack"` in the `className` prop to create vertical layouts.  Stacked items are full-width by default.  Use the `"gap-*"`
utilities to add space between items. 

Use "hstack" to create a horizontal layout.  

------------
"""
)


stack = html.Div(
    [
        dbc.Button("hstack", id="utl_position_stacks-x-hstack"),
        dbc.Button("vstack", id="utl_position_stacks-x-vstack"),
        html.Div("First item", className="bg-light border"),
        html.Div("Second item", className="bg-light border"),
        html.Div("Third item", className="bg-light border"),
        html.Div("Third item", className="bg-light border"),
        html.Div("Third item", className="bg-light border"),
        html.Div("Third item", className="bg-light border"),
    ],
    className="vstack gap-3",
    id = "utl_position_stacks-x-stack"
)


app.layout= html.Div([title, stack])

@app.callback(
    Output("utl_position_stacks-x-stack", "className"),
    Input("utl_position_stacks-x-hstack", "n_clicks"),
    Input("utl_position_stacks-x-vstack", "n_clicks"),
)
def change_layout(h, v):
    if ctx.triggered_id == "utl_position_stacks-x-hstack":
        return "vstack gap-3"
    return "hstack gap-3"


if __name__ == "__main__":
    app.run(debug=True)


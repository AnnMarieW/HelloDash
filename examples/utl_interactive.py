from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc


cheatsheet_img = "https://user-images.githubusercontent.com/72614349/195447550-f0e8c647-4036-4298-97ba-52a66fba7ca9.png"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

sandbox = dbc.Card(
    html.Div("Hello Dash", id="utl-sandbox"),
    style={"height": 300},
    className="shadow position-relative my-2",
)

input_class_name = dbc.FormFloating(
    [
        dbc.Input(
            type="text",
            value="bg-primary text-white",
            autocomplete="off",
            id="utl-class-name",
        ),
        dbc.Label("className="),
    ]
)

demo_intro = """
### Live Demo
Try styling this "Hello Dash" div.  Enter Bootstrap classes here:
"""


gif = "https://user-images.githubusercontent.com/72614349/197416744-9b57ce8d-f300-4497-a532-78e02aa6e5a1.gif"
gif = html.Img(src=gif, className="mt-4 img-fluid")
modal_demo = html.Div(
    [
        dbc.Button(
            "See Demo",
            id="utility-demo-btn",
            n_clicks=0,
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Demo"),
                dbc.ModalBody(gif),
            ],
            is_open=False,
            size="lg",
            id="utility-demo-modal",
        ),
    ]
)

app.layout = dbc.Container(
    [
        dcc.Markdown(demo_intro),
        input_class_name,
        dbc.Row(dbc.Col(sandbox)),
        html.Div(id="utl-code", className="my-2"),
        modal_demo,
    ],
    fluid=True,
    className="dbc",
)


@app.callback(
    Output("utl-sandbox", "className"),
    Output("utl-code", "children"),
    Input("utl-class-name", "value"),
)
def update_sandbox(class_name):
    code = f"""\n
    html.Div(
        children="Hello Dash",
        className="{class_name}"
    )
    """

    code = dcc.Markdown(f"```python\n{code} \n")
    return class_name, code


@app.callback(
    Output("utility-demo-modal", "is_open"),
    Input("utility-demo-btn", "n_clicks"),
)
def open_modal(n):
    if n:
        return True


if __name__ == "__main__":
    app.run_server(debug=True)

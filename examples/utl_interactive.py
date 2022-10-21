from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc


cheatsheet_img = "https://user-images.githubusercontent.com/72614349/195447550-f0e8c647-4036-4298-97ba-52a66fba7ca9.png"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

sandbox = dbc.Card(
    html.Div("Hello Dash", id="utl-sandbox"),
    style={"height": 300},
    className="shadow m-5 position-relative",
)

input_class_name = dbc.FormFloating(
    [
        dbc.Input(type="text", placeholder="Enter Bootstrap Utility Class",
                  value="bg-primary text-white", autocomplete="off" ,id="utl-class-name"),
        dbc.Label("className="),
    ]
)

demo_intro = """
### Live Demo
Try styling this "Hello Dash" div with Bootstrap classes.  Enter them here:
"""


app.layout = dbc.Container(
    [
        dcc.Markdown(demo_intro),
        input_class_name,
        html.Div(id="utl-code", className="mt-2"),
        dbc.Row(dbc.Col(sandbox)),
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


if __name__ == "__main__":
    app.run_server(debug=True)

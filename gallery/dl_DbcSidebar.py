# -*- coding: utf-8 -*-
"""
Dash Labs demo of DbcSidebar Template
"""

import dash_labs as dl
import dash
import numpy as np
import dash_core_components as dcc
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])
tpl = dl.templates.dbc.DbcSidebar(
    app, title="Sample App", figure_template=True, theme=dbc.themes.MINTY
)


dropdown = dcc.Dropdown(
    options=[{"label": i, "value": i} for i in ["sin", "cos", "exp"]], value="sin"
)
textbox = dcc.Textarea("Initial Title")
slider = dcc.Slider(
    min=1, max=10, value=2, tooltip={"placement": "bottom", "always_visible": True}
)
slider2 = dcc.Slider(
    min=1, max=10, value=6, tooltip={"placement": "bottom", "always_visible": True}
)


@app.callback(
    # dl.Output(html.Div(), "children"),  not needed - this is implied
    dl.Input(dropdown, label="Function"),
    dl.Input(textbox, label="Figure Title"),
    dl.Input(slider, label="Phase"),
    dl.Input(slider2, label="Amplitude"),
    template=tpl,
)
def callback(fun, figure_title, phase, amplitude):

    xs = np.linspace(-10, 10, 100)
    np_fn = getattr(np, fun)
    x = xs
    y = np_fn(xs + phase) * amplitude

    return dcc.Graph(figure=px.line(x=x, y=y).update_layout(title_text=figure_title))


app.layout = dbc.Container(fluid=True, children=tpl.children)

if __name__ == "__main__":
    app.run_server(debug=True)

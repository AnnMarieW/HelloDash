from dash.dependencies import Input
import dash_labs as dl
import dash_core_components as dcc
import plotly.express as px
import numpy as np

from app import app
import util

tpl = dl.templates.FlatDiv(app)


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
    Input("themes", "value"),
    Input("graph_template", "value"),
    Input("discrete_selected", "children"),
    Input("checkbox", "value"),
    template=tpl,
)
def callback(
    fun, figure_title, phase, amplitude, theme, template, color_discrete, checkbox,
):
    # figure line colors default is from the generated Bootstrap figure template.  These can be changed
    # in the app by selecting a different color sequence
    color_discrete = color_discrete.split(": ")[1].strip()
    line_colors = util.discrete_colors[color_discrete]
    if checkbox == []:
        line_colors = None
    if template == "bootstrap":
        template = util.url_dbc_themes[theme].lower()

    xs = np.linspace(-10, 10, 100)
    np_fn = getattr(np, fun)
    x = xs
    y = np_fn(xs + phase) * amplitude

    return dcc.Graph(
        figure=px.line(
            x=x, y=y, template=template, color_discrete_sequence=line_colors,
        ).update_layout(title_text=figure_title)
    )

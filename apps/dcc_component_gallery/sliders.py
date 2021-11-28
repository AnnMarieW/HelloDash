import dash_bootstrap_components as dbc
from dash import html, dcc

from .util import dcc_make_subheading

slider = html.Div(
    [
        dcc.Slider(
            min=0, max=9, marks={i: "Label {}".format(i) for i in range(10)}, value=5,
        )
    ]
)


range_slider = html.Div(
    [
        dcc.RangeSlider(
            marks={i: "Label {}".format(i) for i in range(-5, 7)},
            min=-5,
            max=6,
            value=[-3, 4],
        )
    ]
)


dcc_range_slider = html.Div(
    [dcc_make_subheading("dcc.RangeSlider", "rangeslider"), dbc.Row(range_slider)],
    className="mb-4",
)


dcc_slider = html.Div(
    [dcc_make_subheading("dcc.Slider", "slider"), dbc.Row(slider)], className="mb-4",
)

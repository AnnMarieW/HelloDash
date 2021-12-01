import dash_bootstrap_components as dbc
from dash import html

import apps.dcc_component_gallery as dcc_gallery
import apps.dbc_component_gallery as dbc_gallery
import util


dbc_gallery_div = html.Div(
    [
        dbc_gallery.intro,
        dbc_gallery.alerts,
        dbc_gallery.badges,
        dbc_gallery.buttons,
        dbc_gallery.cards,
        dbc_gallery.collapse,
        dbc_gallery.fade,
        dbc.Row(
            [
                dbc.Col([dbc_gallery.form, dbc_gallery.input_group], xs=12, md=6),
                dbc.Col([dbc_gallery.input_], xs=12, md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([dbc_gallery.checklist_items], xs=12, md=6),
                dbc.Col([dbc_gallery.radio_items], xs=12, md=6),
            ]
        ),
        dbc_gallery.list_group,
        dbc_gallery.modal,
        dbc_gallery.navbar,
        dbc_gallery.popover,
        dbc_gallery.progress,
        dbc_gallery.spinner,
        dbc_gallery.table,
        dbc_gallery.tabs,
        dbc_gallery.toast,
        dbc_gallery.tooltip,
    ]
)

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        util.make_header("About Theme Explorer", spacing=""),
                        dbc_gallery.about_explorer,
                        dcc_gallery.sample_layout,
                        util.make_header("Dash Bootstrap Component Gallery"),
                        dbc_gallery_div,
                    ],
                ),
            ],
        ),
    ],
    className="dbc",
)

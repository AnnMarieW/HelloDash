
import dash_bootstrap_components as dbc
from dash import html


import apps.dcc_component_gallery as dcc_gallery
import apps.dbc_component_gallery as dbc_gallery
from .about_dbc_css import about_dbc_css_md


heading_theme_explorer = html.H2(
    "Theme Explorer - Sample App",
    className="text-white bg-primary p-2",
)


heading_dbc = html.H2(
    "Dash Bootstrap Component Gallery",
    className="text-white bg-primary p-2 mt-4",
    id="dbc",
)

heading_dcc = html.H2(
    "Dash Component Gallery -- with className='dbc'",
    className="text-white bg-primary p-2 mt-4",
    id="dcc",
)


heading_about_dbc_css = html.H2(
    "About dbc.css stylesheet",
    className="text-white bg-primary p-2",
)


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



def make_dcc_gallery():
    content = html.Div(
        [
            dcc_gallery.about_dcc_md,
            dcc_gallery.datatable,
            dcc_gallery.dcc_date_picker_single,
            dcc_gallery.dcc_date_picker_range,
            dcc_gallery.dcc_dropdowns,
            dcc_gallery.dcc_markdown,
            dcc_gallery.dcc_slider,
            dcc_gallery.dcc_range_slider,
            dcc_gallery.dcc_tabs,
        ]
    )
    return dbc.Row(
        [
            dbc.Col(
                dbc.Card(content),
                className="dbc",
            ),
        ]
    )


about_dbc_css = dbc.Row(
        [
            dbc.Col(
                dbc.Card([heading_about_dbc_css, about_dbc_css_md], outline=True, color="primary"),
                className="dbc",
            ),
        ]
    )

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                       # heading_theme_explorer,
                       # dcc_gallery.sample_layout_default,
                        html.Div([
                            dcc_gallery.sample_layout,
                            dcc_gallery.about_md,
                            heading_dbc,
                            dbc_gallery_div,
                            heading_dcc,
                            make_dcc_gallery(),
                            about_dbc_css
                        ], className="dbc")
                    ],
                ),
            ],
        ),
    ],

)






import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_templates import ThemeChangerAIO

import apps.dcc_component_gallery as dcc_gallery
import apps.dbc_component_gallery as dbc_gallery


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
    "About className='dbc'",
    className="text-white bg-primary p-2 mt-4",
    id="about-dbc-css",
)


side_nav = dbc.Card(
    [
        ThemeChangerAIO(
            aio_id="theme",
            button_props={"color": "primary", "outline": False},
            radio_props={"value": dbc.themes.SPACELAB},
        ),

        html.Div("Using Bootstrap themes with:", className="mt-4"),
        dbc.Nav(
            [
                dbc.NavLink(
                    "Dash Bootstrap Components", href="#dbc", external_link=True
                ),
                dbc.NavLink("Dash Core Components", href="#dcc", external_link=True),
                dbc.NavLink("DataTable", href="#dcc", external_link=True),
                dbc.NavLink("Figures", href="#mid", external_link=True),
            ],
            vertical=True,
            pills=True,

        ),
        html.Div("More info:", className="mt-4"),
        dbc.Nav(
            [

                dbc.NavLink("className='dbc'", href="#about-dbc-css", external_link=True),
                dbc.NavLink("Theme Change Components", href="#end", external_link=True),
                dbc.NavLink(
                    "Bootstrap Cheatsheet",
                    href="https://dashcheatsheet.pythonanywhere.com/",
                    external_link=True,
                    target="_blank",
                ),
                dbc.NavLink(
                    "Github -Theme Explorer",
                    href="https://github.com/AnnMarieW/HelloDash",
                    external_link=True,
                    target="_blank",
                ),
            ],
            vertical=True,
            pills=True,

        ),
    ],
    body=True,
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
                dbc.Card(content, outline=True, color="primary", body=True),
                className="dbc",
            ),
        ]
    )


about_dbc_css = dbc.Row(
        [
            dbc.Col(
                dbc.Card([heading_about_dbc_css, dcc_gallery.about_dbc_css_md], outline=True, color="primary", body=True),
                className="dbc",
            ),
        ]
    )

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([side_nav], width=2),
                dbc.Col(
                    [
                        dcc_gallery.about_md,
                        dcc_gallery.sample_layout_default,
                        html.Div([
                            dcc_gallery.sample_layout,
                            heading_dbc,
                            dbc_gallery_div,
                            heading_dcc,
                            make_dcc_gallery(),
                            about_dbc_css
                        ], className="dbc")
                    ],
                    width=10,
                ),
            ],
            className="mt-4",
        ),
    ],
    fluid=True,
)






#  todo Move to a different file
# def make_dcc_card():
#     """ This makes a comparison between with className=dbc and default"""
#     content = html.Div(
#         [
#             dcc_gallery.table,
#             dcc_gallery.dcc_date_picker_single,
#             dcc_gallery.dcc_date_picker_range,
#             dcc_gallery.dcc_dropdowns,
#             dcc_gallery.dcc_slider,
#             dcc_gallery.dcc_range_slider,
#             dcc_gallery.dcc_tabs,
#         ]
#     )
#     return dbc.Row(
#         [
#             dbc.Col(
#                 dbc.Card(
#                     [
#                         dbc.CardHeader(
#                             ' with ClassName="dbc"',
#                             className="card-title h3 overflow-auto text-nowrap",
#                         ),
#                         dbc.CardBody(content),
#                     ],
#                     outline=True,
#                     color="primary",
#                 ),
#                 width={"size": 5, "offset": 2},
#                 className="dbc",
#             ),
#             dbc.Col(
#                 dbc.Card(
#                     [
#                         dbc.CardHeader(
#                             "Default style",
#                             className="card-title h3 overflow-auto text-nowrap",
#                         ),
#                         dbc.CardBody(content),
#                     ]
#                 ),
#                 width=5,
#             ),
#         ]
#     )

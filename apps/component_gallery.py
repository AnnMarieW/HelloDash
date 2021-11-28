
import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_templates import ThemeChangerAIO

import apps.dcc_component_gallery as dcc_te
import apps.dbc_component_gallery as dbc_te


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
            button_props={"color": "primary"},
            radio_props={"value": dbc.themes.SPACELAB},
        ),

        html.Div("Bootstrap themes with:", className="mt-4"),
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
            ],
            vertical=True,
            pills=True,

        ),
    ],
    body=True,
)

dbc_gallery = html.Div(
    [
        dbc_te.intro,
        dbc_te.alerts,
        dbc_te.badges,
        dbc_te.buttons,
        dbc_te.cards,
        dbc_te.collapse,
        dbc_te.fade,
        dbc.Row(
            [
                dbc.Col([dbc_te.form, dbc_te.input_group], xs=12, md=6),
                dbc.Col([dbc_te.input_], xs=12, md=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([dbc_te.checklist_items], xs=12, md=6),
                dbc.Col([dbc_te.radio_items], xs=12, md=6),
            ]
        ),
        dbc_te.list_group,
        dbc_te.modal,
        dbc_te.navbar,
        dbc_te.popover,
        dbc_te.progress,
        dbc_te.spinner,
        dbc_te.table,
        dbc_te.tabs,
        dbc_te.toast,
        dbc_te.tooltip,
    ]
)



def make_dcc_gallery():
    content = html.Div(
        [
            dcc_te.about_dcc_md,
            dcc_te.datatable,
            dcc_te.dcc_date_picker_single,
            dcc_te.dcc_date_picker_range,
            dcc_te.dcc_dropdowns,
            dcc_te.dcc_markdown,
            dcc_te.dcc_slider,
            dcc_te.dcc_range_slider,
            dcc_te.dcc_tabs,
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
                dbc.Card([heading_about_dbc_css, dcc_te.about_dbc_css_md], outline=True, color="primary", body=True),
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
                        dcc_te.about_md,
                        dcc_te.sample_layout_default,
                        html.Div([
                            dcc_te.sample_layout,
                            heading_dbc,
                            dbc_gallery,
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
#             dcc_te.table,
#             dcc_te.dcc_date_picker_single,
#             dcc_te.dcc_date_picker_range,
#             dcc_te.dcc_dropdowns,
#             dcc_te.dcc_slider,
#             dcc_te.dcc_range_slider,
#             dcc_te.dcc_tabs,
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

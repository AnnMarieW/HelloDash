from dash import html
import dash_bootstrap_components as dbc
import apps.dcc_component_gallery as dcc_gallery
import util


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
    return dbc.Row([dbc.Col(dbc.Card(content), className="dbc",),])


def make_dcc_card():
    """ This makes a comparison between with className=dbc and default"""
    content = html.Div(
        [
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
                dbc.Card(
                    [
                        dbc.CardHeader(
                            ' with ClassName="dbc"',
                            className="card-title h3 overflow-auto text-nowrap",
                        ),
                        dbc.CardBody(content),
                    ],
                ),
                className="dbc",
                width=6,
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Default style",
                            className="card-title h3 overflow-auto text-nowrap",
                        ),
                        dbc.CardBody(content),
                    ]
                ),
                width=6,
            ),
        ]
    )


layout = html.Div(
    [
        #  dcc_gallery.about_dbc_css_md,
        util.make_header("Bootstrap-themed Dash Component Gallery", spacing=""),

     #   make_dcc_gallery(),
        dcc_gallery.about_examples_md,
        util.make_header("Side-by-Side comparison"),
        make_dcc_card(),
        util.make_header("How to use dbc.css Stylesheet in your App"),
        dcc_gallery.about_dbc_css_md,
    ],
    className="mb-4",
)

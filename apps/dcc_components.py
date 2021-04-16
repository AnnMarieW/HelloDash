import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from datetime import date
import time

DCC_HOME = "https://dash.plotly.com/dash-core-components"
DCC_GITHUB = "https://github.com/plotly/dash-core-components"
DCC_DOCS = "https://dash.plotly.com/dash-core-components/"

from apps import text
from app import app


"""
=====================================================================
Helper functions
"""


def make_subheading(label, link):
    return html.Div(
        [
            dbc.Button(
                [
                    html.H4(
                        [
                            label,
                            html.I(
                                className="far fa-question-circle ml-2",
                                style={"fontSize": 18},
                                id="tooltip_target",
                            ),
                        ],
                    )
                ],
                href=DCC_DOCS + link,
                target="_blank",
                color="link",
            ),
            dbc.Tooltip("Go to official documentation ", target="tooltip_target",),
        ],
    )


def make_btn_with_modal(id, title, content):
    """
     This makes a button that opens a modal for content
     note: The modal callback is located in the app_galery.py

     id:  unique identifier
     title:  what appears on the button
     content:
        To display text, use dcc.Markdown("my text")
        To display a codebox:
          html.Div(html.Pre(html.Code(" enter code here" )), className="codebox",)

    """
    return html.Div(
        [
            dbc.Button(
                title,
                id={"type": "modal_btn", "index": id},
                color="primary",
                size="sm",
                outline=True,
                className="mb-2",
            ),
            dbc.Modal(
                dbc.ModalBody(content),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="lg",
            ),
        ]
    )


def make_btn_with_link(link):
    return dbc.Button(
        "See Code",
        color="primary",
        target="_blank",
        href=link,  # github link
        size="sm",
        outline=True,
    )


"""
=====================================================================
Content
"""


checklist_items = (
    dbc.Card(
        [
            dcc.Checklist(
                options=[
                    {"label": "New York City", "value": "NYC"},
                    {"label": "Montréal", "value": "MTL"},
                    {"label": "San Francisco", "value": "SF"},
                ],
                value=["NYC", "MTL"],
            ),
            html.Br(),
            dcc.Checklist(
                options=[
                    {"label": "New York City", "value": "NYC"},
                    {"label": "Montréal", "value": "MTL"},
                    {"label": "San Francisco", "value": "SF"},
                ],
                value=["NYC", "MTL"],
                labelStyle={"display": "block"},
            ),
        ],
        className="p-2",
    ),
)


radio_items = (
    dbc.Card(
        [
            dcc.RadioItems(
                options=[
                    {"label": "New York City", "value": "NYC"},
                    {"label": "Montréal", "value": "MTL"},
                    {"label": "San Francisco", "value": "SF"},
                ],
                value="MTL",
            ),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {"label": "New York City", "value": "NYC"},
                    {"label": "Montréal", "value": "MTL"},
                    {"label": "San Francisco", "value": "SF"},
                ],
                value="MTL",
                labelStyle={"display": "block"},
                inputClassName="bg-danger",
            ),
        ],
        className="p-2",
    ),
)

dbc_checklist_radio = html.Div(
    [
        dbc.Checklist(
            id="gallery_checklist2",
            options=[{"label": "Option {}".format(i), "value": i} for i in range(4)],
            value=[0, 3],
            inline=True,
        ),
        dbc.RadioItems(
            id="gallery_radio2",
            options=[{"label": "Option {}".format(i), "value": i} for i in range(4)],
            value=[1],
            inline=True,
        ),
    ],
    className="mx-4 mb-4 px-5",
)

checklist_radio_card = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Row(
                [
                    make_subheading("dcc.Checklist", "checklist/"),
                    make_subheading("dcc.RadioItems", "radioitems/"),
                ]
            ),
        ),
        dcc.Markdown(text.dcc_checklist_radio_1, className="p-4"),
        dbc.CardBody([dbc.Row([dbc.Col(checklist_items), dbc.Col(radio_items)]),]),
        dcc.Markdown(text.dcc_checklist_radio_2, className="p-4"),
        dbc_checklist_radio,
    ],
    className="my-4",
)

datepicker_range = html.Div(
    [
        dcc.DatePickerRange(
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2021, 9, 19),
            initial_visible_month=date(2021, 8, 5),
            end_date=date(2021, 8, 25),
        ),
    ],
)

datepicker_single = html.Div(
    [
        dcc.DatePickerSingle(
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2021, 9, 19),
            initial_visible_month=date(2021, 8, 5),
            date=date(2021, 8, 25),
        ),
    ],
)


datepicker_card = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Row(
                [
                    make_subheading("dcc.DatePickerSingle", "datepickersingle/"),
                    make_subheading("dcc.DatePickerRange", "datepickerrange/"),
                ]
            ),
        ),
        dbc.CardBody(
            [dbc.Row([dbc.Col(datepicker_single), dbc.Col(datepicker_range)]),]
        ),
        #  dcc.Markdown(text.dcc_checklist_radio_text, className='p-4'),
    ],
    className="my-4",
)


def make_dropdowns(classname):
    return html.Div(
        [
            dcc.Dropdown(
                options=[
                    {"label": "New York City", "value": "NYC"},
                    {"label": "Montréal", "value": "MTL"},
                    {"label": "San Francisco", "value": "SF"},
                ],
                value="NYC",
                className=classname,
            ),
            html.Br(),
            dcc.Dropdown(
                options=[
                    {"label": "New York City", "value": "NYC"},
                    {"label": "Montréal", "value": "MTL"},
                    {"label": "San Francisco", "value": "SF"},
                ],
                value=["NYC", "MTL"],
                multi=True,
                className=classname,
            ),
        ],
    )


dropdown_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Dropdown", "dropdown/")),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.Markdown(text.dcc_dropdown, className="my-4"),
                        make_btn_with_modal(
                            "dcc_dropdown_css",
                            "see CSS",
                            dcc.Markdown(text.dcc_dropdown_css),
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    ["Styled for all themes:", make_dropdowns("")],
                                    lg=6,
                                    className="mb-4",
                                ),
                                dbc.Col(
                                    [
                                        "Styled for dark themes with className='dbc_dark':",
                                        make_dropdowns("dbc_dark"),
                                    ],
                                    lg=6,
                                ),
                            ],
                            className="mb-4",
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="my-4",
)


df = px.data.gapminder()
dff = df.query("year==2007")
fig = px.scatter(
    dff, x="gdpPercap", y="lifeExp", size="pop", color="continent", size_max=60,
)
fig1 = px.scatter(
    dff,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    size_max=60,
    template="plotly_dark",
)
fig1.update_layout(
    {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)",}
)
graph_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Graph", "graph/")),
        dbc.CardBody(
            [
                dcc.Markdown(text.dcc_graph),
                make_btn_with_modal(
                    "dcc_graph", "see code", dcc.Markdown(text.dcc_graph_code)
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4("Default style"),
                                dcc.Graph(
                                    id="dcc_graph", figure=fig, className="border"
                                ),
                            ],
                            lg=6,
                            className="mb-4",
                        ),
                        dbc.Col(
                            [
                                html.H4("See this style with a dark theme!"),
                                dcc.Graph(
                                    id="dcc_graph", figure=fig1, className="border"
                                ),
                            ],
                            lg=6,
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="my-4",
)

ALLOWED_TYPES = (
    "number",
    "text",
    "password",
    "email",
    "search",
    "tel",
    "url",
    "range",
    "hidden",
)


def make_input_card(classname):
    return html.Div(
        [
            html.Div(
                [
                    dcc.Input(
                        id="input_{}".format(_),
                        type=_,
                        placeholder="input type {}".format(_),
                        className="m-1 p-2",
                    )
                    for _ in ALLOWED_TYPES
                ]
                + [html.Div(id="out-all-types")]
            ),
        ],
        className=classname,
    )


input_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Input", "input/")),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.Markdown(text.dcc_input, className="my-4"),
                        make_btn_with_modal(
                            "dcc_input_css",
                            "see CSS",
                            dcc.Markdown(text.dcc_input_css),
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    ["Dash Default", make_input_card("")],
                                    lg=6,
                                    className="mb-4",
                                ),
                                dbc.Col(
                                    [
                                        "Styled for dark themes with className='dbc_both_input':",
                                        make_input_card("dbc_both_input"),
                                    ],
                                    lg=6,
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="my-4",
)


loading_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Loading", "loading/"),),
        dbc.CardBody(
            [
                html.H3("Edit text input to see loading state"),
                dcc.Input(id="loading-input-1", value="Input triggers local spinner"),
                dcc.Loading(
                    id="loading-1",
                    type="default",
                    children=html.Div(id="loading-output-1"),
                ),
                html.Div(
                    [
                        dcc.Input(
                            id="loading-input-2", value="Input triggers nested spinner"
                        ),
                        dcc.Loading(
                            id="loading-2",
                            children=[html.Div([html.Div(id="loading-output-2")])],
                            type="circle",
                        ),
                    ]
                ),
            ],
        ),
    ],
    className="my-4",
)


def make_range_slider(classname):
    return dcc.RangeSlider(
        min=0,
        max=10,
        step=None,
        marks={0: "0 °F", 3: "3 °F", 5: "5 °F", 7.65: "7.65 °F", 10: "10 °F",},
        value=[3, 7.65],
        className=classname,
    )


def make_slider(classname):
    return dcc.Slider(
        min=0,
        max=10,
        step=None,
        marks={0: "0 °F", 3: "3 °F", 5: "5 °F", 7.65: "7.65 °F", 10: "10 °F",},
        value=3,
        className=classname,
    )


slider_default_card = dbc.Card(
    [
        html.H4("Default slider style"),
        make_slider("m-4"),
        make_range_slider(("m-4")),
        html.Div("Sample selected theme colors"),
        dbc.ButtonGroup(
            [
                dbc.Badge("primary", color="primary", style={"margin": 2}),
                dbc.Badge("secondary", color="secondary", style={"margin": 2}),
                dbc.Badge("success", color="success", style={"margin": 2}),
            ],
        ),
    ],
    className="p-2",
)

slider_pulse_card = dbc.Card(
    [
        html.H4("Styled for PULSE theme "),
        make_slider("m-4 dash-bootstrap"),
        make_range_slider("m-4 dash-bootstrap"),
        html.Div("Sample PULSE colors"),
        html.Div(
            [
                dbc.Badge(
                    "primary",
                    style={"background": "#593196", "color": "white", "margin": 2},
                ),
                dbc.Badge(
                    "secondary",
                    style={"backgroundColor": "#a991d4", "color": "white", "margin": 2},
                ),
                dbc.Badge(
                    "success",
                    style={"backgroundColor": "#13b955", "color": "white", "margin": 2},
                ),
            ],
        ),
    ],
    className="p-2 dbc_pulse",
)


slider_card = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Row(
                [
                    make_subheading("dcc.Slider", "slider/"),
                    make_subheading("dcc.RangeSlider", "rangeslider/"),
                ]
            ),
        ),
        dcc.Markdown(text.dcc_slider, className="px-4 pt-4"),
        html.Div(
            make_btn_with_modal(
                "dcc_slider", "see CSS", dcc.Markdown(text.dcc_slider_css)
            ),
            className="pl-4",
        ),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(slider_default_card, lg=6, className="mb-4"),
                        dbc.Col(slider_pulse_card, lg=6),
                    ]
                ),
            ]
        ),
    ],
    className="my-4",
)

tabs_default = dbc.Card(
    [
        dcc.Tabs(
            id="tabs-example",
            value="tab-1",
            children=[
                dcc.Tab(label="Tab one", value="tab-1"),
                dcc.Tab(label="Tab two", value="tab-2"),
            ],
        ),
        html.Div(id="tabs-example-content"),
    ]
)


tabs_theme = dbc.Card(
    dcc.Tabs(
        [
            dcc.Tab(
                html.Div(
                    [
                        html.H5(
                            "Change theme to see the selected tab border is the "
                            "the theme's 'primary' color",
                            className="m-4 p-5",
                        )
                    ]
                ),
                label="Tab one",
                selected_className="border-primary text-dark",
                style={"backgroundColor": "transparent", "opacity": 0.6},
                selected_style={"backgroundColor": "transparent"},
            ),
            dcc.Tab(
                html.Div(html.Pre(html.Code(text.dcc_tabs_code)), className="codebox"),
                label="code",
                selected_className="border-primary text-dark",
                style={"backgroundColor": "transparent", "opacity": 0.6},
                selected_style={"backgroundColor": "transparent"},
            ),
        ]
    )
)


tabs_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Tabs", "tabs/")),
        dbc.CardBody(
            [
                dcc.Markdown(text.dcc_tabs),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col(tabs_default, lg=6, className="mb-4"),
                        dbc.Col(tabs_theme, lg=6),
                    ]
                ),
            ]
        ),
    ],
    className="my-4",
)


textarea_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Textarea", "textarea/")),
        dbc.CardBody(
            [
                dcc.Textarea(
                    value="Textarea content initialized\nwith multiple lines of text",
                ),
            ]
        ),
    ],
    className="my-4",
)

source_code = dcc.Markdown(
    """
    ## See the [source code](https://github.com/AnnMarieW/HelloDash/blob/main/apps/dcc_components.py)       
    """
)


layout = dbc.Container(
    [
        html.Div(
            [
                dcc.Markdown(text.dcc_intro_text),
                html.Hr(),
                slider_card,
                dropdown_card,
                tabs_card,
                checklist_radio_card,
                graph_card,
                input_card,
                datepicker_card,
                loading_card,
                textarea_card,
                html.Div(style={"height": "50px"}),
                source_code,
            ],
            className="my-2 p-4",
        ),
    ],
    fluid=True,
)


@app.callback(Output("loading-output-1", "children"), Input("loading-input-1", "value"))
def input_triggers_spinner(value):
    time.sleep(1)
    return value


@app.callback(Output("loading-output-2", "children"), Input("loading-input-2", "value"))
def input_triggers_nested(value):
    time.sleep(1)
    return value


@app.callback(
    Output("tabs-example-content", "children"), Input("tabs-example", "value")
)
def render_content(tab):
    if tab == "tab-1":
        return html.Div([html.H4("Default dcc.Tabs", className="m-4 p-5 text-center")])
    elif tab == "tab-2":
        return html.Div(
            [
                html.H4(
                    "Change to a dark theme to see that default style does not work well.",
                    className="m-4 p-5 text-center",
                )
            ]
        )

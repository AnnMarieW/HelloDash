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

header = dcc.Markdown(
    """            
    These are the components available in the Plotly `dash-core-components` library.  Click on the component names to go
     to the official Dash documentation and to see more examples.

     Change the Bootstrap theme in the App Design Selections panel to see how the components respond the different 
     Bootstrap themes.
     
     If you work for a company, consider using Dash Enterprise.  The Design Kit makes all this custom CSS unnecessary. 
    
""",
    id="dcc",
)


def make_subheading(label, link):
    return html.Div(
        [
            dbc.Button(
                [
                    html.H4(
                        [
                            label,
                            html.I(
                                className="far fa-question-circle ml-2 mb-2",
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


checklist_items = (
    html.Div(
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
        ]
    ),
)


radio_items = (
    html.Div(
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
        ]
    ),
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
        dbc.CardBody([dbc.Row([dbc.Col(checklist_items), dbc.Col(radio_items)]),]),
        dcc.Markdown(text.dcc_checklist_radio, className="p-4"),
    ],
    className="my-2",
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
    className="my-2",
)


dropdown_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Dropdown", "dropdown/")),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "New York City", "value": "NYC"},
                                {"label": "Montréal", "value": "MTL"},
                                {"label": "San Francisco", "value": "SF"},
                            ],
                            value="NYC",
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
                        ),
                        dcc.Markdown(text.dcc_dropdown, className="my-4"),
                    ]
                ),
            ]
        ),
    ],
    className="my-2",
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
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4("Default Style"),
                                dcc.Graph(id="dcc_graph", figure=fig,),
                            ]
                        ),
                        dbc.Col(
                            [
                                html.H4("Transparent background for dark themes"),
                                dcc.Graph(id="dcc_graph", figure=fig1,),
                            ]
                        ),
                    ]
                ),
                dcc.Markdown(text.dcc_graph),
            ]
        ),
    ],
    className="my-2",
)

ALLOWED_TYPES = (
    "text",
    "number",
    "password",
    "email",
    "search",
    "tel",
    "url",
    "range",
    "hidden",
)
input_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Input", "input/"),),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.Input(
                            id="input_{}".format(_),
                            type=_,
                            placeholder="input type {}".format(_),
                        )
                        for _ in ALLOWED_TYPES
                    ]
                    + [html.Div(id="out-all-types")]
                ),
            ]
        ),
    ],
    className="my-2",
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
    className="my-2",
)


rangeslider_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.RangeSlider", "rangeslider/")),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.RangeSlider(
                            min=0,
                            max=10,
                            step=None,
                            marks={
                                0: "0 °F",
                                3: "3 °F",
                                5: "5 °F",
                                7.65: "7.65 °F",
                                10: "10 °F",
                            },
                            value=[3, 7.65],
                        )
                    ]
                ),
            ]
        ),
    ],
    className="my-2",
)

slider_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Slider", "slider/")),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dcc.Slider(
                            id="slider-dark-theme",
                            min=0,
                            max=10,
                            step=None,
                            marks={
                                0: "0 °F",
                                3: "3 °F",
                                5: "5 °F",
                                7.65: "7.65 °F",
                                10: "10 °F",
                            },
                            value=3,
                        )
                    ],
                    className="slider-dark-theme",
                ),
            ]
        ),
    ],
    className="my-2",
)

tabs_card = dbc.Card(
    [
        dbc.CardHeader(make_subheading("dcc.Tabs", "tabs/")),
        dbc.CardBody(
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
                html.Hr(),
                dcc.Markdown(text.dcc_tabs),
            ]
        ),
    ],
    className="my-2",
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
    className="my-2",
)

source_code = dcc.Markdown(
    """
    ## See the [source code](https://github.com/AnnMarieW/HelloDash/blob/main/apps/dcc_components.py)       
    """
)


layout = dbc.Container(
    [
        dbc.Card(
            [
                header,
                html.Hr(),
                checklist_radio_card,
                tabs_card,
                dropdown_card,
                graph_card,
                datepicker_card,
                input_card,
                loading_card,
                rangeslider_card,
                slider_card,
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
        return html.Div([html.H3("Tab content 1", className="m-4 p-5 text-center")])
    elif tab == "tab-2":
        return html.Div([html.H3("Tab content 2", className="m-4 p-5 text-center")])

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


from app import app


header = html.Div(
    [
        html.H4(
            ["Here are components available in ", html.Code("dash-core-components"),]
        )
    ],
)


def make_subheading(label, link):
    return html.H4(
        dcc.Link(label, href=DCC_DOCS + link, target="_blank"),
        style={"textDecoration": "underline"},
        className="mb-2",
    )


checklist = html.Div(
    [
        make_subheading("Checklist", "checklist/"),
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
                    labelStyle={"display": "inline-block"},
                ),
            ]
        ),
    ]
)

datepicker_range = html.Div(
    [
        make_subheading("DatePickerRange", "datepickerrange/"),
        html.Div(
            [
                dcc.DatePickerRange(
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2021, 9, 19),
                    initial_visible_month=date(2021, 8, 5),
                    end_date=date(2021, 8, 25),
                ),
            ]
        ),
    ]
)

datepicker_single = html.Div(
    [
        make_subheading("DatePickerSingle", "datepickersingle/"),
        html.Div(
            [
                dcc.DatePickerSingle(
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2021, 9, 19),
                    initial_visible_month=date(2021, 8, 5),
                    date=date(2021, 8, 25),
                ),
            ]
        ),
    ]
)


dropdown = html.Div(
    [
        make_subheading("Dropdown", "dropdown/"),
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
            ]
        ),
    ]
)

dcc_df = px.data.iris()  # iris is a pandas DataFrame
dcc_fig = px.scatter(dcc_df, x="sepal_width", y="sepal_length")
graph = html.Div(
    [
        make_subheading("Graph", "graph/"),
        html.Div([dcc.Graph(id="dcc_graph_v03", figure=dcc_fig,),]),
    ]
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
input = html.Div(
    [
        make_subheading("Input", "input/"),
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
)

loading = html.Div(
    [
        make_subheading("Loading", "loading/"),
        html.H3("Edit text input to see loading state"),
        dcc.Input(id="loading-input-1", value="Input triggers local spinner"),
        dcc.Loading(
            id="loading-1", type="default", children=html.Div(id="loading-output-1")
        ),
        html.Div(
            [
                dcc.Input(id="loading-input-2", value="Input triggers nested spinner"),
                dcc.Loading(
                    id="loading-2",
                    children=[html.Div([html.Div(id="loading-output-2")])],
                    type="circle",
                ),
            ]
        ),
    ],
)

radioitems = html.Div(
    [
        make_subheading("RadioItems", "radioitems/"),
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
                    labelStyle={"display": "inline-block"},
                ),
            ]
        ),
    ]
)


rangeslider = html.Div(
    [
        make_subheading("RangeSlider", "rangeslider/"),
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
)

slider = html.Div(
    [
        make_subheading("Slider", "slider/"),
        html.Div(
            [
                dcc.Slider(
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
            ]
        ),
    ]
)

tabs = html.Div(
    [
        make_subheading("Tabs", "tabs/"),
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


textarea = html.Div(
    [
        make_subheading("Textarea", "textarea/"),
        dcc.Textarea(
            value="Textarea content initialized\nwith multiple lines of text",
        ),
    ]
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
                checklist,
                html.Hr(),
                datepicker_range,
                html.Hr(),
                datepicker_single,
                html.Hr(),
                dropdown,
                html.Hr(),
                graph,
                html.Hr(),
                input,
                html.Hr(),
                loading,
                html.Hr(),
                radioitems,
                html.Hr(),
                rangeslider,
                html.Hr(),
                slider,
                html.Hr(),
                tabs,
                html.Hr(),
                textarea,
                html.Hr(),
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
        return html.Div([html.H3("Tab content 1")])
    elif tab == "tab-2":
        return html.Div([html.H3("Tab content 2")])

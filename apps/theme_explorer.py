import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc

from app import app, header, urls
from apps import text

from .component_gallery import layout as component_layout

import pathlib

# set relative path
PATH = pathlib.Path(__file__).parent
GALLERY_PATH = PATH.joinpath("../gallery").resolve()

# be sure to include a blank line and docstring at start of source file
with open(GALLERY_PATH.joinpath("theme_explorer_app.py")) as f:
    code = f.read()
code = f"```{code}```"


light_themes = [
    "BOOTSTRAP",
    "CERULEAN",
    "COSMO",
    "FLATLY",
    "JOURNAL",
    "LITERA",
    "LUMEN",
    "LUX",
    "MATERIA",
    "MINTY",
    "PULSE",
    "SANDSTONE",
    "SIMPLEX",
    "SKETCHY",
    "SPACELAB",
    "UNITED",
    "YETI",
]
dark_themes = [
    "CYBORG",
    "DARKLY",
    "SLATE",
    "SOLAR",
    "SUPERHERO",
]

plotly_template = [
    "plotly",
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]

continuous_colors = px.colors.named_colorscales()

discrete_colors = {
    "Plotly": px.colors.qualitative.Plotly,
    "D3": px.colors.qualitative.D3,
    "G10": px.colors.qualitative.G10,
    "T10": px.colors.qualitative.T10,
    "Alphabet": px.colors.qualitative.Alphabet,
    "Dark24": px.colors.qualitative.Dark24,
    "Light24": px.colors.qualitative.Light24,
    "Set1": px.colors.qualitative.Set1,
    "Pastel1": px.colors.qualitative.Pastel1,
    "Dark2": px.colors.qualitative.Dark2,
    "Set2": px.colors.qualitative.Set2,
    "Pastel2": px.colors.qualitative.Pastel2,
    "Set3": px.colors.qualitative.Set3,
    "Antique": px.colors.qualitative.Antique,
    "Bold": px.colors.qualitative.Bold,
    "Pastel": px.colors.qualitative.Pastel,
    "Safe": px.colors.qualitative.Safe,
    "Vivid": px.colors.qualitative.Vivid,
    "Prism": px.colors.qualitative.Prism,
}


df = px.data.gapminder()


"""
=====================================================================
"""


def make_dropdown(id, option_list, option_val=0):
    return dcc.Dropdown(
        id=id,
        options=[{"label": str(i), "value": i} for i in option_list],
        value=option_list[option_val],
        clearable=False,
        persistence_type="local",
    )


def make_radio_items(id, option_list, option_val=0):
    return dbc.RadioItems(
        id=id,
        options=[{"label": i, "value": i} for i in option_list],
        #    inputClassName="mr-2 ml-2",
        #  labelStyle={'display': 'inline-block'},
        inline=True,  # for dbc.RadioItems
        value=option_list[option_val],
        persistence_type="local",
        className="mt-2",
    )


def make_checklist(id, option_list):
    return dbc.Checklist(
        id=id,
        options=[{"label": i, "value": i} for i in option_list],
        value=[option_list[0]],
        inline=True,
        #  inputClassName="mr-2 ml-2",
        persistence_type="local",
    )


def make_range_slider(id, slider_list, step=1):
    return dcc.RangeSlider(
        id=id,
        min=slider_list[0],
        max=slider_list[-1],
        step=step,
        marks={int(i): str(i) for i in slider_list},
        value=[slider_list[0], slider_list[-1]],
        persistence_type="local",
    )


"""
=====================================================================
Theme Controls
"""

boostrap_card = html.Div(
    [
        dbc.FormGroup(
            [
                dbc.Label(
                    dbc.Button(
                        "Bootstrap Themes",
                        color="link",
                        href="https://www.bootstrapcdn.com/bootswatch/",
                        target="_blank",
                    )
                ),
                dcc.Dropdown(id="themes"),
                make_radio_items("light_dark", ["Light Themes", "Dark Themes"]),
            ]
        ),
    ],
    className="px-2 mb-2",
    style={"minWidth": 200},
)

graph_template_card = html.Div(
    [
        dbc.FormGroup(
            [
                dbc.Label("Graph Templates", className="mt-2"),
                make_dropdown("template", plotly_template),
            ],
            style={"minWidth": 100},
        )
    ],
    className="px-2 mb-2",
)

discrete_modal = html.Div(
    [
        dbc.Button(
            "Line Colors",
            id="discrete_modal_btn",
            outline=True,
            color="primary",
            size="sm",
            className="mb-1",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(
                    [
                        html.H2(
                            "Click swatch to change line chart colors",
                            className="text-center",
                        ),
                        dbc.Alert(
                            "color selected: Plotly",
                            id="discrete_selected",
                            color="secondary",
                            className="text-center",
                        ),
                        dcc.Markdown(
                            """
                            Learn more about discrete color sequences [here](https://plotly.com/python/discrete-color/)
                            
                        """,
                            className="ml-4",
                        ),
                    ]
                ),
                dbc.ModalBody(
                    [
                        html.Div(
                            "Use these colorscales for data that has distinct groups and a non-meaningful order."
                        ),
                        dcc.Graph(
                            id="discrete_swatch",
                            figure=px.colors.qualitative.swatches(),
                            config={"displayModeBar": False},
                            style={"height": 1000},
                        ),
                    ]
                ),
            ],
            id="discrete_modal",
            scrollable=True,
            centered=False,
            className="p-0 m-0",
        ),
    ]
)


continuous_modal = html.Div(
    [
        dbc.Button(
            "Scatter Colors",
            id="continuous_modal_btn",
            outline=True,
            color="primary",
            size="sm",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(
                    [
                        html.H2(
                            "Click swatch to change scatter plot colors",
                            className="text-center",
                        ),
                        dbc.Alert(
                            "color selected: aggrnyl",
                            id="continuous_selected",
                            color="secondary",
                            className="text-center",
                        ),
                        dcc.Markdown(
                            """
                            Learn more about continuous color sequences [here](https://plotly.com/python/builtin-colorscales/)
                        """,
                            className="ml-4",
                        ),
                    ]
                ),
                dbc.ModalBody(
                    [
                        html.Div(
                            "Use sequential colorscales for data that smoothly changes value and has meaningful order."
                        ),
                        dcc.Graph(
                            id="seq_swatch",
                            figure=px.colors.sequential.swatches(),
                            config={"displayModeBar": False},
                            style={"height": 3000},
                        ),
                        html.Hr(),
                        html.Div(
                            "Use divergent colorscales for data that smoothly changes around a centerpoint (such as zero)."
                        ),
                        dcc.Graph(
                            id="div_swatch",
                            figure=px.colors.diverging.swatches(),
                            config={"displayModeBar": False},
                        ),
                        html.Hr(),
                        html.Div(
                            "Cyclical color scales are appropriate for continuous data that has a natural cyclical "
                            "structure, such as temporal data (hour of day, day of week, day of year, seasons) or "
                            "complex numbers or other phase or angular data."
                        ),
                        dcc.Graph(
                            id="cyc_swatch",
                            figure=px.colors.cyclical.swatches(),
                            config={"displayModeBar": False},
                        ),
                    ]
                ),
            ],
            id="continuous_modal",
            scrollable=True,
            className=("p-0 m-0"),
        ),
    ]
)


graph_continuous_color_card = html.Div(
    [
        dbc.FormGroup(
            [
                dbc.Label("Graph Colors", className="mt-2"),
                discrete_modal,
                continuous_modal,
            ]
        )
    ],
    className="px-2 mb-2",
    style={"minWidth": 200},
)

background_color_card = html.Div(
    [
        dbc.FormGroup(
            [
                dbc.Label("Background Color", className="mt-2"),
                dbc.Input(
                    type="color",
                    id="bg_color",
                    value="#e2e2e4",
                    style={"width": 75, "height": 50},
                ),
                make_radio_items("bg_default", ["Use Default", "Use Colorpicker"]),
            ]
        ),
    ],
    className="px-2 mb-2",
    style={"minWidth": 200},
)


theme_controls = dbc.Card(
    [
        dbc.CardHeader("App Design Selections"),
        dbc.CardBody(
            [
                boostrap_card,
                graph_template_card,
                graph_continuous_color_card,
                background_color_card,
            ],
        ),
    ],
    style={"minWidth": 250},
)

source_code_modal = html.Div(
    [
        html.Div(
            [
                html.Div("Sample App"),
                dbc.Button(
                    "Source Code",
                    id="code_modal_btn",
                    outline=True,
                    color="primary",
                    size="sm",
                ),
            ],
            className="ml-4",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader(
                    [
                        html.H3(
                            "Source code for the Sample Dash App",
                            className="text-center",
                        ),
                        html.H5("See this app and more in the App Gallery!"),
                    ]
                ),
                dbc.ModalBody([dcc.Markdown(code)]),
            ],
            id="code_modal",
            scrollable=True,
            size="xl",
        ),
    ],
    className="my-2",
)


css_modal = html.Div(
    [
        html.Div(
            [
                html.Div("Custom CSS"),
                dbc.Button(
                    "Learn More",
                    id="css_modal_btn",
                    outline=True,
                    color="primary",
                    size="sm",
                ),
            ],
            className="ml-4",
        ),
        dbc.Modal(
            [
                dbc.ModalBody([dcc.Markdown(text.css_text)]),
            ],
            id="css_modal",
            scrollable=True,
            size="xl",
        ),
    ],
    className="my-2",
)



"""
===============================================================================
Sample Apps 
"""

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ]
)

sample_app_controls = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Select indicator (y-axis)"),
                            make_dropdown("indicator", ["gdpPercap", "lifeExp", "pop"]),
                        ]
                    )
                ),
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Select continents"),
                            make_checklist("continents", df.continent.unique()),
                        ]
                    )
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Select years"),
                make_range_slider("slider_years", df.year.unique(), 5),
                html.Div("Bootstrap theme colors"),
                buttons,
            ]
        ),
    ],
    className="mr-4 ml-4 px-2",
)

sample_app = dbc.Card(
    [
        html.H2("Sample Dash App", className="bg-primary text-white p-2"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(
                            id="line_chart_title",
                            className="text-center mb-0 d-inline-block",
                        ),
                        dcc.Graph(id="line_chart", config={"displayModeBar": False},),
                    ],
                    lg=6,
                ),
                dbc.Col(
                    [
                        dcc.Markdown(
                            id="scatter_chart_title",
                            className="text-center  d-inline-block",
                        ),
                        dcc.Graph(
                            id="scatter_chart", config={"displayModeBar": False},
                        ),
                    ],
                    lg=6,
                ),
            ],
            className="mt-0, mb-2 mx-2",
        ),
        sample_app_controls,
    ],
    className="mx-1 shadow p-1 pb-4",
    id="sample_app_container",
)


"""
===============================================================================
Layout
"""
layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col([theme_controls, source_code_modal, css_modal], md=3),
                dbc.Col(sample_app, md=9, sm=12,),
            ],
        ),
        component_layout,
        html.Div(id="blank_output"),
        dcc.Store(id="store"),
    ],
    fluid=True,
)


@app.callback(
    Output("line_chart", "figure"),
    Output("scatter_chart", "figure"),
    Output("line_chart_title", "children"),
    Output("scatter_chart_title", "children"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("slider_years", "value"),
    Input("template", "value"),
    Input("discrete_selected", "children"),
    Input("continuous_selected", "children"),
)
def update_line_chart(
    indicator, continents, years, template, color_discrete, color_continuous
):

    color_discrete = color_discrete.split(": ")[1].strip()
    color_continuous = color_continuous.split(": ")[1].strip()

    if continents == [] or indicator is None:
        return {}, {}, "", ""

    dff = df[df.year.between(years[0], years[1])]
    dff = dff[dff.continent.isin(continents)]

    title = """template= {}  \ncolor_discrete_sequence=px.colors.qualitative.{}""".format(
        template, color_discrete
    )
    fig = px.line(
        dff,
        x="year",
        y=indicator,
        color="country",
        template=template,
        color_discrete_sequence=discrete_colors[color_discrete],
        height=350,
    )
    fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))
    dff = df[df.year == years[1]]
    title2 = """template= {}  \n  color_continuous_scale= {}""".format(
        template, color_continuous
    )
    fig2 = px.scatter(
        dff[dff.continent.isin(continents)],
        x="lifeExp",
        y=indicator,
        color="lifeExp",
        template=template,
        color_continuous_scale=color_continuous,
        hover_data=["country", "year"],
        height=350,
    )
    fig2.update_layout(margin=dict(l=75, r=20, t=10, b=20))
    return fig, fig2, title, title2


@app.callback(
    Output("themes", "options"),
    Output("themes", "value"),
    Input("light_dark", "value"),
)
def update(theme):

    if theme == "Light Themes":
        options = [{"label": str(i), "value": urls[i]} for i in light_themes]
        value = urls["BOOTSTRAP"]
    else:
        options = [{"label": str(i), "value": urls[i]} for i in dark_themes]
        value = urls["CYBORG"]
    return options, value


@app.callback(
    Output("sample_app_container", "style"),
    Output("bg_default", "value"),
    Input("bg_color", "value"),
    Input("bg_default", "value"),
)
def update_app_bg_color(color, radio):

    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if input_id == "bg_color":
        radio = "Use Colorpicker"

    else:
        color = "" if radio == "Use Default" or color is None else color
    return {"backgroundColor": color}, radio


#  ------------ color scale modal selection ------------------


@app.callback(
    Output("discrete_selected", "children"), Input("discrete_swatch", "clickData"),
)
def sel_swatch(clicked):
    return (
        dash.no_update
        if clicked is None
        else f"color selected:   {clicked['points'][0]['y']}"
    )


@app.callback(
    Output("continuous_selected", "children"),
    Input("seq_swatch", "clickData"),
    Input("div_swatch", "clickData"),
    Input("cyc_swatch", "clickData"),
)
def sel_swatch(seq, div, cyc):
    if seq is None and div is None and cyc is None:
        return dash.no_update
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if input_id == "seq_swatch":
        return f"color selected:   {seq['points'][0]['y']}"
    if input_id == "div_swatch":
        return f"color selected:   {div['points'][0]['y']}"
    if input_id == "cyc_swatch":
        return f"color selected:   {cyc['points'][0]['y']}"


# --------------- modals open close -------------------------------------------------------------
@app.callback(
    Output("discrete_modal", "is_open"),
    [Input("discrete_modal_btn", "n_clicks")],
    [State("discrete_modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("continuous_modal", "is_open"),
    [Input("continuous_modal_btn", "n_clicks")],
    [State("continuous_modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("code_modal", "is_open"),
    [Input("code_modal_btn", "n_clicks")],
    [State("code_modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("css_modal", "is_open"),
    [Input("css_modal_btn", "n_clicks")],
    [State("css_modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


# ----------------------------------------------------


# Using 2 stylesheets with the delay reduces the annoying flicker when the theme changes
app.clientside_callback(
    """
    function(url) {
        // Select the FIRST stylesheet only.
        var stylesheets = document.querySelectorAll('link[rel=stylesheet][href^="https://stackpath"]')
        // Update the url of the main stylesheet.
        stylesheets[stylesheets.length - 1].href = url
        // Delay update of the url of the buffer stylesheet.
        setTimeout(function() {stylesheets[0].href = url;}, 100);
    }
    """,
    Output("blank_output", "children"),
    Input("themes", "value"),
)

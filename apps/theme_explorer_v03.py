import dash
import dash_core_components as dcc
import dash_html_components as html


from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

from app import app, header
from .tutorial import tutorial
from .component_gallery import layout as component_layout


boostrap_light_themes = [
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
boostrap_dark_themes = [
    "CYBORG",
    "DARKLY",
    "SLATE",
    "SOLAR",
    "SUPERHERO",
]

colors_diverging = [
    "rdbu",
    "armyrose",
    "brbg",
    "earth",
    "fall",
    "geyser",
    "prgn",
    "piyg",
    "picnic",
    "portland",
    "puor",
    "rdgy",
    "rdylbu",
    "rdylgn",
    "spectral",
    "tealrose",
    "temps",
    "tropic",
    "balance",
    "curl",
    "delta",
]

colors_squential = [
    "aggrnyl",
    "agsunset",
    "blackbody",
    "bluered",
    "blues",
    "blugrn",
    "bluyl",
    "brwnyl",
    "bugn",
    "bupu",
    "burg",
    "burgyl",
    "cividis",
    "darkmint",
    "electric",
    "emrld",
    "gnbu",
    "greens",
    "greys",
    "hot",
    "inferno",
    "jet",
    "magenta",
    "magma",
    "mint",
    "orrd",
    "oranges",
    "oryel",
    "peach",
    "pinkyl",
    "plasma",
    "plotly3",
    "pubu",
    "pubugn",
    "purd",
    "purp",
    "purples",
    "purpor",
    "rainbow",
    "rdbu",
    "rdpu",
    "redor",
    "reds",
    "sunset",
    "sunsetdark",
    "teal",
    "tealgrn",
    "viridis",
    "ylgn",
    "ylgnbu",
    "ylorbr",
    "ylorrd",
    "algae",
    "amp",
    "deep",
    "dense",
    "gray",
    "haline",
    "ice",
    "matter",
    "solar",
    "speed",
    "tempo",
    "thermal",
    "turbid",
]

colors_cyclical = ["edge", "hsv", "icefire", "phase", "twilight", "mrybm", "mygbm"]


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

boostrap_card = dbc.Card(
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
                make_dropdown("themes_v03", boostrap_light_themes),
                make_radio_items("light_dark_v03", ["Light Themes", "Dark Themes"]),
            ]
        ),
    ],
    className="pr-2 pl-2",
    style={"minWidth": 200},
)

graph_template_card = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label(
                    dbc.Button(
                        "Graph Templates",
                        color="link",
                        href="https://plotly.com/python/templates/",
                        target="_blank",
                    )
                ),
                make_dropdown("template_v03", plotly_template),
            ]
        )
    ],
    className="pr-2 pl-2",
    style={"minWidth": 200},
)

graph_color_sequence_card = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label(
                    dbc.Button(
                        "Discrete Colors",
                        color="link",
                        href="https://plotly.com/python/discrete-color/#color-sequences-in-plotly-express",
                        target="_blank",
                    )
                ),
                make_dropdown("color_sequence_v03", list(discrete_colors)),
            ]
        ),
    ],
    className="pr-2 pl-2",
    style={"minWidth": 200},
)

graph_continuous_color_card = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label(
                    dbc.Button(
                        "Continuous Colorscales",
                        color="link",
                        href="https://plotly.com/python/builtin-colorscales/",
                        target="_blank",
                    )
                ),
                make_dropdown("color_scale_v03", list(continuous_colors)),
                make_radio_items(
                    "color_scale_radio_v03", ["Sequential", "Diverging", "Cyclical"]
                ),
            ]
        ),
    ],
    className="pr-2 pl-2",
    style={"minWidth": 200},
)

background_color_card = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("App Background Color", className="mt-2"),
                dbc.Input(
                    type="color",
                    id="bg_color_v03",
                    value="#DFDEE3",
                    style={"width": 100},
                ),
                make_radio_items("bg_default_v03", ["Use Default", "Use Colorpicker"]),
            ]
        ),
    ],
    className="pr-2 pl-2",
    style={"minWidth": 200},
)


theme_controls = dbc.CardGroup(
    [
        boostrap_card,
        graph_template_card,
        graph_color_sequence_card,
        graph_continuous_color_card,
        background_color_card,
    ],
    className=" p-2",
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
                            make_dropdown(
                                "indicator_v03", ["gdpPercap", "lifeExp", "pop"]
                            ),
                        ]
                    )
                ),
                dbc.Col(
                    dbc.FormGroup(
                        [
                            dbc.Label("Select continents"),
                            make_checklist("continents_v03", df.continent.unique()),
                        ]
                    )
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Select years"),
                make_range_slider("slider_years_v03", df.year.unique(), 5),
                html.Div(id="theme_colors_v03"),
                buttons,
            ]
        ),
    ],
    className="mr-4 ml-4 px-2",
)

sample_app_1 = dbc.Card(
    [
        html.H2("Sample Dash App", className="bg-primary text-white m-1 p-2"),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(id="line_chart_v03", config={"displayModeBar": False}),
                ),
                dbc.Col(
                    dcc.Graph(id="scatter_chart_v03", config={"displayModeBar": False}),
                ),
            ],
            className="m-2",
        ),
        sample_app_controls,
    ],
    className="mx-4 shadow-lg p-2",
    id="layout_container_v03",
)


"""
===============================================================================
Layout
"""
layout = dbc.Container(
    [
        header,
        theme_controls,
        sample_app_1,
        component_layout,
        dcc.Markdown(tutorial, className="m-4 p-4"),
        html.Div(id="blank_output_v03"),
    ],
    fluid=True,
)


@app.callback(
    Output("line_chart_v03", "figure"),
    Output("scatter_chart_v03", "figure"),
    Input("indicator_v03", "value"),
    Input("continents_v03", "value"),
    Input("slider_years_v03", "value"),
    Input("template_v03", "value"),
    Input("color_sequence_v03", "value"),
    Input("color_scale_v03", "value"),
)
def update_line_chart(
    indicator, continents, years, template, color_sequence, color_scale
):

    if continents == [] or indicator is None:
        return {}, {}

    dff = df[df.year.between(years[0], years[1])]
    dff = dff[dff.continent.isin(continents)]
    fig = px.line(
        dff,
        x="year",
        y=indicator,
        color="country",
        template=template,
        color_discrete_sequence=discrete_colors[color_sequence],
        title=f'Graph Template= "{template}"  Discrete Colors ="{color_sequence}"',
        height=350,
    )
    fig.update_layout(margin=dict(l=75, r=20, t=50, b=20))
    dff = df[df.year == years[1]]
    fig2 = px.scatter(
        dff[dff.continent.isin(continents)],
        x="lifeExp",
        y=indicator,
        color="lifeExp",
        template=template,
        color_continuous_scale=color_scale,
        hover_data=["country", "year"],
        title=f'Graph Template= "{template}"  Continuous Colorscale= "{color_scale}"',
        height=350,
    )
    fig2.update_layout(margin=dict(l=75, r=20, t=50, b=20))
    return fig, fig2


@app.callback(
    Output("themes_v03", "options"),
    Output("themes_v03", "value"),
    Input("light_dark_v03", "value"),
)
def update(theme):

    if theme == "Light Themes":
        options = [{"label": str(i), "value": i} for i in boostrap_light_themes]
        value = boostrap_light_themes[0]
    else:
        options = [{"label": str(i), "value": i} for i in boostrap_dark_themes]
        value = boostrap_dark_themes[0]
    return options, value


@app.callback(
    Output("color_scale_v03", "options"), Input("color_scale_radio_v03", "value")
)
def update(colorscale):
    if colorscale == "Sequential":
        options = [{"label": str(i), "value": i} for i in colors_squential]
    elif colorscale == "Diverging":
        options = [{"label": str(i), "value": i} for i in colors_diverging]
    else:
        options = [{"label": str(i), "value": i} for i in colors_cyclical]
    return options


@app.callback(
    Output("layout_container_v03", "style"),
    Output("bg_default_v03", "value"),
    Input("bg_color_v03", "value"),
    Input("bg_default_v03", "value"),
)
def update_app_bg_color(color, radio):

    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if input_id == "bg_color_v03":
        radio = "Use Colorpicker"

    else:
        color = "" if radio == "Use Default" or color is None else color
    return {"backgroundColor": color}, radio


@app.callback(
    Output("theme_colors_v03", "children"), Input("themes_v03", "value"),
)
def update(theme):
    theme = "default" if theme == "BOOTSTRAP" else theme
    link = f"https://bootswatch.com/{theme.lower()}/"
    return html.Div(
        ["Boostrap Theme colors: ", dcc.Link(theme, href=link, target="_blank")]
    )


app.clientside_callback(
    """
    function(theme) {
        // remove all stylesheets except for CSS files in assets folder
        var elements = document.querySelectorAll('link[rel=stylesheet][href^="https"]');
        for(var i=0;i<elements.length;i++){
          elements[i].parentNode.removeChild(elements[i]);
        }

        // add new stylesheet from dropdown
        var name = theme.toLowerCase()
        var link = document.createElement("link")
        link.rel = "stylesheet"
        link.type = "text/css"
        if (name === 'bootstrap') {
            link.href = 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css'
          } else {
            link.href = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/" + name + "/bootstrap.min.css"
        }
        document.getElementsByTagName("head")[0].appendChild(link);
    }
    """,
    Output("blank_output_v03", "children"),
    Input("themes_v03", "value"),
)

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_daq as daq

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

boostrap_themes = [
    "BOOTSTRAP",
    "CERULEAN",
    "COSMO",
    "CYBORG",
    "DARKLY",
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
    "SLATE",
    "SOLAR",
    "SPACELAB",
    "SUPERHERO",
    "UNITED",
    "YETI",
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
}


df = px.data.gapminder()


def make_dropdown(id, option_list, option_val=0):
    return dcc.Dropdown(
        id=id,
        options=[{"label": str(i), "value": i} for i in option_list],
        value=option_list[option_val],
        clearable=False,
        persistence_type="memory",
    )


def make_radio_items(id, option_list, option_val=0):
    return dcc.RadioItems(
        id=id,
        options=[{"label": i, "value": i} for i in option_list],
        inputClassName="mr-2 ml-2",
        value=option_list[option_val],
        persistence_type="session",
    )


def make_checklist(id, option_list):
    return dcc.Checklist(
        id=id,
        options=[{"label": i, "value": i} for i in option_list],
        value=[option_list[0]],
        labelStyle={"display": "inline-block"},
        inputClassName="mr-2 ml-2",
        persistence_type="session",
    )


def make_range_slider(id, slider_list, step=1):
    return dcc.RangeSlider(
        id=id,
        min=slider_list[0],
        max=slider_list[-1],
        step=step,
        marks={int(i): str(i) for i in slider_list},
        value=[slider_list[0], slider_list[-1]],
        persistence_type="session",
    )


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

alerts1 = html.Div(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
    ],
)
alerts2 = html.Div(
    [
        dbc.Alert("This is a danger alert. Scary!", color="danger"),
        dbc.Alert("This is an info alert. Good to know!", color="info"),
        dbc.Alert("This is a light alert", color="light"),
        dbc.Alert("This is a dark alert", color="dark"),
    ],
)

graph_tabs = dbc.Card(
    dbc.Tabs(
        [
            dbc.Tab(dcc.Graph(id="line_chart"), label="Color Sequences - Line Chart"),
            dbc.Tab(
                dcc.Graph(id="scatter_chart"),
                label="Continuous colorscales - Scatter Chart ",
            ),
        ],
    ),
    className="m-2 p-2 mb-2",
)

theme_controls = dbc.Card(
    [
        html.Div(
            "See how different Bootstrap themes, Plotly templates and colors "
            "look in the app.  Make selections here:",
            className="mt-4",
        ),
        html.H1("☟"),
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
                make_dropdown("themes", boostrap_themes),
            ]
        ),
        dbc.FormGroup(
            [
                html.Hr(),
                dbc.Label(
                    dbc.Button(
                        "Graph Templates",
                        color="link",
                        href="https://plotly.com/python/templates/",
                        target="_blank",
                    )
                ),
                make_dropdown("template", plotly_template),
            ]
        ),
        dbc.FormGroup(
            [
                html.Hr(),
                dbc.Label(
                    dbc.Button(
                        "Graph Color Sequences",
                        color="link",
                        href="https://plotly.com/python/discrete-color/#color-sequences-in-plotly-express",
                        target="_blank",
                    )
                ),
                make_dropdown("color_sequence", list(discrete_colors)),
            ]
        ),
        dbc.FormGroup(
            [
                html.Hr(),
                dbc.Label(
                    dbc.Button(
                        "Graph Continuous Colorscales",
                        color="link",
                        href="https://plotly.com/python/builtin-colorscales/",
                        target="_blank",
                    )
                ),
                make_dropdown("color_scale", list(continuous_colors)),
            ]
        ),
        dbc.FormGroup(
            [
                html.Hr(),
                dbc.Label("App Background Color"),
                make_radio_items("bg_default", ["Use default", "Use colorpicker"]),
                html.Div(
                    daq.ColorPicker(id="bg_color", size=250), style={"width": 250},
                ),
            ]
        ),
        html.Div(id="blank_output"),
    ],
    className="m-2 p-2 mb-2",
)


"""
===============================================================================
Markdown Text
"""


with open("sample_app_1.py") as f:
    code = f.read()
example_app_code = f"```{code}```"


app_notes = dcc.Markdown(
    """

These two images are the same app!  Only 5 lines are changed to set a different theme.




|Light Theme app     | Dark Theme app |
| ----------- | ----------- |
| ![minty](https://user-images.githubusercontent.com/72614349/108880577-aa390900-75bf-11eb-8cb2-d246b342f4b5.png#thumbnail) | ![dark](https://user-images.githubusercontent.com/72614349/108880544-a1483780-75bf-11eb-913d-09c10adbe537.png#thumbnail) |
| __Boostrap Theme:__ MINTY | DARKLY
| __Graph Template:__ simple_white | plotly_dark|
| __Graph Color Sequences:__ Pastel | Dark24|
| __Graph Continuous Colorscales:__ darkmint | ice|
| __App Background Color:__ #F3F6F3 | ""|

------

The light Bootstrap themes are the easiest themes to add to your Dash app.  The Dash components have a light background color and that works well with the Bootswatch light themes.

A dark theme will set the text color to white or some other light color making the text  hard  to read in some Dash components. Here are some way to change the colors:
-  Dash Core Components:  Try using the `className` or `style` parameter of the component or use the inspector in the browser to see how the colors are set and override it with custom CSS in the assets folder. 
See more information [here](https://dash.plotly.com/external-resources).   See the css we used here [ github link](https://github.com/AnnMarieW/HelloDash/blob/main/assets/mycss.css) 
-  Dash DataTables:  See how to set a dark theme [here](https://dash.plotly.com/datatable/style) in the Dash documentation
-  Dash DAQ components: Use the `theme` parameter:   `theme= {'dark': True}`
-  Figures: Use the [Graph template](https://plotly.com/python/templates/)  `plotly_dark`

## Source code
The code for the sample app is also available in the [GitHub](https://github.com/AnnMarieW/HelloDash).


"""
    + example_app_code,
    style={"backgroundColor": "white", "color": "black", "padding": 20},
)


"""
===============================================================================
Controls
"""
controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Select indicator (y-axis)"),
                make_dropdown("indicator", ["gdpPercap", "lifeExp", "pop"]),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Select continents"),
                make_checklist("continents", df.continent.unique()),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Select years"),
                make_range_slider("slider_years", df.year.unique(), 5),
            ]
        ),
    ],
    className="m-2 p-2",
)

sample_controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Sample Buttons and alerts for selected Bootswatch theme"),
                buttons,
            ]
        ),
        dbc.Row([dbc.Col(alerts1), dbc.Col(alerts2)]),
    ],
    className="m-2 p-2 mt-4",
)
"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([theme_controls,], md=3, style={"minWidth": 325}),
                dbc.Col(
                    [
                        html.H1(
                            "App Theme Explorer", className="bg-primary text-white",
                        ),
                        html.Hr(),
                        graph_tabs,
                        controls,
                        sample_controls,
                    ]
                ),
            ],
        ),
        html.Hr(),
        html.H1(
            "Sample Apps and Source Code",
            style={"backgroundColor": "white", "color": "black", "padding": 20},
        ),
        dbc.Row(dbc.Col(app_notes)),
    ],
    id="layout_container",
    fluid=True,
)


@app.callback(
    Output("line_chart", "figure"),
    Output("scatter_chart", "figure"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("slider_years", "value"),
    Input("template", "value"),
    Input("color_sequence", "value"),
    Input("color_scale", "value"),
)
def update_line_chart(
    indicator, continents, years, template, color_sequence, color_scale
):
    if continents == [] or indicator is None:
        return {}, {}

    dff = df[df.year.between(years[0], years[1])]
    fig = px.line(
        dff[dff.continent.isin(continents)],
        x="year",
        y=indicator,
        color="country",
        template=template,
        color_discrete_sequence=discrete_colors[color_sequence],
        title=f'Graph with "{template}" template and "{color_sequence}" color sequence',
    )
    dff = df[df.year == years[1]]
    fig2 = px.scatter(
        dff[dff.continent.isin(continents)],
        x="lifeExp",
        y=indicator,
        color="lifeExp",
        template=template,
        color_continuous_scale=color_scale,
        hover_data=["country", "year"],
        title=f'Graph with "{template}" template and "{color_scale}" color scale',
    )
    return fig, fig2


@app.callback(
    Output("layout_container", "style"),
    Output("bg_default", "value"),
    Input("bg_color", "value"),
    Input("bg_default", "value"),
)
def update_app_bg_color(color, radio):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if input_id == "bg_color":
        radio = "Use colorpicker"
        color = color["hex"]
    else:
        color = "" if radio == "Use default" or color is None else color["hex"]
    return {"backgroundColor": color}, radio


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
        document.getElementsByTagName("head")[0].appendChild(link)
    }
    """,
    Output("blank_output", "children"),
    Input("themes", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True)

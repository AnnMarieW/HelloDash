"""
This is a collection of shared components, utilities and data

"""


import pathlib


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash_bootstrap_templates import load_figure_template


# set relative path
PATH = pathlib.Path(__file__).parent
GALLERY_PATH = PATH.joinpath("./gallery").resolve()
DATA_PATH = PATH.joinpath("./data").resolve()


def get_code_file(filename):
    """
    :param filename: (str) file name of python file in the gallery directory
    :return: a string to display the code with highlighting in dcc.Markdown(code)

    Note: be sure to include a blank line and docstring at start of source file so highlighting
      works correctly
    """
    with open(GALLERY_PATH.joinpath(filename)) as f:
        code = f.read()
    return f"```{code}```"


header = dbc.Jumbotron(
    [
        html.H1("Dash Bootstrap Theme Explorer", className="display-3"),
        html.P(
            "The easy way to see Bootstrap themes and Plotly  graph templates and colors in a Dash app.",
            className="lead",
        ),
        html.P("Your app design starts here!", className=" font-italic",),
        html.Hr(className="my-2"),
        html.Div(
            [
                dbc.Button(
                    "Theme Explorer",
                    color="primary",
                    outline=True,
                    href="/theme_explorer",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "Dash Bootstrap Templates",
                    color="primary",
                    outline=True,
                    href="/dash_bootstrap_templates",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "App Gallery",
                    id="app_gallery",
                    color="primary",
                    outline=True,
                    href="/app_gallery",
                    className="mr-2",
                    size="sm",
                ),
                dbc.Button(
                    "Cheatsheet",
                    id="cheatsheet",
                    color="primary",
                    outline=True,
                    href="/cheatsheet",
                    className="mr-2",
                    size="sm",
                ),
            ],
            className="mt-2",
        ),
        html.Div(id="blank_output", className="mb-4"),
    ]
)


dash_labs_templates = [
    "DbcSidebar_4graphs",
    "FlatDiv",
    "HtmlCard",
    "DbcCard",
    "DbcRow",
    "DbcSidebar",
    "DbcSidebarTabs",
]

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

# the template themes are lower case to be consistent with the plotly naming convention
dbc_lower_case = [t.lower() for t in light_themes + dark_themes]
load_figure_template(dbc_lower_case)


dbc_themes_url = {
    "BOOTSTRAP": dbc.themes.BOOTSTRAP,
    "CERULEAN": dbc.themes.CERULEAN,
    "COSMO": dbc.themes.COSMO,
    "FLATLY": dbc.themes.FLATLY,
    "JOURNAL": dbc.themes.JOURNAL,
    "LITERA": dbc.themes.LITERA,
    "LUMEN": dbc.themes.LUMEN,
    "LUX": dbc.themes.LUX,
    "MATERIA": dbc.themes.MATERIA,
    "MINTY": dbc.themes.MINTY,
    "PULSE": dbc.themes.PULSE,
    "SANDSTONE": dbc.themes.SANDSTONE,
    "SIMPLEX": dbc.themes.SIMPLEX,
    "SKETCHY": dbc.themes.SKETCHY,
    "SPACELAB": dbc.themes.SPACELAB,
    "UNITED": dbc.themes.UNITED,
    "YETI": dbc.themes.YETI,
    "CYBORG": dbc.themes.CYBORG,
    "DARKLY": dbc.themes.DARKLY,
    "SLATE": dbc.themes.SLATE,
    "SOLAR": dbc.themes.SOLAR,
    "SUPERHERO": dbc.themes.SUPERHERO,
}

url_dbc_themes = dict(map(reversed, dbc_themes_url.items()))


plotly_template = [
    "bootstrap",
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


def get_copy_code_div(code, id="copy_id", width=800, height=600):
    """
    Args:
        code: The text to show in dcc.Markdown
        id: The id for the copy to clipboard
        width: The width of the div in pixels (integer)
        height: The height of the div in pixels

    Returns: a scrolling div with a copy to clipboard icon in top right corner
    """
    return html.Div(
        [
            dcc.Markdown(
                code,
                id=id,
                style={
                    "width": width,
                    "height": height,
                    "overflow": "auto",
                    "backgroundColor": "white",
                },
                className="border p-2",
            ),
            dcc.Clipboard(
                target_id=id,
                style={"position": "absolute", "top": 0, "right": 20, "fontSize": 20,},
            ),
        ],
        style={"width": width, "height": height, "position": "relative",},
    )

"""
This is a collection of shared components, utilites and data

"""


import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px


header = dbc.Jumbotron(
    [
        html.H1("Dash Bootstrap Theme Explorer", className="display-3"),
        html.P(
            "The easy way to see Boostrap themes and Plotly  graph templates and colors in a Dash app.",
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
                # dbc.Button(
                #     "Dash Bootstrap Components",
                #     color="primary",
                #     outline=True,
                #     target="_blank",
                #     className="mr-2",
                #     href="https://dash-bootstrap-components.opensource.faculty.ai/",
                #     size="sm",
                # ),
                # dbc.Button(
                #     "Dash Documentation",
                #     color="primary",
                #     outline=True,
                #     target="_blank",
                #     href="https://dash.plotly.com/",
                #     size="sm",
                # ),
            ],
            className="mt-2",
        ),
    ]
)


dash_labs_templates = [
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


# this is now in assets folder as a class name
codebox = {
    "backgroundColor": "transparent",
    "borderStyle": "groove",
    "borderRadius": 15,
    "maxWidth": 900,
    "marginTop": 0,
    "marginBottom": 20,
}

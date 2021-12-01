from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
import util

df = px.data.gapminder()


intro_text = dcc.Markdown(
    """
Below you will see 8 of the 26 Bootstrap-themed Plotly figure templates. available in the [`dash-bootstrap-templates`](https://github.com/AnnMarieW/dash-bootstrap-templates) library.

Learn more about Plotly figure templates [here](https://plotly.com/python/templates/)  

See more information about the [`dash-bootstrap-template`](https://github.com/AnnMarieW/dash-bootstrap-templates) library, including theme switch components and a stylesheet to
 appy Bootstrap themes to Dash Core Components and the DataTable [here](https://github.com/AnnMarieW/dash-bootstrap-templates)

    """
)
intro_text_md = dbc.Alert(intro_text, color="primary", className="p-2")

four_figures_text = dcc.Markdown(
    """
#### Here is an example of an app using the "cyborg" figure template in a Dash app with a Cyborg theme.      
    """,
    className="mt-4 p-4",
)


def make_figure_sampler():
    templates = [
        "bootstrap",
        "minty",
        "pulse",
        "flatly",
        "quartz",
        "cyborg",
        "darkly",
        "vapor",
    ]
    load_figure_template(templates)
    figures = [
        px.scatter(
            df.query("year==2007"),
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            log_x=True,
            size_max=60,
            template=template,
            title="Gapminder 2007: '%s' theme" % template,
        )
        for template in templates
    ]
    return html.Div([dcc.Graph(figure=fig, className="m-4") for fig in figures])


figure_sampler_code = util.get_code_file("demo_figure_template_sampler.py")
figure_sampler_code_card = util.make_code_card(
    figure_sampler_code, id="figure_sampler_code", height=450
)


four_figures_code = util.get_code_file("demo_4_graphs.py")
four_figures_code_card = util.make_code_card(
    four_figures_code, id="four_figures_code", height=450
)
four_figures_image = dcc.Markdown(
    """
![image](https://user-images.githubusercontent.com/72614349/143795917-97677fc2-7c35-439b-a6d5-0e3ce122422d.png)
"""
)

available_themes = """
## Available Themes
```
templates = [
    "bootstrap",
    "cerulean",
    "cosmo",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "pulse",
    "sandstone",
    "simplex",
    "sketchy",
    "spacelab",
    "united",
    "yeti",
    "cyborg",
    "darkly",
    "slate",
    "solar",
    "superhero",
    "morph",
    "quartz",
    "vapor"
    "zephyr"
]
```    
    """
available_themes_code_card = util.make_code_card(
    available_themes, id="available_themes_code"
)

layout = html.Div(
    [
        util.make_header("Bootstrap-Themed Plotly Figure Templates", spacing=""),
        intro_text_md,
        figure_sampler_code_card,
        make_figure_sampler(),
        four_figures_text,
        four_figures_code_card,
        four_figures_image,
        available_themes_code_card,
    ],
    className="dbc pb-4",
)


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
import util


heading = html.H2(
    "Bootstrap Themed Plotly Figure Templates",
    className="text-white bg-primary p-2 mt-4",
)

intro_text = dcc.Markdown(
    """
Here are 8 of the 26 **Bootstrap themed Plotly figure templates**. available in the `dash-bootstrap-templates` library.
See how they look with your selected bootstrap theme in the Theme Explorer!

Learn more about Plotly figure templates [here](https://plotly.com/python/templates/)  

See more examples in the `dash-bootstrap-template` library [here](https://github.com/AnnMarieW/dash-bootstrap-templates)

```
pip install dash-bootstrap-templates
```

    """
)

def make_figure_sampler():
    df = px.data.gapminder()
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

    return html.Div([dcc.Graph(figure=fig, className="m-4", style={"maxWidth": 800}) for fig in figures])


figure_sampler_code = util.get_code_file("demo_figure_template_sampler.py")
figure_sampler_code_card = util.make_code_card(figure_sampler_code, id="figure_sampler_code", height=450, width=800)



layout = dbc.Container(
    [
        heading,
        intro_text,
        figure_sampler_code_card,
        make_figure_sampler(),
    ],
    fluid=True,
    className="dbc"
)
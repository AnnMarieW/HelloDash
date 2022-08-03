from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_app_first
from lib.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Adding Themes/Figure Templates",
    name="Figure templates",
)

notes_first = """
--------
## Plotly Figure Templates with a Bootstrap theme

Example of the "minty" theme applied to the figure. See all 26 themes below

"""


layout = html.Div(
    [
        example_app("adding_theme_figure_template", notes_first=notes_first),
        html.Hr(),
        html.H2("All Themes"),
        example_app(
            "all_figure_templates", show_code=False, make_layout=make_app_first
        ),
    ],
    className="dbc",
)

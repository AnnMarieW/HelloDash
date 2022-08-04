from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_app_first, make_tabs
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

"""


layout = html.Div(
    [
        html.Div(
            example_app(
                "all_figure_templates",
                notes_first=notes_first,
                show_code=False,
                make_layout=make_app_first,
            ),
            className="p-4",
        ),
        example_app(
            "adding_theme_figure_template",
            notes_first="### Example of the 'minty' theme applied to the figure.",
        ),
        html.Div(
            example_app("figure_templates_4graphs", make_layout=make_tabs),
            className="dbc",
        ),
    ],
    className="dbc",
)

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_tabs
from lib.utils import app_description

dash.register_page(
    __name__,
    path="/",
    order=1,
    name="Sample App",
    description=app_description,
    title="Theme Explorer",
    redirect_from=["/theme_explorer"],
)

notes = """
This sample app demonstrates Bootstrap themes applied to Dash components and Plotly figures.  It uses the stylesheet, figure
templates and theme change component from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.


Try changing the theme and you'll see:
  - The text in the `dcc.Dropdown` component is readable in both light and dark themes
  - The accent color in the `dcc.RangeSlider` is the theme's primary color
  - The font in all the components and figures are from the Bootstrap theme's font family
  - The  `DataTable` in the Table tab is  styled with the theme's colors and fonts
  - The figures have theme colors and fonts.


You can run this example locally by copying the code in the "view code" tab.

"""


icon = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
icon_text = html.Span(
    [
        icon,
        "Use 'Change Theme' button to see this app with all 26 themes! ",
    ]
)

layout = html.Div(
    [
        html.Div(
            dbc.Alert(
                icon_text, is_open=True, dismissable=True, style={"maxWidth": 350}
            ),
        ),
        example_app("sample_app", make_layout=make_tabs),
        dcc.Markdown(notes, className="m-5")
    ],
    className="dbc",
)

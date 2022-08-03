from dash import html, register_page

from lib.code_and_show import example_app, make_tabs
from lib.other_components import change_theme_alert


register_page(__name__, order=4, description="")

vapor = "https://user-images.githubusercontent.com/72614349/182483204-c91811e4-8068-4b53-bed2-db0fca74efba.gif"
minty = "https://user-images.githubusercontent.com/72614349/182483205-49174237-c303-4186-8daa-ec251003fc47.gif"


notes = """

Dash docs: [DataTable](https://dash.plotly.com/datatable)

If you are using `row_selectable` prop in the datatable, be sure to add  `className="dbc-row-selectable"` so that
the radio buttons are formatted properly in the table and have the Bootstrap theme applied.



"""


layout = html.Div(
    [
        html.H2("Dash DataTable with a Bootstrap Theme"),
        html.Div(
            [
                html.H3("Vapor Theme"),
                html.Img(src=vapor, className="img-fluid"),
            ],
            className="border p-4 m-4",
        ),
        html.Div(
            [
                html.H3("Minty Theme"),
                html.Img(src=minty, className="img-fluid"),
            ],
            className="border p-4 m-4",
        ),
        change_theme_alert(auto_dismiss=False),
        example_app("datatable", make_layout=make_tabs, notes=notes),
    ],
    className="dbc",
)

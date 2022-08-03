from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_tabs
from lib.other_components import change_theme_alert
from lib.utils import app_description


register_page(
    __name__, order=4, description=app_description, title="Adding Themes/DataTable"
)

intro = """
## Dash DataTable with a Bootstrap Theme

Add this stylesheet to your app:
```
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])
```
Then add `className="dbc"`.  See the <dccLink href="/adding-themes/getting-started" children="Getting Started" /> section for more information.  
 
Here's a demo with 2 themes.  See a live example below where you can see this table with any theme.


### Vapor theme:
![Vapor Theme](https://user-images.githubusercontent.com/72614349/182483204-c91811e4-8068-4b53-bed2-db0fca74efba.gif#fluid)

### Minty theme:
"![Minty Theme](https://user-images.githubusercontent.com/72614349/182483205-49174237-c303-4186-8daa-ec251003fc47.gif#fluid)"
"""


notes = """

Dash docs: [DataTable](https://dash.plotly.com/datatable)

If you are using `row_selectable` prop in the datatable, be sure to add  `className="dbc-row-selectable"` so that
the radio buttons are formatted properly in the table and have the Bootstrap theme applied.
"""
layout = html.Div(
    [
        dcc.Markdown(intro, className="p4", dangerously_allow_html=True),
        change_theme_alert(auto_dismiss=False),
        example_app("datatable", make_layout=make_tabs, notes=notes),
    ],
    className="dbc",
)

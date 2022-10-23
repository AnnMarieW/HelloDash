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
To see a [human readable stylesheet,](https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css) 
change the the url above to `/dbc.css` instead of `/dbc.min.css`.

Add `className="dbc"`  
 
Or if you have selectable rows the DataTable, this will style the radio buttons with a Bootstrap theme:

`className="dbc dbc-row-selectable"` 

For an example, see the "view code" tab below or  <dccLink href="/adding-themes/getting-started" children="Getting Started" /> 
section.  
  
------------

Here's a gif to demo two themes.  Use the app below and the "Change Themes" button to see this table with any of the 26 themes.


### Vapor theme:
![Vapor Theme](https://user-images.githubusercontent.com/72614349/182483204-c91811e4-8068-4b53-bed2-db0fca74efba.gif#fluid)

### Minty theme:
"![Minty Theme](https://user-images.githubusercontent.com/72614349/182483205-49174237-c303-4186-8daa-ec251003fc47.gif#fluid)"
"""


notes = """

Dash docs: [DataTable](https://dash.plotly.com/datatable)

"""
layout = html.Div(
    [
        dcc.Markdown(
            intro,
            className="p4 dbc",
            dangerously_allow_html=True,
        ),
        change_theme_alert(auto_dismiss=False),
        example_app("datatable", make_layout=make_tabs, notes=notes),
    ],
)

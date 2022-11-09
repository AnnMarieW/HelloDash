from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_tabs
from lib.other_components import change_theme_alert
from lib.utils import app_description


register_page(
    __name__, order=4, description=app_description, title="Adding Themes/DataTable", name="DataTable"
)

intro = """
## Styling Dash DataTable with a Bootstrap Theme

To style the Dash DataTable with a Bootstrap theme, simply add this stylesheet to your app:
```
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])
```

Then add `className="dbc"` to the DataTable container, or outer container of the app. 

If you have selectable rows the DataTable, this will style the radio buttons with a Bootstrap theme:

`className="dbc dbc-row-selectable"` 

That's it!  

` `  

So how does it work?  The stylesheet defines the "dbc" class.  It uses Bootstrap variable names --  so when the theme
 changes, the components are automatically updated based on the named theme colors. For example, this highlights the
  active cell in the DataTable with the theme's primary color, rather than the default "hotpink":

```css
/* active cell */
.dbc .dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner td.focused {
  background-color: rgba(var(--bs-primary-rgb), 0.2) !important;
  outline: 1px solid var(--bs-primary);
}

```
` `  
` `  

#### Tips
- To see a [human readable stylesheet,](https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css) 
change the the url above to `/dbc.css` instead of `/dbc.min.css`. 
- To customize this stylesheet, download it and place it in a .css file in the `assets` folder.  More info in the [dash-docs](https://dash.plotly.com/external-resources)
- If you find a better way that works for all themes, please [open an issue](https://github.com/AnnMarieW/dash-bootstrap-templates/issues). Pull requests are welcome!
- If you add `className="dbc"` to the outer container of your app, you do not need to add it to every component.  See an
example in the <dccLink href="/adding-themes/dcc-components" children="dash-core-components" /> section.

` `  
` `  

### Examples

Here's a gif to demo two themes.  Use the app below and the "Change Theme" button to see this table with any of the 26 themes.


##### Vapor theme:
![Vapor Theme](https://user-images.githubusercontent.com/72614349/182483204-c91811e4-8068-4b53-bed2-db0fca74efba.gif#fluid600)

##### Minty theme:
"![Minty Theme](https://user-images.githubusercontent.com/72614349/182483205-49174237-c303-4186-8daa-ec251003fc47.gif#fluid600)"
"""


notes = """

Dash docs: [DataTable](https://dash.plotly.com/datatable)

"""




next = """
-----------------  

### Next:  
Using Bootstrap themed Plotly <dccLink href="/adding-themes/figure-templates" children="figure templates" />

"""





layout = html.Div(
    [
        dcc.Markdown(
            intro,
            className="mx-5 px-3 dbc",
            dangerously_allow_html=True,
        ),
        change_theme_alert(auto_dismiss=False),
        example_app("datatable", make_layout=make_tabs, notes=notes),
        dcc.Markdown(
            next,
            className="m-5 px-3 dbc",
            dangerously_allow_html=True,
        ),
    ],
)

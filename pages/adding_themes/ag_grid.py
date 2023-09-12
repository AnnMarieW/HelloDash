from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_tabs
from lib.other_components import change_theme_alert
from lib.utils import app_description


register_page(
    __name__, order=3, description=app_description, title="Adding Themes/Ag Grid", name="Dash AG Grid"
)

intro = """
## Styling Dash AG Grid with a Bootstrap Theme

To style the Dash AG Grid with a Bootstrap theme, simply add this stylesheet to your app:
```
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])
```

Then add `className="dbc dbc-ag-grid"` to the outer container of the app.

```
app.layout = dbc.Container(
    [
        ...
    ],
    fluid=True,
    className="dbc dbc-ag-grid"
)
``` 
"""

text2 = """


So how does it work?  The stylesheet defines the `dbc-ag-grid` class.  It uses Bootstrap variable names --  so when the theme
 changes, the grid is automatically updated based on the Bootstrap theme colors and fonts.
 
The `dbc-ag-grid` class is designed to work along with the grid's `ag-theme-alpine`, which is the default theme in
  the `dash-ag-grid` component. Learn more about styling dash-ag-grid in the [Dash Documentation](https://dash.plotly.com/dash-ag-grid/styling-themes)

To only style certain grids with the the Bootstrap theme, you can use the grid component's className.  But be sure to 
also include `ag-theme-alpine`. For example:  
```
app.layout = dbc.Container(
    [
        dag.AgGrid(
            className="ag-theme-alpine dbc-ag-grid",        
        )
    ],
    fluid=True,
    className="dbc"
)

```


` `  
` `  

#### Tips
- To see a [human readable stylesheet,](https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css) 
change the the url above to `/dbc.css` instead of `/dbc.min.css`. 
- To customize this stylesheet, download it and place it in a .css file in the `assets` folder.  More info in the [dash-docs](https://dash.plotly.com/external-resources)
- If you find a better way that works for all themes, please [open an issue](https://github.com/AnnMarieW/dash-bootstrap-templates/issues). Pull requests are welcome!
- If you add `className="dbc dbc-ag-grid"` to the outer container of your app, you do not need to add it to every component. 


` `  
` `  

"""


notes = """

Dash docs: [Dash AG Grid](https://dash.plotly.com/dash-ag-grid)

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
        example_app("ag_grid", make_layout=make_tabs, notes=notes),
        dcc.Markdown(
            text2,
            className="mx-5 px-3 dbc",
            dangerously_allow_html=True,
        ),
        dcc.Markdown(
            next,
            className="m-5 px-3 dbc",
            dangerously_allow_html=True,
        ),
    ],
)

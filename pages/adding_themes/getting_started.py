from dash import register_page, html, dcc
from lib.code_and_show import example_app, make_app_first
from lib.utils import app_description

register_page(
    __name__,
    order=0,
    description=app_description,
    title="Adding Themes/Getting started",
    name="Getting started",
)


notes1 = """
## Adding a Bootstrap Theme 

When you add a Bootstrap stylesheet, all dash-bootstrap-components will be styled with your selected theme. 
See the [dash-bootstrap-components Quickstart docs](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/) for more info.

For example, add the stylesheets for the "SPACELAB" theme and FontAwesome icons to a Dash app like this:

```python
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME])  

```

Note that the Bootstrap theme is not automatically applied to other components such as dash-core-components, DataTable and Figures.

👈 See the <dccLink href="/theme-explorer/gallery" children="dbc Gallery" /> section to view a collection dash-bootstrap components and see how they look with different themes.
Find more info about themes at [Bootswatch.com](https://bootswatch.com/)

----------
"""

notes2 = """
----------
## Apply Bootstrap Theme to Dash Core Components and DataTable

The `dash-core-components`, the Dash `DataTable` and Plotly figures are not automatically styled with a Bootstrap theme.
An easy way to make your Dash components look better with a Bootstrap theme is to use the stylesheet from
 the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. This stylesheet defines the "dbc" class.

Adding `className="dbc"` minimally styles Dash components with your selected Bootstrap theme:
- Makes the text readable in both light and dark themes.
- Uses theme's font-family.
- Changes the accent color to the theme's primary color


You can add the dbc class as an external stylesheet like this:
```
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

```

> See a human readable stylesheet by changing the  the the url above to `/dbc.css` instead of `/dbc.min.css`.


Add  `className="dbc"` to the outer container of the app or a component like this:
```
app.layout = dbc.Container(
    [
        ...
    ],
    fluid=True,
    className="dbc"
)
```

**That's it!** Simply adding `className="dbc"` will make Dash Core Components and the DataTable look better with **ALL** themes included in the `dash-bootstrap-components` library.
  
👈 See examples of <dccLink href="/adding-themes/dcc-components" children="dash-core-components" /> 
and <dccLink href="/adding-themes/datatable" children="DataTable" /> with a Bootstrap theme.  


"""


notes3 = """
-----------
### Bootstrap Themed Figure Templates

`dash-bootstrap-templates` library provides **Bootstrap themed Plotly figure templates**. You will find a Plotly template for each of the 26 Bootstrap/Bootswatch themes available in the
[Dash Bootstrap Components Library](https://dash-bootstrap-components.opensource.faculty.ai/). These templates will automatically style your figures with Bootstrap theme colors and fonts.

> Learn more about Plotly figure templates and themes at: https://plotly.com/python/templates/

👈 See all 26 Bootstrap themed Plotly <dccLink href="/adding-themes/figure-templates" children="Figure templates" /> 

"""

notes4 = """

----------

#### More figure template examples:

![image](https://user-images.githubusercontent.com/72614349/143956545-769a00f8-92a3-44aa-8718-bdbb32b2464e.png#fluid600)
![image](https://user-images.githubusercontent.com/72614349/143956649-32b620c7-231a-4de6-ad3a-8fb0863da2a4.png#fluid600)

"""


layout = html.Div(
    [
        example_app(
            "adding_theme",
            make_layout=make_app_first,
            notes_first=notes1,
        ),
        dcc.Markdown(notes2, className="p-4", dangerously_allow_html=True),
        example_app("adding_theme_figure_template", notes_first=notes3, notes=notes4),
    ],
    className="dbc",
)

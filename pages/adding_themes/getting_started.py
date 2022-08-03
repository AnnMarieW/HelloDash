from dash import register_page, html, dcc


from lib.code_and_show import example_app, make_app_first


register_page(__name__, order=0, description="", name="Getting started")


notes1 = """
## Adding a Bootstrap Theme 

When you add a Bootstrap stylesheet, all dash-bootstrap-components will be styled with your selected theme. 
See the [dash-bootstrap-components Quickstart docs](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/) for more info.

Note that the Bootstrap theme is not automatically applied to other components such as dash-core-components, DataTable and Figures.

See the [dbc Gallery]() section to see all the dbc components.

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

See a human readable stylesheet by changing the  the the url above to `/dbc.css` instead of `/dbc.min.css`


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

See examples in the [TODO section!]()

"""


notes3 = """
-----------
### Bootstrap Themed Figure Templates

`dash-bootstrap-templates` library provides **Bootstrap themed Plotly figure templates**. You will find a Plotly template for each of the 26 Bootstrap/Bootswatch themes available in the
[Dash Bootstrap Components Library](https://dash-bootstrap-components.opensource.faculty.ai/). These templates will automatically style your figures with Bootstrap theme colors and fonts.

> Learn more about Plotly figure templates and themes at: https://plotly.com/python/templates/


"""


layout = html.Div(
    [
        example_app(
            "adding_theme",
            make_layout=make_app_first,
            notes_first=notes1,
        ),
        dcc.Markdown(notes2, className="p-4"),
        example_app("adding_theme_figure_template", notes_first=notes3),
    ],
    className="dbc",
)

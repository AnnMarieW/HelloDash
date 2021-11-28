from dash import dcc


about_dbc_css_md = dcc.Markdown(
    """
The `dash-core-components`, the Dash `DataTable` and Plotly figures are not automatically styled with a Bootstrap theme.
An easy way to make your Dash components look better with a Bootstrap theme is to use the stylesheet from
 the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. This stylesheet defines the "dbc" class.

Adding `className="dbc"` minimally styles Dash components with your selected Bootstrap theme:
- Makes the text readable in both light and dark themes.
- Uses the font from the Bootstrap theme's font-family.
- Changes the accent color to the theme's primary color


You can add the dbc class as an external stylesheet like this:
```
dbc_css = ("https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css")
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

```
You can also add the stylesheet to your assets folder. If you would like to modify it, you can find a more human readable stylesheet here:  "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.css"

This stylesheet is from version V1.0.2. Check the dash-bootstrap-templates library for the latest updates.


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

## That's it!  

Simply adding `className="dbc"` will make Dash Core Components and the DataTable look better with **ALL** themes included in the `dash-bootstrap-components` library.

If you have suggestion for improvements or if you find a bug, please let us know on the [issue tracker](https://github.com/AnnMarieW/dash-bootstrap-templates/issues)

**Requires `dash-bootstrap-components>=V1.0.0`**

""",
    className="dbc p-4",
    id="about-dbc-css",
)



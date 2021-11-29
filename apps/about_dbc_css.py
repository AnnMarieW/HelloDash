from dash import dcc, html
import dash_bootstrap_components as dbc
import apps.dcc_component_gallery as dcc_gallery


heading_about_dbc_css = html.H2(
    "About className='dbc'",
    className="text-white bg-primary p-2 mt-4",
)


heading_examples = html.H2(
    "Examples",
    className="text-white bg-primary p-2 mt-4",
)



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

about_examples_text = dcc.Markdown(
    """
The column on the left has `className="dbc" added.  Try changing the themes - you will see the 
biggest difference in dark themes.  

Also, interact with the components. Notice that when you hover over
the icons in the DataTable or select a cell, it's the theme's primary color rather than the default
hot pink.  Try selecting dates in the datapickers.  You will see the calendar has a dark background in dark
themes and the dates are highlighted in the primary color.     
    """
)

about_examples_md = dbc.Alert(about_examples_text, color="primary", className="p-2")


def make_dcc_card():
    """ This makes a comparison between with className=dbc and default"""
    content = html.Div(
        [
            dcc_gallery.datatable,
            dcc_gallery.dcc_date_picker_single,
            dcc_gallery.dcc_date_picker_range,
            dcc_gallery.dcc_dropdowns,
            dcc_gallery.dcc_slider,
            dcc_gallery.dcc_range_slider,
            dcc_gallery.dcc_tabs,
        ]
    )
    return dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            ' with ClassName="dbc"',
                            className="card-title h3 overflow-auto text-nowrap",
                        ),
                        dbc.CardBody(content),
                    ],
                    outline=True,
                    color="primary",
                ),
                className="dbc",
                width=6
            ),
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Default style",
                            className="card-title h3 overflow-auto text-nowrap",
                        ),
                        dbc.CardBody(content),
                    ]
                ),
                width=6,
            ),
        ]
    )


about_dbc_css = dbc.Row(
        [
            dbc.Col(
                dbc.Card([heading_about_dbc_css, about_dbc_css_md], outline=True, color="primary", body=True),
                className="dbc",
            ),
        ]
    )


layout = html.Div(
    [
        heading_about_dbc_css,
        about_dbc_css_md,
        heading_examples,
        about_examples_md,
        make_dcc_card()
    ],
    className="mb-4"

)
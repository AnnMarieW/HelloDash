"""
This is for longer text and code blocks used throughout this app.

"""

"""
=====================================================================
Used in: app_gallery.py
"""

tutorial = """

### Bootstrap Themes
The Explorer app makes it easy to see how a Bootstrap or [Bootswatch theme](https://www.bootstrapcdn.com/bootswatch/)
 will look in your Dash app.  Choose from one of 22 Bootstrap themes - or even create your own.   

Note that the light Bootstrap themes are the easiest themes to use with Dash.  The Dash components have a light 
background color and that works well with the Bootswatch light themes.  A dark theme will set the text color to 
white or some other light color making the text hard to read in some Dash components. 

### Dark Theme
 Here are some way to change the colors in Dash components:
-  Dash Core Components:  Try using the `className` or `style` parameter of the component or use the inspector in the browser to see how the colors are set and override it with custom CSS in the assets folder. 
See more information [here](https://dash.plotly.com/external-resources).   See the css we used here [ github link](https://github.com/AnnMarieW/HelloDash/blob/main/assets/mycss.css) 
-  Dash DataTables:  See how to set a dark theme [here](https://dash.plotly.com/datatable/style) in the Dash documentation
-  Dash DAQ components: Use the `theme` parameter:   `theme= {'dark': True}`
-  Figures: Use the [Graph template](https://plotly.com/python/templates/)  `plotly_dark`


### Graph Templates

Setting the Plotly graph template is a quick way to set the style of the figure  in your app.  Try selecting one of 
the 11 standard templates to see how they look with your  Bootstrap themes.  Note that the  "plotly_dark" template 
works well with Bootstrap  dark themes.

The templates  can also be used to  can pre-populate a figure with visual elements like annotations, shapes,
images, and more. Learn more about Plotly templates and how to customize them [here](https://plotly.com/python/templates/)

### Discrete Colors & Continuous Colorscales

Selecting the Plotly trace colors that look nice with your selected Bootstrap theme can really enhance your app design.
See the Dash documentation to learn more about [discrete colors](https://plotly.com/python/discrete-color/) and 
[continuous colorscales](https://plotly.com/python/colorscales/)
"""


"""
=====================================================================
Used in: html.dbc_components.py
"""

typography_code = """
typography = html.Div(
    [
        html.H2("Typography"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Heading 1"),
                        html.H2("Heading 2"),
                        html.H3("Heading 3"),
                        html.H4("Heading 4"),
                        html.H5("Heading 5"),
                        html.H6("Heading 6"),
                        html.H3(
                            [
                                "This html.H3 heading has ",
                                html.Small("some muted html.Small text", className="text-muted"),
                            ]
                        ),
                        html.P(
                            "The className=`lead`adds emphasis to this html.P paragraph.",
                            className="lead",
                        ),
                    ],
                    className="p-4",
                ),
                dbc.Col(
                    [
                        html.H2("Example of body text"),
                        html.P(
                            [
                                "This is some text with an embedded link using ",
                                html.A("html.A", href="#"),

                            ]
                        ),
                        html.P(
                            html.Small(
                                "This is html.Small - use this for the fine print"
                            )
                        ),
                        html.P(
                            [
                                "The following is rendered in bold text ",
                                html.Strong("using html.Strong"),
                            ]
                        ),
                        html.P(
                            [
                                "The following is rendered in italics ",
                                html.Em("using html.Em"),
                            ]
                        ),
                        html.P(
                            [
                                "html.Abbr represents an abbreviation or acronym like this:",
                                html.Abbr("abbr", title="abbreviation"),
                            ]
                        ),
                    ],
                    className="p-4",
                ),
                dbc.Col(
                    [
                        html.H2("Emphasis classes"),
                        html.P(
                            "text with className='text-muted'", className="text-muted"
                        ),
                        html.P(
                            "Text with className='text-primary'",
                            className="text-primary",
                        ),
                        html.P(
                            "Text with className='text-secondary'",
                            className="text-secondary",
                        ),
                        html.P(
                            "Text with className='text-warning'",
                            className="text-warning",
                        ),
                        html.P(
                            "Text with className='text-danger'", className="text-danger"
                        ),
                        html.P(
                            "Text with className='text-success'",
                            className="text-success",
                        ),
                        html.P(
                            "Text with className='text-info'", className="text-info"
                        ),
                        html.P(
                            "Text with className='bg-primary text-white'", className="bg-primary text-white"
                        ),
                    ],
                    className="p-4",
                ),
                typography_text
            ]
        ),
    ]
)
"""

blockquotes_code = """
blockquotes = html.Div(
    [
        html.H2("Blockquotes and text alignment"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    [
                                        "Someone famous in ",
                                        html.Cite("Source Title", title="Source Title"),
                                    ],
                                    className="blockquote-footer",
                                ),
                            ],
                            className="blockquote",
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    [
                                        "Someone famous in ",
                                        html.Cite("Source Title", title="Source Title"),
                                    ],
                                    className="blockquote-footer",
                                ),
                            ],
                            className="blockquote text-center",
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P(
                                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    [
                                        "Someone famous in ",
                                        html.Cite("Source Title", title="Source Title"),
                                    ],
                                    className="blockquote-footer",
                                ),
                            ],
                            className="blockquote text-right",
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
            ]
        ),
    ]
)

"""

blockquotes_code2 = """
blockquotes2 = html.Div(
    [
        html.H4("Blockquotes using className and style parameters"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P(
                                    "We dine well here in Camelot. We eat ham and jam and spam a lot.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    html.Cite(
                                        "Knights of Camelot",
                                        title="Camelot the Musical",
                                    ),
                                    className="blockquote-footer",
                                ),
                            ],
                            className="blockquote text-left pl-4 border-light",
                            style={"borderLeft": "solid", "borderLeftWidth": 15},
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P(
                                    "Always code as if the guy who ends up maintaining your code will be a violent "
                                    "psychopath who knows where you live.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    "Martin Golding ", className="blockquote-footer"
                                ),
                            ],
                            className="blockquote text-left pl-4 border-primary",
                            style={"borderLeft": "solid", "borderLeftWidth": 5},
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P(
                                    "There are only two industries that refer to their customers as ‘users’.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    "Edward Tufte ", className="blockquote-footer",
                                ),
                            ],
                            className="blockquote text-left pl-4 border-secondary",
                            style={"borderLeft": "solid", "borderLeftWidth": 10},
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
            ]
        ),    
    ]
)

# -------------------------------------------------------------------

#  Here is another way to format blockquotes.  Put the following in a 
#  css file in the assets folder.  Change the #  border-left color to one
#  that works well with your selected Bootstrap theme.


/* 
 * When using Bootstrap, this will add the left border style to blockquotes 
 * in dcc.Markdown and html.Blockquote 
 */
blockquote {
  border-left: 4px lightgrey solid;
  padding-left: 1rem;
  margin-top: 2rem;
  margin-bottom: 2rem;
  margin-left: 0rem;
}

"""


"""
===========================================================================
Used in:  cheatsheet.py 
"""

pythonanywhere_quickstart = """
# Pythonanywhere Quickstart Guide

Your free PythonAnywhere account comes with a website at http://your-username.pythonanywhere.com/. 

### Setting up a page
You can create an app to run there by going to the Web tab of your account. From there you click on the 
"Add a new web app" button, which will pop up a wizard where you can  select a web application framework.
 Use the "quickstart" options for Flask.


### Uploading files
Follow [these instructions](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/) for getting your 
app files uploaded.  

If this is your first time, you can even skip this step for now.  Just copy the code for the Dash Hello World app 
from the [Dash tutorial](https://dash.plotly.com/layout) and paste it into the app that was set up when you did 
the Flask quickstart called "flask_app.py".


### Configure WSGI file
If you just copied and pasted into "flask_app.py" you can skip this step.  The WSGI file is already configured. 
 If you want to run a different app, follow [these instructions](https://help.pythonanywhere.com/pages/DashWSGIConfig/)

### Error Log
If you click on reload webpage and go to your app, you will get an error message.  You will find details if 
you click on the link for the error log.  This is because Dash needs to be installed.   More info on debugging 
this and other errors [here](https://help.pythonanywhere.com/pages/)


### Install Dash

Many modules are already included, but you will need to install Dash.  Here's how:
Click on the Console tab and open a Bash console.

`pip3.8 install --user dash`    

Please note, the command line option before the module name is quite literally `--user`, you don't need to 
replace it with your username, or to add your username to the command line. More in installing dependencies and using  a virtual environment [here](https://help.pythonanywhere.com/pages/InstallingNewModules/)

Go back to the Web tab, reload the page.  That's it!  Your first app is live!!

"""


cheatsheet_advanced_callback = """

|What to use||When to use it |  
| :----|:----| :----|  
|```  PreventUpdate ```| |Prevents _all_ outputs of a callback from updating| 
|`dash.no_update`|| Prevents _certain_ outputs of a callback from updating|
|`prevent_initial_call=True`|| Prevents initial call of a  _certain_ callback|
|`prevent_initial_callbacks=True` || Prevents _all_ initial calls|
| `dash.callback_context`|| Determine which Input triggered a callback|


---
#### Code snippets:

```  PreventUpdate ```
```
    from dash.exceptions import PreventUpdate    
    ...   
    def update_output(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
```

---
`dash.no_update`    
```
        # first  Output not updated
        return dash.no_update, figure
```


---
`prevent_initial_call=True`
```
    @app.callback(Output('container', 'children'),
                   Input('btn-1', 'n_clicks'),
                   Input('btn-2', 'n_clicks'),
                   prevent_initial_call=True
    )
```
---
`prevent_initial_callbacks=True`
```
    app = Dash(name=__name__, prevent_initial_callbacks=True)
```


---

`dash.callback_context`    
```
    @app.callback(Output('container', 'children'),
                   Input('btn-1', 'n_clicks'),
                   Input('btn-2', 'n_clicks'))
    def display(btn1, btn2):
        ctx = dash.callback_context
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if input_id == 'btn-1':
            # do something...
```
"""

# this is created in  cheatsheet.py and displayed in datatable.py
datatable_markdown = """
    Add the following to the css file in the assets folder:

    /*  when using Bootstrap, this will style the table in dcc.Markdown */

    table {
      border-collapse: collapse;
    }
    th:not(.CalendarDay),
    td:not(.CalendarDay) {
      padding: 12px 15px;
      text-align: left;
      border-bottom: 1px solid #E1E1E1; }
    th:first-child:not(.CalendarDay),
    td:first-child:not(.CalendarDay) {
      padding-left: 0; }
    th:last-child:not(.CalendarDay),
    td:last-child:not(.CalendarDay) {
      padding-right: 0; }
      """

datatable_move_export_btn = """

    # This moves the Export and/or Toggle Columns button to the bottom left 
    # side of the DataTable

    import dash
    import dash_table
    import pandas as pd
    
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")
    
    app = dash.Dash(__name__)
    
    app.layout = dash_table.DataTable(
        id="table",
        columns=[{"name": i, "id": i, "hideable": True} for i in df.columns],
        export_format="xlsx",
        css=[
            # If export button only,  use this:
            #{"selector": ".export", "rule": "position:absolute; left: 0px; bottom:-30px"},
    
            # If both export button and toggle columns button,  use this:
            {
                "selector": ".dash-spreadsheet-menu",
                "rule": "position:absolute; left:0px; bottom:-30px",
            },
        ],
        data=df.to_dict("records"),
    )
    
    if __name__ == "__main__":
        app.run_server(debug=True)
    

"""

"""
=========================================================================
Used in: DataTable.py 
"""


datatable_light_text = """   

    With two simple style changes, the DataTable will look even better in your app with Bootstrap light themes:

    -  Change the font to be the same font as your selected theme.
    -  Change the active and selected cells to Bootstrap theme colors rather than the Dash default of "hotpink". Try
    selecting cells in this table and in the default table above to see the style difference.
"""


datatable_light_code = """ 
        Styling a Dash Datatable with a Light theme.  Note:  To see how to format
        the tooltip, switch to a dark theme to see more info and example.
    
        # DashTable updated with font and colors from this bootstrap theme:        
        # https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.css 
        
               
        font = "sans-serif"
        primary = "#007bff"
        secondary = "#6c757d"
        selected = "rgba(0, 0, 0, 0.075)"

        datatable = dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            style_cell={"fontFamily": font},
            style_data_conditional=[
                {
                    "if": {"state": "active"},
                    "backgroundColor": selected,
                    "border": "1px solid " + primary,
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": selected,
                    "border": "1px solid" + secondary,
                },
            ],
        )   
"""


datatable_dark_text = """    

    When you use a dark theme, you will need to do a few more things to make the DataTable look nice.  The next table
    has the following style changes:

    -  The table background color is transparent to make it the same as the Bootstrap background color.
    -  The font color is white when cells are selected or the table is editable. This makes text visible in a dark background.
    -  The hover color is changed to transparent.  This is done because the default hover background color is white
    which looks bad and makes the text disappear.
    -  The text color of tooltips is changed to black.  The default background color is grey, which isn't bad -- but note
     that you can also use this same selector to change the background color and/or add other style changes to tooltips.

"""


datatable_dark_code = """
    Styling a Dash Datatable with a Light theme
    
    # DashTable updated with font and colors from this bootstrap theme:    
    # https://bootswatch.com/4/cyborg/bootstrap.css   
     
    primary = "#2a9fd6"
    secondary = "#555"
    selected = "rgba(255, 255, 255, 0.075)"
    font_color = "white"
    font = "Roboto"    

    datatable =dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        editable=True,
        page_size=4,
        css=[
            {"selector": "input", "rule": f"color:{font_color}"},                # fixes text color for editable columns
            {"selector": "tr:hover", "rule": "background-color:transparent"},    # fixes hover bg color 
            {"selector": ".dash-table-tooltip", "rule": "color:black"},          # fixes text color of tooltip data
        ],
        style_cell={"backgroundColor": "transparent", "fontFamily": font},
        style_data_conditional=[
            {
                "if": {"state": "active"},
                "backgroundColor": selected,
                "border": "1px solid " + primary,
                "color": font_color,
            },
            {
                "if": {"state": "selected"},
                "backgroundColor": "selected",
                "border": "1px solid" + secondary,
                "color": font_color,
            },
        ],
    )  
    """

"""
=====================================================================
Used in: dcc_components.py
"""

dcc_checklist_radio_1 = """
##### Styling dcc.RadioItems and dcc.Checklist
The first row of dcc.Checklist and dcc.RadioItems below shows the default style.
It's also possible to adjust the margins and style of the text label using the `inputStyle, InputClassName, 
labelStyle, labelClassName` parameters. See [this example]( https://community.plotly.com/t/dcc-radioitems-and-label-style/26358/2)
 for how to change the label color in a callback.  Unfortunately, there is no easy way to change the color 
 of the radio and checkbox icons."""

dcc_checklist_radio_2 = """
A great alternate is to use `dash-bootstrap-components` dbc.Checklist and dbc.RadioItems. Here are the advantages:

- The checked boxes and selected radio items of dbc components automatically use the theme's "primary" color.  See this in action by changing the theme in the App Design Selections panel. 
- You can also customize the selected label and icons color in dbc components using `labelCheckedStyle` and `labelCheckedStyle` parameters.
- By default there is nice spacing between the icon and the label, so there is no need to define this manually.
-  The dbc.Checklist can be displayed as toggle switches by setting `switch=True`.  See the dash-boostrap-components gallery for an example.  

Here is an example of `dash-bootstrap-components` dcc.Checklist and dcc.RadioItems.  Change the theme to see the updated
style:"""

dcc_tabs = """
##### Styling dcc.Tabs

 If you switch to a dark theme you will see that the default style for dcc.Tabs shown here does not work well. However,
 the dcc.Tabs are very easy to customize using the `style` and `selected_className` parameters.   

The tabs on the left are the default and the tabs on the right are styled so that they work well with both light and
dark themes. The selected tab is highlighted with the "primary" theme color and the background is transparent.  

The tabs for this Component Gallery use dcc.Tabs styled for all themes and and `vertical=True`
"""

dcc_dropdown = """

##### Styling dcc.Dropdown

The dcc.Dropdown default style works well with many Bootstrap light themes.  However with dark themes, the
font color makes the dropdown options text very hard to read. 

We fix it in this app by using the following CSS in the asset folder:"""

dcc_dropdown_css = """
```

/** This styles the dropdown menu items so they are visible in both light and dark theme apps **/
.VirtualizedSelectOption {
    background-color: white;
    color: black;
}

.VirtualizedSelectFocusedOption {
    background-color: lightgrey;
    color: black;
}
```"""

dcc_graph = """

##### Styling dcc.Graph

The Plotly figures are highly customizable.  The options shown in the Theme Explorer app such as changing the colorscale
and the template are only *some* of the many choices available.  See the Plotly card in the Cheatsheet tab to see 
a few of my favorite Plotly resources and tutorials.

Below is another way to make graphs look better in dark themes.  The figure on the right has a transparent background.
It also use the "plotly_dark" template which makes the text and grid lines look better with dark themes


Try switching between different dark themes in the App Design Selections panel to see how it looks! 
"""

dcc_graph_code = """
```
# This is a figure with a transparent background color for the  plot and paper
# It also uses the "plotly_dark" template which makes the text and grig lines look 
# better with dark themes

df = px.data.gapminder()
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    size_max=60,
    template="plotly_dark",
)
fig.update_layout(
    {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"}
)
```
"""


dcc_slider = """
##### Styling dcc.Slider and dcc.RangeSlider

The default style for the dcc.Slider and dcc.RangeSlider is shown on the left.  It's possible to change the 
style of the label with the `marker`  property, but if you would like to update the color of the track, or the handles, 
or the selected label style, it's  necessary to use custom CSS.  
 
 The sliders on the right side are updated with the primary colors of the PULSE theme.  See the CSS to add to your
 css file in the assets folder:
"""


dcc_slider_css = """

/*
 * Custom CSS for sliders -  PULSE Theme
 */
.rc-slider-handle {
  border: 0;
  background-color: #593196;  /* primary */
}

.rc-slider-rail {
  background-color: #ededed;  /* grey */
}

.rc-slider-track {
  background-color: #593196;  /* primary */
}

.rc-slider-dot {
  border: 0;
  background-color: #ededed; /* grey */
}

.rc-slider-dot.rc-slider-dot-active {
  background-color: #593196;  /* primary */
}

.rc-slider-mark-text {
  color: #868e96;    /* label color */
}

.rc-slider-mark-text.rc-slider-mark-text-active {
  color: #343a40;     /* Makes the active label color different than default label color */
}
"""

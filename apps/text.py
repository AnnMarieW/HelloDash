"""
This is for longer text and code blocks used throughout this app.

"""

"""
=====================================================================
Used in: dash_bootstrap_templates_explorer.py
"""

css_text = """ 
    #### Custom CSS for Dash apps with Bootstrap themes.  
    
    Dash components and `dash-bootstrap-components` can be styled with the components' `style` and/or `className` parameter.
     Most dbc components will automatically update when the theme changes - like the color of the checkboxes will be the
     theme's "primary" color.   However, some parts of some Dash components don't update based on their `style` and 
     `className` properties.  For example if you would like to change the color of the slider, or make 
     dropdown options more visible in dark themes, you need to use custom CSS.  
     
    In the [assets folder](https://github.com/AnnMarieW/HelloDash/tree/main/assets) for this app,
    see the stylesheets that define the classNames  `dbc_light dbc_dark, dbc_both`. Use these classNames to enhance the 
    design of your Dash app when using Bootstrap themes.
    
    - [`dbc_both `](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_both.css)
    has minimal CSS and is just enough to make text visible in dropdowns in both light and dark themes. When
    using a DataTable, it only fixes issues like data cut off at the edges, and it works best with light themes.
    - [`dbc_light`](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_light.css)
     uses  CSS to add Bootstrap theme colors to  dcc components and the DataTable. See more details in the Component Gallery.
    - [`dbc_dark`](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_dark.css)
     add Bootstrap theme colors to dcc components and the DataTable.  It looks best with dark themed apps.  See more details in the Component Gallery.
    
     
    In the Dash Component Gallery below, you will find details on how to apply custom CSS to Dash Core Components, 
    HTML Components and the DataTable.  Dash DAQ components coming soon!  
    
    See also the Dash documentation:
    
      - [How to add custom CSS to a Dash app](https://dash.plotly.com/external-resources).
      
    If you work for a company, see also Dash Enterprise Design Kit.
"""

"""
=====================================================================
Used in: dbc_components.py
"""

dbc_intro_text = """  
    `dash-bootstrap-components` is a library of Bootstrap components for Plotly Dash that makes it easier to build 
    consistently styled apps with complex, responsive layouts. It's provided open source by [Faculty AI](https://dash-bootstrap-components.opensource.faculty.ai/).  
    Click on the component name in the card header to go directly to the component's official documentation for more
     info and great examples.  

    All dash-boostrap-components are automatically styled based on your selected Bootstrap theme -- no custom CSS is required!
    See this in action by changing the Bootstrap theme in the App Design Selections panel above.  

    Note that most of the other Dash components (such as `dash-core-components`, `DataTable` and `DAQ` components) and 
    Plotly figures have some elements of the component that cannot be updated with the `style` and className`
    properties, so they do not all respond well to changes to Bootstrap themes.  See more information on how to style
    these components by clicking on the tabs to the left. 
        
    - [dash-bootstrap-components documentation](https://dash-bootstrap-components.opensource.faculty.ai/)
    - [Bootswatch Themes](https://www.bootstrapcdn.com/bootswatch/)
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
See more information [here](https://dash.plotly.com/external-resources).   See the css we used here [ github link](https://github.com/AnnMarieW/HelloDash/blob/main/assets) 
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
Used in: html_components.py
"""

html_intro_text = """ 
    The `dash-html-components` library has a component for every HTML tag.  All components are fully customizable using
    the  `className` and `style` parameter.
    
    When you use Bootstrap classes, the style will automatically be updated when you change themes - no custom CSS
    required!  See this in action by changing the Bootstrap theme in the App Design Selections panel above.  Notice that 
    the font and the colors change according to the theme selected.

    Note - it's often easier to use dbc or dcc components rather than dash-html-components.  See dcc.Markdown for an easy 
    way to format text - including code blocks, lists, simple tables and more.  See also dbc.Table and 
    Dash DataTable for formatting tables, and other dbc components for lists and forms. 

    - See the  full documentation for [dash-html-components](https://dash.plotly.com/dash-html-components) 
    - Learn more about [Bootstrap classes](https://getbootstrap.com/docs/3.4/css/)
    - This is my favorite Bootstrap classes [cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)   
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
=========================================================================
Used in: DataTable.py 
"""

datatable_intro_text = """
    Dash `DataTable` is an interactive table component designed for viewing, editing, and exploring large datasets. 

     - [DataTable Quickstart](https://dash.plotly.com/datatable)
     - [DataTable styling](https://dash.plotly.com/datatable/style)
     - [DataTable Reference](https://dash.plotly.com/datatable/reference)
"""


datatable_default_text = """
    This is the default style of the Datatable.  Note the hotpink accents in the header icons and when you select cells,
    This accent color does not look nice with many themes.   Also, with dark themes, the table is unreadable. 
    
    The good news is that DataTable is highly customizable  -- see the Dash DataTable documentation for details.
    
    The tables in the next sections are styled with custom CSS optimized for Bootstrap themes. Learn how below.

"""


datatable_light_text = """   

    This DataTable is styled with the `className='dbc_light'` 
    
    - The background color is the Bootstrap theme's "light" color.
    - The text color is the Bootstrap theme's "dark" color.
    - The font is the Bootstrap theme's font.
    - The accent color for icons is changed from the Dash default hotpink to the Bootsrap theme's "primary" color.
    The icons are the pagination arrows and the icons in the header if the table is sortable or columns are deletable.
    
    The DataTable is also styled with `style_data_conditional` to change the hotpink color on active and selected cells.
    
    Click on the code button to see the code and CSS for this table
    
"""

datatable_light_hover_text = """   

    This DataTable is styled with the `className='dbc_light dbc_row_hover'` 
    
    - The `dbc_row_hover`  className removes all of the hotpink accents in the table body without using `style_data_conditional` prop.
    - There is no styling of active or selected cells, but the functionality remains.  
     
     Note that this overrides formatting for text color, border color, and opacity in the `style_*` props
     in the DataTable.  Also, it does not work for tables with fixed columns. See [issue #871](https://github.com/plotly/dash-table/issues/871)
"""


datatable_light_code = """ 
        Styling a Dash Datatable with a light theme. 
        
        ```
        light_table = html.Div(
            dash_table.DataTable(
                columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
                data=df.to_dict("records"),
                editable=True,
                page_size=4,
                filter_action="native",
                sort_action="native",
                style_data_conditional=[
                    {"if": {"state": "active"}, "border": "1px solid var(--primary)",},
                    {"if": {"state": "selected"}, "border": "1px solid var(--secondary)",},
                ],
            ),
            className="dbc_light",
        )        
        ```
        
        The class `dbc_light` is defined in the assets folder [here](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_light.css)
        
"""


datatable_dark_text = """   
    This DataTable is styled with the `className='dbc_dark'` 
    
    - The background color is the Bootstrap theme's "dark" color.
    - The text color is the Bootstrap theme's "light" color.
    - The font is the Bootstrap theme's font.
    - The text color for tooltips is black so it's more visible with the default grey background
    - The accent color for icons is changed from the Dash default hotpink to the Bootsrap theme's "primary" color.
    The icons are the pagination arrows and the icons in the header if the table is sortable or columns are deletable.
    
    The DataTable is also styled with `style_data_conditional` to change the hotpink color on active and selected cells.
    
    Click on the code button to see the code and CSS for this table
    

"""

datatable_dark_hover_text = """   

    This DataTable is styled with the `className='dbc_dark dbc_row_hover'` 

     - The `dbc_row_hover`  className removes all of the hotpink accents in the table body without using `style_data_conditional` prop.
    - There is no styling of active or selected cells, but the functionality remains.  
    
     Note that this overrides formatting for text color, border color, and opacity in the `style_*` props
     in the DataTable.  Also, it does not work for tables with fixed columns. See [issue #871](https://github.com/plotly/dash-table/issues/871)
"""


datatable_dark_code = """
    Styling a Dash Datatable with a dark theme
    
    ```
    dark_table = html.Div(
        dash_table.DataTable(
            columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
            data=df.to_dict("records"),
            editable=True,
            page_size=4,
            filter_action="native",
            sort_action="native",
            style_data_conditional=[
                {
                    "if": {"state": "active"},
                    "border": "1px solid var(--primary)",
                    "opacity": 0.75,
                },
                {"if": {"state": "selected"}, "opacity": 0.75},
            ],
            tooltip_conditional=[
                {
                    "if": {"row_index": "odd"},
                    "type": "markdown",
                    "value": "odd rows have a sample tooltip",
                }
            ],
        ),
        className="dbc_dark",
    )
    ```
    
    The class `dbc_dark` is defined in the assets folder [here](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_dark.css)
    """

"""
=====================================================================
Used in: dcc_components.py
"""

dcc_intro_text = """            
     The `dash-core-components` library is the core set of components included with Dash.  Change the Bootstrap theme in the
      App Design Selections panel to see how these components respond the different Bootstrap themes.  Note: if you work for
       a company, see also Dash Enterprise Design KIt.  

       Most Dash core components (dcc) have a `style` and `className` property that can be used to style the component.  Some 
       components will also inherit the style of the container.  However,  it's not possible to style all parts of 
       the component this way.  For example, there is no way to style the options of a dropdown without using  CSS.  

       If you use Bootstrap, you will see that Dash components look nice with the default BOOTSTRAP theme and 
       most light themes, however,  many elements of the component cannot be updated without CSS and do not 
       automatically respond to changes in themes.  

        This section will show how to style dcc components so they look great with your selected Bootstrap theme. 
          Note this is still a work in progress, so if you have any style tips please open an 
          [issue](https://github.com/AnnMarieW/HelloDash/issues) and  I'll include them here!
           
      - [dash-core-components Overview](https://dash.plotly.com/dash-core-components)
      - [How to add custom CSS to a Dash app](https://dash.plotly.com/external-resources).
"""

dcc_checklist_radio_1 = """
##### Styling dcc.RadioItems and dcc.Checklist
The first row of dcc.Checklist and dcc.RadioItems below shows the default style.
It's also possible to adjust the margins and style of the text label using the `inputStyle, InputClassName, 
labelStyle, labelClassName` parameters. See [this example]( https://community.plotly.com/t/dcc-radioitems-and-label-style/26358/2)
 for how to change the label color in a callback.  Unfortunately, there is no easy way to change the color 
 of the radio and checkbox icons."""

dcc_checklist_radio_2 = """

##### Alternate: `dbc.Checklist and dbc.RadioItems`
Here are the advantages of using `dash-bootstrap-components` dbc.Checklist and dbc.RadioItems:

- The checked boxes and selected radio items of dbc components automatically use the theme's "primary" color. No CSS required!  
See this now by changing the theme in the App Design Selections panel. 
- You can also customize the selected label and icons color in dbc components using `labelCheckedStyle` and `labelCheckedStyle` parameters.
- By default there is nice spacing between the icon and the label, so there is no need to define this manually.
-  The dbc.Checklist can be displayed as toggle switches by setting `switch=True`.  See the dash-boostrap-components gallery for an example.  

Change the theme to see the updated colors.
"""

dcc_tabs = """
##### Styling dcc.Tabs


 If you switch to a dark theme you will see that the default style for dcc.Tabs shown here 
  on the left does not work well. However,
 the dcc.Tabs are very easy to customize using the `style` and `selected_className` parameters.   

- The tabs on the left are the default.  (No CSS or `style` or `className` is applied)

- The tabs on the right are styled so that they work well with both light and dark themes. 
The selected tab is highlighted with the "primary" theme color and the background is transparent. See
the tab labeled "code" to see how it's defined.  
 
"""

dcc_tabs_code = """

dcc.Tab(
    children="tab content"
    label="Tab one",
    selected_className="border-primary text-dark",
    style={"backgroundColor": "transparent", "opacity": 0.6},
    selected_style={"backgroundColor": "transparent"},
),"""


dcc_dropdown = """

##### Styling dcc.Dropdown

The dcc.Dropdown default style works well with many Bootstrap light themes.  However with dark themes, the
font color makes the dropdown options text very hard to read. 

There are only limited ways to style the dropdown using component props. The dropdowns below are styled with CSS.
The ones on the left are styled so the dropdown menu options are visible with with any theme.  The ones on 
the right have a black background and work well with many dark themes.  This CSS can be used as a starting point 
to fine tune the dropdown for your selected theme."""

dcc_dropdown_css = """

```
/* This styles the dropdown menu items so they are visible in both light and dark theme apps */
.VirtualizedSelectOption {
    background-color: white;
    color: black;
}

.VirtualizedSelectFocusedOption {
    background-color: lightgrey;
    color: black;
}
```


This dropdown with the dark background  uses `className="dbc_dark"`  
It's defined in the assets folder [here](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_dark.css)

"""


dcc_input = """

##### Styling dcc.Input

The default Dash input component has a white background.  Even the Bootswatch dark themes have input components 
have a white background.  If you would like to change the input box background or text color, it is necessary
to use custom CSS.  
  
This CSS creates a class that can be used to style specific input boxes.  Use it as a starting point to fine tune 
the input boxes for your selected theme."""

dcc_input_css = """

The dcc.Inputs with the dark background uses `className="dbc_dark_input"`  
It's defined in the assets folder [here](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_dark.css)

"""


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


Note:  This is slider is styled to show the PULSE theme.  If you would like the slider color to be the primary color of any
Bootstrap theme, specify the color like this:   `var(--primary)`
Example:
```
.rc-slider-handle {
  border: 0;
  background-color: var(--primary)
}
```

This slider uses `className="dbc_pulse"`  it's defined in the assets folder [here](https://github.com/AnnMarieW/HelloDash/blob/main/assets/dbc_pulse.css)

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
| `MATCH, ALL, ALLSMALLER`|| Pattern matching callbacks|


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
        @app.callback(
            Output('container', 'children'),
            Output('my_graph', 'figure'),
            Input('btn-1', 'n_clicks'),
        )
        def update(n):
            # ......
            # updates the figure only
            return dash.no_update, fig

```


---
`prevent_initial_call=True`
```
    @app.callback(Output('container', 'children'),
                   Input('btn-1', 'n_clicks'),                   
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
    def display(n_clicks_1, n_clicks_2):
        ctx = dash.callback_context
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if input_id == 'btn-1':
            # do something...
```


---
`Pattern Matching Callbacks`

```
from dash.dependencies import Input, Output, State, MATCH, ALL, ALLSMALLER

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

datatable_pink_css = """

The default table has hot pink accents.  Add the CSS below to the css file in the assets folder to
 will change the pagination buttons and the icons in the column headers.

Note the `var(--primary)` is the "primary" color of the Bootstrap theme.  You can change this to
any other named Bootstrap color, or use a named css color,  or hex, rgb color code.  For example 
`--accent: yellow` !important;'  or `color: #fff !important;`

```
/*
 * Changes the color of the sort arrow and delete icons in the DataTable header
 *  these icons appear when the table is sortable and/or columns are deletable
 */
.dash-table-container .dash-spreadsheet-container .dash-spreadsheet-inner table {
    --accent: var(--primary) !important;
    }


/*
 * Changes the pink color when hovering over the pagination buttons in the DataTable
 */
.last-page:hover, .previous-page:hover, .first-page:hover, .next-page:hover{
  color: var(--primary) !important;
}
```
"""

datatable_filter_data_css = """
In dark themed tables the default black text of the "filter data..." placeholder disappears.
To change the color you can add this to the css file in the assets folder:

```
.dash-spreadsheet .dash-filter input {
            color: var(--white) !important;
         }
```

Or add it in the css parameter in the table definition:

```
css = [{"selector": "input", "rule": f"color: {color}"}],

```

"""


import_basic = """```

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_boostrap_components as dbc

```"""


import_plotly = """```
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

```"""

import_datatable = """```
import data_table
import pandas as pd
import numpy as np
```"""

datasets_code = """

```
    import pandas as pd
    import numpy as np
    import plotly.express as px

    # random numbers
    df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))  


    # ploty express datasets.  See more at 
    #  https://plotly.com/python-api-reference/generated/plotly.data.html#module-plotly.data
    #  
    df = px.data.gapminder()
    df = px.data.iris()
    df = px.data.tips()

    # other hosted datasets
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    # used in the datatable conditional formatting chapter:
    data = dict(
        [
            ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
            ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
            ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
            ("Humidity", [10, 20, 30, 40, 50, 60]),
            ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
        ]
    )
    df = pd.DataFrame(data)
"""

layout_code = """

Layout with Bootstrap stylesheet

```
controls= ....
graph = ...
```

```
app.layout = dbc.Container(
    [
        html.H1("My Title"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(graph, md=8),
            ],
            align="center",
        ),
    ],
    fluid=True,
)
```

---
Layout with Dash default stylesheet

```
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H3('Column 1'),
            controls,
        ], className="four columns"),

        html.Div([
            html.H3('Column 2'),
            graph,
        ], className="eight columns"),
    ], className="row")
])

```"""


basic_callbacks = """```

from dash.dependencies import Input, Output

@app.callback(
    Output("output_id", "children"),
    Input("input_id", "n_clicks")
)
def update_output(n):
    .....
    return .....

```"""

import_advanced_callbacks = """```



```"""

external_stylesheets = """```

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
DASH_DEFAULT = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
BOOTSTRAP = dbc.themes.BOOTSTRAP

external_stylesheets = [BOOTSTRAP, FONT_AWESOME]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



# Note: include font awesome like this:  html.Div(className="fa fa-globe")

```"""

quickstart_dropdown = """```

dropdown = html.Div(
    dcc.Dropdown(
        id="my_dropdown",
         options=[{"label": str(i), "value": i} for i in ["a", "b", "c"],
         value=["a"],
         clearable=False,
         multi=True,
         placeholder="select a"
     )
)

```"""


quickstart_sliders = """```

slider = html.Div(
    dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.5,
        value=10,
        tooltip={"always_visible": True, "placement": "bottom"},
    ),
)

slider_with_marks = html.Div(
    dcc.Slider(
        min=0,
        max=100,
        value=65,
        marks={
            0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
            26: {'label': '26 °C'},
            37: {'label': '37 °C'},
            100: {'label': '100 °C', 'style': {'color': '#f50'}}
        }
    )
)

range_slider = html.Div(
    dcc.RangeSlider(
        # same as slider except value is a list
    )
)

```"""

quickstart_cheklist_radio = """```

radioitems = dbc.FormGroup(
    [
        dbc.Label("Choose one"),
        dbc.RadioItems(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled option", "value": 3, "disabled": True},
            ],
            value=1,
            id="radioitems-input",
        ),
    ]
)

checklist = dbc.FormGroup(
    [
        dbc.Label("Choose a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[],
            id="checklist-input",
        ),
    ]
)

switches = dbc.FormGroup(
    [
        dbc.Label("Toggle a bunch"),
        dbc.Checklist(
            options=[
                {"label": "Option 1", "value": 1},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled Option", "value": 3, "disabled": True},
            ],
            value=[],
            id="switches-input",
            switch=True,
        ),
    ]
)

inputs = html.Div(
    [
        dbc.Form([radioitems, checklist, switches]),
        html.P(id="radioitems-checklist-output"),
    ]
)

```"""


quickstart_button = """
##### Bootstrap dbc.Button.   Dash default see html.Button

```
buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="mr-1"),
        dbc.Button("Secondary", color="secondary", className="mr-1"),
        dbc.Button("Success", color="success", className="mr-1"),
        dbc.Button("Warning", color="warning", className="mr-1"),
        dbc.Button("Danger", color="danger", className="mr-1"),
        dbc.Button("Info", color="info", className="mr-1"),
        dbc.Button("Light", color="light", className="mr-1"),
        dbc.Button("Dark", color="dark", className="mr-1"),
        dbc.Button("Link", color="link"),
    ]
)
```


"""


dash_bootstrap_templates_text = """

## Apply Bootstrap theme to figures with one line of code!

See more info at [dash-bootstrap-templates GitHub](https://github.com/AnnMarieW/dash-bootstrap-templates)

pip install dash-bootstrap-templates
"""

dash_bootstrap_templates_app_text = """
# Demo:
Select the "CYBORG" Bootstrap theme.

Then select either "Use figure templates from dash-bootstrap-templates" or "Use Plotly default figure template.
"""

"""
This is text for the tutorial and help text for the theme_explorer
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
Source code examples in html.components.py
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

# =============================================================================================================

#  Here is another way to format blockquotes.  Put the following in a css file in the assets folder.  Change the
#  border-left color to one that works well with your selected Bootstrap theme.


/* When using Bootstrap, this will add the left border style to blockquotes in dcc.Markdown and html.Blockquote */
blockquote {
  border-left: 4px lightgrey solid;
  padding-left: 1rem;
  margin-top: 2rem;
  margin-bottom: 2rem;
  margin-left: 0rem;
}


"""
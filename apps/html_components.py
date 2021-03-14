"""
This module is imported in the component_gallery.py and demonstrates how to style
Dash html components with standard Bootstrap classnames.
"""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd

HTML_DOCS = "https://dash.plotly.com/dash-html-components"

from app import app


"""
=====================================================================
Change the Bootstrap style details
"""
codebox = {
    "backgroundColor": "transparent",
    "borderStyle": "groove",
    "borderRadius": 15,
    "maxWidth": 900,
    "marginTop": 0,
    "marginBottom": 20,
}

# https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.css
BOOTSTRAP = {
    "primary": "#007bff",
    "secondary": "#6c757d",
    "selected": "rgba(0, 0, 0, 0.075)",
    "font_color": "black",
    "font": "sans-serif",
}


# https://bootswatch.com/4/cerulean/bootstrap.css
SUPERHERO = {
    "primary": "#df691a",
    "secondary": "#4e5d6c",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "white",
    "font": "Lato",
}

# https://bootswatch.com/4/cyborg/bootstrap.css
CYBORG = {
    "primary": "#2a9fd6",
    "secondary": "#555",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "white",
    "font": "Roboto",
}

# https://bootswatch.com/4/cerulean/bootstrap.css
CERULEAN = {
    "primary": "#2fa4e7",
    "secondary": "#e9ecef",
    "selected": "rgba(0, 0, 0, 0.075)",
    "font_color": "black",
    "font": "Segoe UI",
}

# https://bootswatch.com/4/journal/bootstrap.css
JOURNAL = {
    "primary": "#eb6864",
    "secondary": "#aaa",
    "selected": "rgba(255, 255, 255, 0.075)",
    "font_color": "black",
    "font": "Segoe UI",
}
THEMES = {
    "SUPERHERO": SUPERHERO,
    "CYBORG": CYBORG,
    "BOOTSTRAP": BOOTSTRAP,
    "JOURNAL": JOURNAL,
    "CERULEAN": CERULEAN,
}


"""
======================================================================
"""


def make_subheading(label, link):
    return html.H4(
        dcc.Link(label, href=HTML_DOCS + link, target="_blank"),
        style={"textDecoration": "underline"},
        className="mb-2",
    )


html_intro_text = dcc.Markdown(
    """ 
    The `dash-html-components` library has a component for every HTML tag.  All components have a `className`
    parameter, so you can use standard Bootstrap classes.  This makes dash-html-components  compatible with any 
    Bootstrap theme.  You can also customize them with CSS using the `style` property.
    
    All dash-htm-components are automatically styled based on your selected Boostrap theme -- no custom CSS is required!
    See this in action by changing the Bootstrap theme in the App Design Selections panel above.  Notice that the font
    and the colors change according to the theme selected.
    
    - See the  full documentation for [dash-html-components](https://dash.plotly.com/dash-html-components) 
    - Learn more about [Boostrap classes](https://getbootstrap.com/docs/3.4/css/)
    - This is my favorite Bootstrap classes [cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)   
"""
)


typography = dbc.Row(
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
                        "This heading has ",
                        html.Small("some muted text", className="text-muted"),
                    ]
                ),
                html.P(
                    "The lead class in Bootstrap is used to add emphasis to a paragraph.",
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
                        "This is some text",
                        html.A("with an embedded link", href="#"),
                        html.P(" and some more text"),
                    ]
                ),
                html.P(html.Small("This is html.Small - use this for the fine print")),
                html.P(
                    [
                        "The following is rendered in bold text",
                        html.Strong("using html.Strong"),
                    ]
                ),
                html.P(
                    ["The following is rendered in italics ", html.Em("using html.Em")]
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
                html.P("text with className='text-muted'", className="text-muted"),
                html.P("Text with className='text-primary'", className="text-primary"),
                html.P(
                    "Text with className='text-secondary'", className="text-secondary"
                ),
                html.P("Text with className='text-warning'", className="text-warning"),
                html.P("Text with className='text-danger'", className="text-danger"),
                html.P("Text with className='text-success'", className="text-success"),
                html.P("Text with className='text-info'", className="text-info"),
            ],
            className="p-4",
        ),
    ]
)


typograpy_code = html.Div(
    html.Pre(
        html.Code(
            """ 
typography = dbc.Row(
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
                        "This heading has ",
                        html.Small("some muted text", className="text-muted"),
                    ]
                ),
                html.P(
                    "The lead class in Bootstrap is used to add emphasis to a paragraph.",
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
                        "This is some text",
                        html.A("with an embedded link", href="#"),
                        html.P(" and some more text"),
                    ]
                ),
                html.P(html.Small("This is html.Small - use this for the fine print")),
                html.P(
                    [
                        "The following is rendered in bold text",
                        html.Strong("using html.Strong"),
                    ]
                ),
                html.P(
                    ["The following is rendered in italics ", html.Em("using html.Em")]
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
                html.P("text with className='text-muted'", className="text-muted"),
                html.P("Text with className='text-primary'", className="text-primary"),
                html.P(
                    "Text with className='text-secondary'", className="text-secondary"
                ),
                html.P("Text with className='text-warning'", className="text-warning"),
                html.P("Text with className='text-danger'", className="text-danger"),
                html.P("Text with className='text-success'", className="text-success"),
                html.P("Text with className='text-info'", className="text-info"),
            ],
            className="p-4",
        ),
    ]
)
   
""",
        )
    ),
    style=codebox,
    #  className='codebox'
)

more_text = dcc.Markdown(
    """ #### See more information on styling the DataTable in the [Dash Documentation](https://dash.plotly.com/datatable/style). """,
)


layout = dbc.Container(
    [
        dbc.Card(
            [html_intro_text, html.Hr(), typography, typograpy_code],
            className="my-2 p-4",
        ),
    ],
    fluid=True,
)

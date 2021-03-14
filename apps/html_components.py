"""
This module is imported in the component_gallery.py and demonstrates how to style
Dash html components with standard Bootstrap classnames.
"""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from apps import text


HTML_DOCS = "https://dash.plotly.com/dash-html-components"


"""
=====================================================================
Style details
"""
codebox = {
    "backgroundColor": "transparent",
    "borderStyle": "groove",
    "borderRadius": 15,
    "maxWidth": 900,
    "marginTop": 0,
    "marginBottom": 20,
}


"""
=====================================================================
Helper functions
"""


def make_subheading(label, link):
    return html.H4(
        dcc.Link(label, href=HTML_DOCS + link, target="_blank"),
        style={"textDecoration": "underline"},
        className="mb-2",
    )


def make_card(id, content, source_code):
    className_btn = "d-none" if source_code == "" else ""
    return dbc.Card(
        [
            dbc.CardBody(
                [
                    content,
                    dbc.Button(
                        "see code",
                        id={"type": "modal_btn", "index": id},
                        color="secondary",
                        outline=True,
                        size="sm",
                        className=className_btn,
                    ),
                ],
                className="p-2",
            ),
            # Note:  The callback for this modal is in app_gallery.py
            dbc.Modal(
                dbc.ModalBody(source_code),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="lg",
            ),
        ],
        className="mb-4 shadow",
    )


"""
=====================================================================
Content
"""

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
                        html.P(
                            html.Small(
                                "This is html.Small - use this for the fine print"
                            )
                        ),
                        html.P(
                            [
                                "The following is rendered in bold text",
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
                    ],
                    className="p-4",
                ),
            ]
        ),
    ]
)
typography_code = html.Div(html.Pre(html.Code(text.typography_code,)), style=codebox,)


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
                                    "We interrupt this program to annoy you and make things generally more irritating.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    html.Cite(
                                        "Monty Python and the Holy Grail",
                                        title="Source Title",
                                    ),
                                    className="blockquote-footer",
                                ),
                            ],
                            className="blockquote text-left",
                        ),
                    ],
                    className="p-4",
                    width="md-4",
                ),
                dbc.Col(
                    [
                        html.Blockquote(
                            [
                                html.P("Where is the 'any' key?", className="mb-0",),
                                html.Footer(
                                    [
                                        "Homer Simpson ",
                                        html.Cite(
                                            "The Simpson's", title="The Simpson's"
                                        ),
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
                                    "A computer once beat me at chess, but it was no match for me at kick boxing.",
                                    className="mb-0",
                                ),
                                html.Footer(
                                    "Emo Philips ", className="blockquote-footer",
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
blockquotes_code = html.Div(html.Pre(html.Code(text.blockquotes_code,)), style=codebox,)


layout = dbc.Container(
    [
        dbc.Card(
            [
                html_intro_text,
                html.Hr(),
                html.H2(
                    "dash-html-components Overview",
                    className="bg-primary text-white p-2",
                ),
                make_card("typography", typography, typography_code),
                make_card("blockquotes", blockquotes, blockquotes_code),
            ],
            className="my-2 p-4",
        ),
    ],
    fluid=True,
)

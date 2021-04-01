"""
This module is imported in the component_gallery.py and demonstrates how to style
Dash html components with standard Bootstrap classnames.
"""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from apps import text
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/AnnMarieW/HelloDash/main/assets/html.csv"
)


HTML_DOCS = "https://dash.plotly.com/dash-html-components/"


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


def make_links(tags):
    """
    This formats  the list html tags shown in a card
    """
    return ", ".join(
        f"[{tag}]({HTML_DOCS + tag.split('.')[1].lower()})" for tag in tags
    )


def make_btn_with_modal(id, title, content):
    """
     This makes a button that opens a modal for content
     note: The modal callback is located in the app_galery.py

     id:  unique identifier
     title:  what appears on the button
     content:
        To display text, use dcc.Markdown("my text")
        To display a codebox:
          html.Div(html.Pre(html.Code(" enter code here" )), style=codebox,)

    """
    return html.Div(
        [
            dbc.Button(
                title,
                id={"type": "modal_btn", "index": id},
                color="primary",
                size="sm",
                outline=True,
                className="my-2",
            ),
            dbc.Modal(
                dbc.ModalBody(content),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="lg",
            ),
        ]
    )


def make_html_table():
    return dash_table.DataTable(
        columns=[
            {"name": "Component", "id": "Component", "presentation": "markdown"},
            {"name": "Description", "id": "Description"},
        ],
        data=df.to_dict("records"),
        style_table={
            "overflowY": "scroll",
            "border": "thin lightgrey solid",
            "maxHeight": "425px",
        },
        style_cell={"textAlign": "right", "font-family": "arial"},
    )


"""
=====================================================================
Content
"""


typography_text = dcc.Markdown(
    "This shows the use of html.H1 - "
    + make_links(
        [
            "html.H6",
            "html.P",
            "html.Div",
            "html.Small",
            "html.A",
            "html.Strong",
            "html.Em",
            "html.Abbr",
        ]
    )
    + ".  It also shows the use of Boostrap classes to change the text and background color.",
    className="ml-4",
)
typography_card = dbc.Card(
    [
        dbc.CardHeader(html.H2("Typography")),
        dbc.CardBody(
            [
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
                                        html.Small(
                                            "some muted html.Small text",
                                            className="text-muted",
                                        ),
                                    ]
                                ),
                                html.P(
                                    "The className=`lead`adds emphasis to this html.P paragraph.",
                                    className="lead",
                                ),
                            ],
                            className="p-4",
                            lg=4,
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
                            lg=4,
                        ),
                        dbc.Col(
                            [
                                html.H2("Emphasis classes"),
                                html.P(
                                    "text with className='text-muted'",
                                    className="text-muted",
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
                                    "Text with className='text-danger'",
                                    className="text-danger",
                                ),
                                html.P(
                                    "Text with className='text-success'",
                                    className="text-success",
                                ),
                                html.P(
                                    "Text with className='text-info'",
                                    className="text-info",
                                ),
                                html.P(
                                    "Text with className='bg-primary text-white'",
                                    className="bg-primary text-white",
                                ),
                                html.P(
                                    "Text with className='bg-light text-dark'",
                                    className="bg-light text-dark",
                                ),
                                html.P(
                                    "Text with className='bg-dark text-light'",
                                    className="bg-dark text-light",
                                ),
                            ],
                            className="p-4",
                            lg=4,
                        ),
                    ]
                ),
                dbc.Row(typography_text),
                make_btn_with_modal(
                    "typograhy_code",
                    "see code",
                    html.Div(
                        html.Pre(html.Code(text.typography_code,)), style=codebox,
                    ),
                ),
            ]
        ),
    ],
    className="my-2",
)


blockquotes_text = dcc.Markdown(
    "This shows the default Bootstrap style for Blockquotes and the use of "
    + make_links(["html.H2", "html.P", "html.Blockquote", "html.Footer", "html.Cite"])
    + ". It also uses Bootstrap classes to align the text",
    className="ml-4",
)
blockquotes_card = dbc.Card(
    [
        dbc.CardHeader(html.H2("Blockquotes and text alignment")),
        dbc.CardBody(
            [
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
                                        html.P(
                                            "Where is the 'any' key?", className="mb-0",
                                        ),
                                        html.Footer(
                                            [
                                                "Homer Simpson ",
                                                html.Cite(
                                                    "The Simpson's",
                                                    title="The Simpson's",
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
                                            "Emo Philips ",
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
                blockquotes_text,
                dbc.Row(
                    make_btn_with_modal(
                        "blockquotes_code",
                        "see_code",
                        html.Div(
                            html.Pre(html.Code(text.blockquotes_code,)), style=codebox,
                        ),
                    )
                ),
            ]
        ),
    ],
    className="my-2",
)


blockquotes_text2 = dcc.Markdown(
    """
    This shows how to format blockquotes with the left border color, which is a common Blockquote style.  This is done 
    with Bootstrap classes in `className` plus CSS in the `style` parameters. Alternately, you can add custom CSS to the 
    assets folder.  This will format blockquotes when used with the dcc.Markdown component as well. See the code for details,
    """,
    className="ml-4",
)
blockquotes2_card = dbc.Card(
    [
        dbc.CardHeader(html.H4("Blockquotes using className and style parameters")),
        dbc.CardBody(
            [
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
                                    style={
                                        "borderLeft": "solid",
                                        "borderLeftWidth": 15,
                                    },
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
                                            "Martin Golding ",
                                            className="blockquote-footer",
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
                                            "Edward Tufte ",
                                            className="blockquote-footer",
                                        ),
                                    ],
                                    className="blockquote text-left pl-4 border-secondary",
                                    style={
                                        "borderLeft": "solid",
                                        "borderLeftWidth": 10,
                                    },
                                ),
                            ],
                            className="p-4",
                            width="md-4",
                        ),
                    ]
                ),
                blockquotes_text2,
                dbc.Row(
                    make_btn_with_modal(
                        "blockquotes_code2",
                        "see code",
                        html.Div(
                            html.Pre(html.Code(text.blockquotes_code2,)), style=codebox,
                        ),
                    )
                ),
            ]
        ),
    ],
    className="my-2",
)


layout = dbc.Container(
    [
        html.Div(
            [
                dcc.Markdown(text.html_intro_text),
                html.Hr(),
                typography_card,
                blockquotes_card,
                blockquotes2_card,
                html.H5(
                    "Coming Soon:  More examples and a list of all dash-html-components"
                ),
            ],
            className="my-2 p-4",
        ),
    ],
    fluid=True,
)


"""
html.A	Defines a hyperlink
html.Abbr	Defines an abbreviation or an acronym
html.Acronym	Not supported in HTML5. Use html.Abbr instead.  Defines an acronym
html.Address	Defines contact information for the author/owner of a document
html.Area	Defines an area inside an image map
html.Article	Defines an article
html.Aside	Defines content aside from the page content
html.Audio	Defines embedded sound content
html.B	Defines bold text
html.Base	Specifies the base URL/target for all relative URLs in a document
html.Basefont	Not supported in HTML5. Use CSS instead. Specifies a default color, size, and font for all text in a document
html.Bdi	Isolates a part of text that might be formatted in a different direction from other text outside it
html.Bdo	Overrides the current text direction
html.Big	Not supported in HTML5. Use CSS instead. Defines big text
html.Blockquote 	Defines a section that is quoted from another source
html.Br	Defines a single line break
html.Button	Defines a clickable button
html.Canvas	Used to draw graphics, on the fly, via scripting (usually JavaScript)
html.Caption	Defines a table caption
html.Center	Not supported in HTML5. Use CSS instead.Defines centered text
html.Cite	Defines the title of a work
html.Code	Defines a piece of computer code
html.Col	Specifies column properties for each column within a <colgroup> element
html.Colgroup	Specifies a group of one or more columns in a table for formatting
html.Data	Adds a machine-readable translation of a given content
html.Datalist	Specifies a list of pre-defined options for input controls
html.Dd	Defines a description/value of a term in a description list
html.Del	Defines text that has been deleted from a document
html.Details	Defines additional details that the user can view or hide
html.Dfn	Specifies a term that is going to be defined within the content
html.Dialog	Defines a dialog box or window
html.Dir	Not supported in HTML5. Use html.Ul instead. Defines a directory list
html.Div	Defines a section in a document
html.Dl	Defines a description list
html.Dt	Defines a term/name in a description list
html.Em	Defines emphasized text
html.Embeded	Defines a container for an external application
html.Fieldset	Groups related elements in a form
html.Figcaption	Defines a caption for a <figure> element
html.Figure	Specifies self-contained content
html.Font	Not supported in HTML5. Use CSS instead. Defines font, color, and size for text
html.Footer	Defines a footer for a document or section
html.Form	Defines an HTML form for user input
html.Frame	Not supported in HTML5. Defines a window (a frame) in a frameset
html.Framset	Not supported in HTML5. Defines a set of frames
html.H1 to html.H6	Defines HTML headings
html.Header	Defines a header for a document or section
html.Hr	Defines a thematic change in the content
html.I	Defines a part of text in an alternate voice or mood
html.Iframe	Defines an inline frame
html.Img	Defines an image
html.Input	Defines an input control
html.Ins	Defines a text that has been inserted into a document
html.Kbd	Defines keyboard input
html.Label	Defines a label for an <input> element
html.Legent	Defines a caption for a <fieldset> element
html.Li	Defines a list item
html.Link	Defines the relationship between a document and an external resource (most used to link to style sheets)
html.Main	Specifies the main content of a document
html.Map	Defines an image map
html.Mark	Defines marked/highlighted text
html.Meta	Defines metadata about an HTML document
html.Meter	Defines a scalar measurement within a known range (a gauge)
html.Nav	Defines navigation links
html.Noscript	Defines an alternate content for users that do not support client-side scripts
html.ObjectEl	Defines a container for an external application
html.Ol	Defines an ordered list
html.Optgroup	Defines a group of related options in a drop-down list
html.Option	Defines an option in a drop-down list
html.Output	Defines the result of a calculation
html.P	Defines a paragraph
html.Param	Defines a parameter for an object
html.Picture	Defines a container for multiple image resources
html.Pre	Defines preformatted text
html.Progress	Represents the progress of a task
html.Q	Defines a short quotation
html.Rp	Defines what to show in browsers that do not support ruby annotations
html.Rt	Defines an explanation/pronunciation of characters (for East Asian typography)
html.Ruby	Defines a ruby annotation (for East Asian typography)
html.S	Defines text that is no longer correct
html.Samp	Defines sample output from a computer program
html.Script	Defines a client-side script
html.Section	Defines a section in a document
html.Select	Defines a drop-down list
html.Small	Defines smaller text
html.Source	Defines multiple media resources for media elements (<video> and <audio>)
html.Span	Defines a section in a document
html.Strike	Not supported in HTML5. Use <del> or <s> instead. Defines strikethrough text
html.Strong	Defines important text
html.Sub	Defines subscripted text
html.Summary	Defines a visible heading for a <details> element
html.Sup	Defines superscripted text
html.Svg	Defines a container for SVG graphics
html.Table	Defines a table
html.Tbody	Groups the body content in a table
html.Td	Defines a cell in a table
html.Template	Defines a container for content that should be hidden when the page loads
html.Textarea	Defines a multiline input control (text area)
html.Tfoot	Groups the footer content in a table
html.Th	Defines a header cell in a table
html.Thead	Groups the header content in a table
html.Time	Defines a specific time (or datetime)
html.Title	Defines a title for the document
html.Tr	Defines a row in a table
html.Track	Defines text tracks for media elements (<video> and <audio>)
html.U	Defines some text that is unarticulated and styled differently from normal text
html.Ul	Defines an unordered list
html.var	Defines a variable
html.Video	Defines embedded video content
html.Wbr	Defines a possible line-break
"""

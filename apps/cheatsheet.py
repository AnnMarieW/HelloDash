"""
This app creates the  cheatsheets and how-to card with links and modals.

To maintain:  add extended text and code snippets to text.py
              add complete apps to the gallery

              add links or new cards in the Add Topics section
              add the card to the layout on this page or any other page

"""


import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps import text
from util import header
import pathlib


# set relative path for reading code files
PATH = pathlib.Path(__file__).parent
GALLERY_PATH = PATH.joinpath("../gallery").resolve()


"""
=====================================================================
Helper functions 
"""


def make_link(title, link):
    """
    This makes an external link in a listgroup
    """
    return dbc.ListGroupItem(title, href=link, target="_blank")


def make_link_with_modal(title, content):
    """
     This makes a link that opens a modal for content
     note: The modal callback is located in the app_galery.py
     content example:
        To display text, use dcc.Markdown("my text")
        To display a codebox:
          html.Div(html.Pre(html.Code(" enter code here" )), style=codebox,)

    """
    return dbc.ListGroupItem(
        [
            dbc.Button(
                title,
                id={"type": "modal_btn", "index": title},
                color="link",
                className="text-left pl-0",
            ),
            dbc.Modal(
                dbc.ModalBody(content),
                id={"type": "modal", "index": title},
                scrollable=True,
                size="lg",
            ),
        ]
    )


def make_button_with_popover(title, content, link=""):
    """
    This makes a button that shows content on hover. Primary use is quickstart apps
    and code examples
    """
    id = title.replace(" ", "")
    return html.Div(
        [
            dbc.Button(title, id=id, color="link", className="text-left ", block=True,),
            dbc.Popover(
                [
                    dbc.PopoverHeader(dcc.Link(title, href=link, target="_blank")),
                    dbc.PopoverBody(content, style={"padding": 30}),
                ],
                id="popover" + id,
                target=id,
                trigger="legacy",
                className="shadow-lg",
                placement="right-start"
                #  placement="top"
            ),
        ],
    )


def get_code_file(filename):
    """
    :param filename: (str) file name of python file in the gallery directory
    :return: a string to display the code with highlighting in dcc.Markdown(code)

    Note: be sure to include a blank line and docstring at start of source file so highlighting
      works correctly
    """
    with open(GALLERY_PATH.joinpath(filename)) as f:
        code = f.read()
    return f"```{code}```"


"""
=====================================================================
Add Topics  here
"""

dash_links = dbc.Card(
    [
        dbc.CardHeader(html.H4("Dash")),
        dbc.ListGroup(
            [
                make_link("Dash Documentation", "https://dash.plotly.com/"),
                make_link(
                    "dash-core-components",
                    "https://dash.plotly.com/dash-core-components",
                ),
                make_link("DataTable", "https://dash.plotly.com/datatable"),
                make_link(
                    "DashTable Reference",
                    "https://dash.plotly.com/datatable/reference",
                ),
                make_link("Dash DAQ components", "https://dash.plotly.com/dash-daq"),
                make_link(
                    "Dash Community Forum", "https://community.plotly.com/c/dash/16"
                ),
            ]
        ),
    ],
    className="m-1",
)


bootstrap_links = dbc.Card(
    [
        dbc.CardHeader(html.H4("Bootstrap")),
        dbc.ListGroup(
            [
                make_link(
                    "dash-bootstrap-components Documentation",
                    "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/",
                ),
                make_link(
                    "Bootstrap Cheatsheet",
                    "https://hackerthemes.com/bootstrap-cheatsheet/",
                ),
                make_link(
                    "Bootstrap Bootswatch Themes",
                    "https://www.bootstrapcdn.com/bootswatch/",
                ),
            ]
        ),
    ],
    className="m-1",
)


about_links = dbc.Card(
    [
        dbc.CardHeader(html.H4("About")),
        dbc.ListGroup(
            [
                make_link(
                    "GitHub:  Theme Explorer", "https://github.com/AnnMarieW/HelloDash",
                ),
            ]
        ),
    ],
    className="m-1",
)


plotly_links = dbc.Card(
    [
        dbc.CardHeader(html.H4("Plotly")),
        dbc.ListGroup(
            [
                make_link(
                    "Plotly discrete colors",
                    "https://plotly.com/python/discrete-color/",
                ),
                make_link(
                    "Plotly continuous colorscales",
                    "https://plotly.com/python/builtin-colorscales/",
                ),
                make_link(
                    "Plotly templates and themes",
                    "https://plotly.com/python/templates/",
                ),
                make_link(
                    "Plotly Figure Reference",
                    "https://plotly.com/python/reference/index/",
                ),
                make_link(
                    "Plotly Figure Structure Tutorial",
                    "https://plotly.com/python/figure-structure/",
                ),
                make_link(
                    "Plotly Express Overview",
                    "https://plotly.com/python/plotly-express/",
                ),
                make_link(
                    "Plotly Express Reference",
                    "https://plotly.com/python-api-reference/plotly.express.html",
                ),
            ]
        ),
    ],
    className="m-1",
)

getting_started_links = dbc.Card(
    [
        dbc.CardHeader(html.H4("Getting Started")),
        dbc.ListGroup(
            [
                make_link(
                    "Dash Bootstrap video by Charming Data",
                    "https://www.youtube.com/watch?v=0mfIK8zxUds",
                ),
                make_link(
                    "See quickstart apps and layout templates in the App Gallery",
                    "/app_gallery",
                ),
                make_link(
                    "Getting started with HTML",
                    "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started",
                ),
                make_link(
                    "Learn CSS", "https://developer.mozilla.org/en-US/docs/Learn/CSS",
                ),
                make_link(
                    "Browser developer tools",
                    "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools",
                ),
                make_link(
                    "10 minutes to Pandas",
                    "https://pandas.pydata.org/pandas-docs/dev/user_guide/10min.html",
                ),
            ]
        ),
    ],
    className="m-1",
)


how_to_datatable = dbc.Card(
    [
        dbc.CardHeader(html.H4("How To: DataTable")),
        dbc.ListGroup(
            [
                make_link_with_modal(
                    "How change the hotpink color of icons in the header and pagination buttons",
                    dcc.Markdown(text.datatable_pink_css),
                ),
                make_link_with_modal(
                    "How change color of the `filter data...` text in the header",
                    dcc.Markdown(text.datatable_filter_data_css),
                ),
                make_link_with_modal(
                    "How to add thumbail images to table",
                    dcc.Markdown(get_code_file("image_in_table.py")),
                ),
                make_link(
                    "How to do fix table where data is cut off at the edges",
                    "https://dash-bootstrap-components.opensource.faculty.ai/docs/faq/",
                ),
                make_link_with_modal(
                    "How to fix dropdown options that don't appear",
                    dcc.Markdown(
                        """ Add this to the css in the assets folder:
                        ```
                        .Select-menu-outer {
                            display: block !important;
                        }
                        ```                        
                        """
                    ),
                ),
                make_link_with_modal(
                    "How to move the Export and Toggle Columns button",
                    html.Div(
                        html.Pre(html.Code(text.datatable_move_export_btn)),
                        className="codebox",
                    ),
                ),
                make_link(
                    "How to format numbers in a DataTable",
                    "https://formattable.pythonanywhere.com/",
                ),
                make_link(
                    "How to add sparkline to a DataTable",
                    "https://community.plotly.com/t/sparklines-as-fonts-embedding-minimal-sparklines-in-tables-components/39468",
                ),
                make_link(
                    "How to make a cell act like a button in a  DataTable",
                    "https://community.plotly.com/t/button-inside-a-dash-table/51460",
                ),
                make_link(
                    "How to make columns editable after pasting new data into a table",
                    "https://community.plotly.com/t/copy-and-paste-with-data-table-restricting-new-rows-and-columns/35758/5",
                ),
            ]
        ),
    ],
    className="m-1",
)

how_to_general = dbc.Card(
    [
        dbc.CardHeader(html.H4("How to: General")),
        dbc.ListGroup(
            [
                make_link(
                    "How to add custom CSS to a Dash app",
                    "https://dash.plotly.com/external-resources",
                ),
                make_link(
                    "How to make a round button with an icon",
                    "https://community.plotly.com/t/formatting-in-dash/51197/3",
                ),
                make_link(
                    "How to make a card with an image to the left or right",
                    "https://community.plotly.com/t/how-to-create-card-with-icon-on-the-right/51832/3",
                ),
                make_link_with_modal(
                    "How to make blockquotes in markdown text have a colored left border",
                    dcc.Markdown(
                        "Click on the HTML Components tab to see the answer with examples."
                    ),
                ),
                make_link_with_modal(
                    "How to style a text table in markdown",
                    html.Div(
                        html.Pre(html.Code(text.datatable_markdown)),
                        className="codebox",
                    ),
                ),
                make_link(
                    "How to do pattern matching callback",
                    "https://community.plotly.com/t/pattern-call-backs-regarding-adding-dynamic-graphs/40724",
                ),
                make_link_with_modal(
                    "How to deploy your app on PythonAnywhere",
                    dcc.Markdown(text.pythonanywhere_quickstart),
                ),
                make_link(
                    "How to deploy your app on Heroku",
                    "https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723",
                ),
                make_link(
                    "How to add your dash app to Flask",
                    "https://community.plotly.com/t/how-to-add-your-dash-app-to-flask/51870",
                ),
            ]
        ),
    ],
    className="m-1",
)


quickstart_code = dbc.Card(
    [
        dbc.CardHeader(html.H4("App Quickstart")),
        dbc.ListGroup(
            [
                make_button_with_popover(
                    "Bootstrap quickstart app - two graphs side by side",
                    dcc.Markdown(get_code_file("quickstart1.py")),
                ),
                make_button_with_popover(
                    "Bootstrap quickstart app - DataTable with callback",
                    dcc.Markdown(get_code_file("quickstart2.py")),
                ),
                make_button_with_popover(
                    "Basic imports", dcc.Markdown(text.import_basic)
                ),
                make_button_with_popover(
                    "Graphing imports", dcc.Markdown(text.import_plotly)
                ),
                make_button_with_popover(
                    "DataTable imports", dcc.Markdown(text.import_datatable)
                ),
                make_button_with_popover("Datasets", dcc.Markdown(text.datasets_code)),
                make_button_with_popover(
                    "External stylesheets", dcc.Markdown(text.external_stylesheets)
                ),
                make_button_with_popover("Layout", dcc.Markdown(text.layout_code)),
                make_button_with_popover(
                    "Basic Callbacks", dcc.Markdown(text.basic_callbacks)
                ),
                make_button_with_popover(
                    "Advanced Callback Cheatsheet",
                    dcc.Markdown(text.cheatsheet_advanced_callback),
                ),
            ],
        ),
    ],
    className="m-1 mt-4",
)

quickstart_components = dbc.Card(
    [
        dbc.CardHeader(html.H4("App Quickstart - Most common components")),
        dbc.ListGroup(
            [
                make_button_with_popover(
                    "Dropdown", dcc.Markdown(text.quickstart_dropdown),
                ),
                make_button_with_popover(
                    "Bootstrap Button", dcc.Markdown(text.quickstart_button),
                ),
                make_button_with_popover(
                    "Sliders", dcc.Markdown(text.quickstart_sliders)
                ),
                make_button_with_popover(
                    "Checklists and RadioItems with labels",
                    dcc.Markdown(text.quickstart_cheklist_radio),
                ),
                make_button_with_popover(
                    "DataTable", dcc.Markdown(text.datatable_light_code)
                ),
            ],
        ),
    ],
    className="m-1 mt-4",
)


"""
=====================================================================
Add card name to the Layout for the cheatsheet page here
"""

layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(bootstrap_links, md=4),
                dbc.Col(dash_links, md=4),
                dbc.Col(plotly_links, md=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(getting_started_links, md=4),
                dbc.Col(how_to_general, md=4),
                dbc.Col(how_to_datatable, md=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(quickstart_code, md=4),
                # dbc.Col(quickstart_components, md=4),
                # dbc.Col(about_links, md=4),
            ]
        ),
        dbc.Row(
            [
                #  dbc.Col(quickstart_code, md=4),
                dbc.Col(quickstart_components, md=4),
                # dbc.Col(about_links, md=4),
            ]
        ),
        dbc.Row(
            [
                #  dbc.Col(quickstart_code, md=4),
                # dbc.Col(quickstart_components, md=4),
                dbc.Col(about_links, md=4),
            ]
        ),
        html.Div(style={"height": 2000}),
    ],
    fluid=True,
)

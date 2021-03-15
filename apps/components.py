"""
This module is imported in the component_gallery.py and shows all of the dbc components available
"""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

DBC_HOME = "https://dash-bootstrap-components.opensource.faculty.ai/"
DBC_GITHUB = "https://github.com/facultyai/dash-bootstrap-components"
DBC_DOCS = "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/"


from app import app

about = """
This app is part of a multi page app adapted from an [example app](https://github.com/facultyai/dash-bootstrap-components/blob/main/examples/components.py)
 in the dash-bootstrap-components github repo.  It is a gallery of all of the components available in the dbc library.
"""


header = dcc.Markdown(
    """  
    `dash-bootstrap-components` is a library of Bootstrap components for Plotly Dash that makes it easier to build 
    consistently styled apps with complex, responsive layouts. It's provided open source by Faculty AI - see the 
    full documentation [here](https://dash-bootstrap-components.opensource.faculty.ai/).  Click on the link with the 
    component name to go directly to the component's docs for more great examples.  
    
    All dash-boostrap-components are automatically styled based on your selected Boostrap theme -- no custom CSS is required!
    See this in action by changing the Bootstrap theme in the App Design Selections panel above.  See an overview
    of Boostrap themes available with dbc components [here](https://www.bootstrapcdn.com/bootswatch/)
    
      
     
    Note that most of the other Dash components (such as `dash-core-components`, `DataTable` and `DAQ` components) and 
    Plotly figures do not automatically respond to changes to Bootstrap themes.  See more information on how to style
    these components in each section.
"""
)


def make_subheading(label, link):
    return html.H4(
        dcc.Link(label, href=DBC_DOCS + link, target="_blank"),
        style={"textDecoration": "underline"},
        className="mb-2",
    )


alerts1 = html.Div(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a secondary alert", color="secondary"),
        dbc.Alert("This is a success alert! Well done!", color="success"),
        dbc.Alert("This is a warning alert... be careful...", color="warning"),
    ]
)
alerts2 = html.Div(
    [
        dbc.Alert("This is a danger alert. Scary!", color="danger"),
        dbc.Alert("This is an info alert. Good to know!", color="info"),
        dbc.Alert("This is a light alert", color="light"),
        dbc.Alert("This is a dark alert", color="dark"),
    ]
)

alerts = html.Div(
    [
        make_subheading("Alerts", "alert/"),
        dbc.Row([dbc.Col(alerts1), dbc.Col(alerts2)]),
    ]
)

badge_colors = html.Span(
    [
        dbc.Badge("Primary", color="primary", className="mr-1"),
        dbc.Badge("Secondary", color="secondary", className="mr-1"),
        dbc.Badge("Success", color="success", className="mr-1"),
        dbc.Badge("Warning", color="warning", className="mr-1"),
        dbc.Badge("Danger", color="danger", className="mr-1"),
        dbc.Badge("Info", color="info", className="mr-1"),
        dbc.Badge("Light", color="light", className="mr-1"),
        dbc.Badge("Dark", color="dark"),
    ],
)

badges = html.Div(
    [
        make_subheading("Badges", "badge/"),
        html.Div(
            [
                badge_colors,
                html.Br(),
                dbc.Button(
                    ["Notifications", dbc.Badge("4", color="light", className="ml-1")],
                    color="primary",
                    className="mt-2",
                ),
            ]
        ),
    ]
)

buttons1 = html.Div(
    [
        make_subheading("Buttons", "button/"),
        html.Div(
            [
                dbc.Button("Primary", color="primary", className="mr-1"),
                dbc.Button("Secondary", color="secondary", className="mr-1"),
                dbc.Button("Success", color="success", className="mr-1"),
                dbc.Button("Warning", color="warning", className="mr-1"),
                dbc.Button("Danger", color="danger", className="mr-1"),
                dbc.Button("Info", color="info"),
            ]
        ),
        html.Div(
            [
                dbc.Button("Primary", outline=True, color="primary", className="mr-1"),
                dbc.Button(
                    "Secondary", outline=True, color="secondary", className="mr-1",
                ),
                dbc.Button("Success", outline=True, color="success", className="mr-1"),
                dbc.Button("Warning", outline=True, color="warning", className="mr-1"),
                dbc.Button("Danger", outline=True, color="danger", className="mr-1"),
                dbc.Button("Info", outline=True, color="info"),
            ],
            className="my-2",
        ),
        html.Div(
            [
                dbc.Button("Regular", color="primary", className="mr-1"),
                dbc.Button("Active", color="primary", active=True, className="mr-1"),
                dbc.Button(
                    "Disabled", color="primary", disabled=True, className="mr-1"
                ),
                dbc.Button("Large button", size="lg", className="mr-1"),
                dbc.Button("Regular button", className="mr-1"),
                dbc.Button("Small button", size="sm"),
            ]
        ),
    ]
)


buttons2 = html.Div(
    [
        make_subheading("Button Groups", "buttongroups/"),
        html.Div(
            [
                dbc.ButtonGroup(
                    [
                        dbc.Button("Primary", color="primary"),
                        dbc.Button("Secondary", color="secondary"),
                        dbc.Button("Success", color="success"),
                        dbc.Button("Warning", color="warning"),
                        dbc.Button("Danger", color="danger"),
                        dbc.Button("Info", color="info"),
                    ]
                ),
                html.Br(),
                dbc.ButtonGroup(
                    [
                        dbc.Button("First"),
                        dbc.Button("Second"),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Item 1"),
                                dbc.DropdownMenuItem("Item 2"),
                            ],
                            label="Dropdown",
                            group=True,
                        ),
                    ],
                    vertical=True,
                ),
            ],
        ),
    ]
)
buttons = dbc.Row([dbc.Col(buttons1), dbc.Col(buttons2)])


cards = html.Div(
    [
        make_subheading("Cards", "card/"),
        dbc.CardDeck(
            [
                dbc.Card(
                    [
                        dbc.CardHeader("Header"),
                        dbc.CardBody(
                            [
                                html.H5(
                                    "This card has a title", className="card-title",
                                ),
                                html.P("And some text", className="card-text"),
                            ]
                        ),
                    ]
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H5(
                                    "This card has a title", className="card-title",
                                ),
                                html.P(
                                    "and some text, but no header",
                                    className="card-text",
                                ),
                            ]
                        )
                    ],
                    outline=True,
                    color="primary",
                ),
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H5(
                                    "This card has a title", className="card-title",
                                ),
                                html.P(
                                    "and some text, and a footer!",
                                    className="card-text",
                                ),
                            ]
                        ),
                        dbc.CardFooter("Footer"),
                    ],
                    outline=True,
                    color="dark",
                ),
            ]
        ),
    ]
)

collapse = html.Div(
    [
        make_subheading("Collapse", "collapse/"),
        dbc.Button(
            "Open collapse", id="collapse-button", style={"marginBottom": "1rem"},
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
            id="collapse",
        ),
    ]
)

columns = html.Div(
    [
        make_subheading("Columns", "layout/"),
        html.Div(
            [
                dbc.Row(
                    dbc.Col(html.H4("A single column"), className="border bg-light")
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H4(
                                "One of three columns", className="border bg-light"
                            ),
                        ),
                        dbc.Col(
                            html.H4(
                                "One of three columns", className="border bg-light"
                            ),
                        ),
                        dbc.Col(
                            html.H4(
                                "One of three columns", className="border bg-light"
                            ),
                        ),
                    ]
                ),
            ]
        ),
        html.Hr(),
        html.H4("Row with no gutters"),
        dbc.Row(
            [
                dbc.Col(html.H4("Column 1  md=3", className="border bg-light"), md=3,),
                dbc.Col(html.H4("Column 2  md=6", className="border bg-light"), md=6,),
                dbc.Col(html.H4("column 3  md=3", className="border bg-light"), md=3,),
            ],
            no_gutters=True,
        ),
    ]
)

dropdownmenu = html.Div(
    [
        make_subheading("DropdownMenu", "dropdown_menu/"),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("Heading", header=True),
                dbc.DropdownMenuItem("Item 1", href=DBC_GITHUB),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Another heading", header=True),
                dbc.DropdownMenuItem("Item 2"),
            ],
            label="Open DropdownMenu",
        ),
    ]
)

fade = html.Div(
    [
        make_subheading("Fade", "fade/"),
        dbc.Button("Toggle fade", id="fade-button", style={"marginBottom": "1rem"}),
        dbc.Fade(
            dbc.Card(
                dbc.CardBody(
                    html.P("This content fades in and out", className="card-text")
                )
            ),
            id="fade",
            is_in=True,
        ),
    ]
)

# ---------  start forms row ------------------
form = html.Div(
    [
        make_subheading("Form", "form/"),
        dbc.Form(
            [
                dbc.FormGroup(
                    [
                        dbc.Label("Username"),
                        dbc.Input(placeholder="Enter your username", type="text"),
                        dbc.FormText(
                            [
                                "Can't remember your username? ",
                                html.A(
                                    "Click here.",
                                    href="#",
                                    className="text-muted",
                                    style={"textDecoration": "underline"},
                                ),
                            ]
                        ),
                    ]
                ),
                dbc.FormGroup(
                    [
                        dbc.Label("Username"),
                        dbc.Input(placeholder="Enter your password", type="password"),
                        dbc.FormText(
                            [
                                "Can't remember your password? ",
                                html.A(
                                    "Click here.",
                                    href="#",
                                    className="text-muted",
                                    style={"textDecoration": "underline"},
                                ),
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ]
)

input_ = html.Div(
    [
        make_subheading("Input", "input/"),
        dbc.FormGroup([dbc.Label("Text input"), dbc.Input(type="text")]),
        dbc.FormGroup(
            [
                dbc.Label("Valid text input"),
                dbc.Input(type="text", valid=True),
                dbc.FormFeedback("That's a valid input!", valid=True),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Invalid text input"),
                dbc.Input(type="text", invalid=True),
                dbc.FormFeedback("That's an invalid input..."),
            ]
        ),
    ]
)

checklist_items = html.Div(
    [
        make_subheading("Checklist", "input/"),
        dbc.Checklist(
            options=[{"label": "Option {}".format(i), "value": i} for i in range(3)],
            value=[],
        ),
        html.H5("Inline checklist", className="mt-3"),
        dbc.Checklist(
            options=[{"label": "Option {}".format(i), "value": i} for i in range(5)],
            value=[],
            inline=True,
        ),
    ]
)

radio_items = html.Div(
    [
        make_subheading("RadioItems", "input/"),
        dbc.RadioItems(
            options=[{"label": "Option {}".format(i), "value": i} for i in range(3)],
            value=0,
        ),
        html.H5("Inline radioitems", className="mt-3"),
        dbc.RadioItems(
            options=[{"label": "Option {}".format(i), "value": i} for i in range(5)],
            value=0,
            inline=True,
        ),
    ]
)

input_group = html.Div(
    [
        make_subheading("Input groups and addons", "input_group/"),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon(
                    dbc.Button("To the left!", color="danger"), addon_type="prepend",
                ),
                dbc.Input(type="text"),
            ]
        ),
        html.Br(),
        dbc.InputGroup(
            [
                dbc.Input(type="text"),
                dbc.InputGroupAddon(
                    dbc.Button("To the right!", color="success"), addon_type="append",
                ),
            ]
        ),
        html.Br(),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("@", addon_type="prepend"),
                dbc.Input(type="text", placeholder="Enter username"),
            ]
        ),
    ]
)


# ----- end forms row  --------------------------------------------

jumbotron = html.Div(
    [
        make_subheading("Jumbotron", "jumbotron/"),
        dbc.Jumbotron(
            [
                html.H2("This is a jumbotron"),
                html.P("It makes things big..."),
                dbc.Button("Click here", color="danger"),
            ]
        ),
    ]
)

list_group = html.Div(
    [
        make_subheading("ListGroup", "list_group/"),
        dbc.ListGroup(
            [
                dbc.ListGroupItem("Item 1", color="primary", action=True),
                dbc.ListGroupItem("Item 2"),
                dbc.ListGroupItem("Item 3"),
                dbc.ListGroupItem(
                    [
                        dbc.ListGroupItemHeading("Item 4 heading"),
                        dbc.ListGroupItemText("Item 4 text"),
                    ]
                ),
            ]
        ),
    ]
)


COOKIE = (
    "https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png"
)
modal = html.Div(
    [
        make_subheading("Modal", "modal/"),
        html.P(
            [
                dbc.Button("Show the cookie monster", id="button"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("Cookies!"),
                        dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                    ],
                    id="modal",
                    is_open=False,
                ),
            ]
        ),
    ]
)

navbar = html.Div(
    [
        make_subheading("Navbar", "navbar/"),
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("GitHub", href=DBC_GITHUB)),
                dbc.DropdownMenu(
                    nav=True,
                    in_navbar=True,
                    label="Menu",
                    children=[
                        dbc.DropdownMenuItem("Entry 1", href="https://google.com"),
                        dbc.DropdownMenuItem("Entry 2", href="/test"),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem("A heading", header=True),
                        dbc.DropdownMenuItem(
                            "Entry 3", href="/external-relative", external_link=True
                        ),
                        dbc.DropdownMenuItem("Entry 4 - does nothing"),
                    ],
                ),
            ],
            brand="Dash Bootstrap Components",
            brand_href=DBC_HOME,
            sticky="top",
            color="primary",
            dark=True,
        ),
    ]
)

popover = html.Div(
    [
        make_subheading("Popover", "popover/"),
        dbc.Button("Click to toggle popover", id="popover-target", color="danger"),
        dbc.Popover(
            [dbc.PopoverHeader("Popover header"), dbc.PopoverBody("Popover body"),],
            id="popover",
            is_open=False,
            target="popover-target",
        ),
    ]
)

progress = html.Div(
    [
        make_subheading("Progress", "progress/"),
        dbc.Progress("25%", value=25),
        dbc.Progress(value=50, striped=True, className="my-2"),
        dbc.Progress(value=75, color="success"),
    ]
)

spinner = html.Div(
    [
        make_subheading("Spinner", "spinner/"),
        html.P(),
        html.Div(
            [
                dbc.Spinner(color="secondary"),
                dbc.Spinner(color="danger", type="grow"),
                dbc.Spinner(color="light", type="grow"),
                dbc.Button(
                    [dbc.Spinner(size="sm"), " Loading..."],
                    color="primary",
                    disabled=True,
                ),
            ]
        ),
    ]
)


table = html.Div(
    [
        make_subheading("HTML Table", "table/"),
        dbc.Table(
            [
                html.Thead(
                    html.Tr(
                        [html.Th("#"), html.Th("First name"), html.Th("Last name"),]
                    )
                ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th("1", scope="row"),
                                html.Td("Tom"),
                                html.Td("Cruise"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("2", scope="row"),
                                html.Td("Jodie"),
                                html.Td("Foster"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th("3", scope="row"),
                                html.Td("Chadwick"),
                                html.Td("Boseman"),
                            ]
                        ),
                    ]
                ),
            ],
            responsive=True,
            striped=True,
            hover=True,
        ),
    ]
)

tabs = html.Div(
    [
        make_subheading("Tabs", "tabs/"),
        dbc.Tabs(
            [
                dbc.Tab(
                    html.H4("This is tab 1"), label="Tab 1", style={"padding": "10px"},
                ),
                dbc.Tab(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.P("This tab has a card!", className="card-text",),
                                dbc.Button("Click here", color="success"),
                            ]
                        )
                    ),
                    label="Tab 2",
                    style={"padding": "10px"},
                ),
            ]
        ),
    ]
)

toast = html.Div(
    [
        make_subheading("Toast", "toast/"),
        dbc.Button(
            "Open toast", id="auto-toast-toggle", color="primary", className="mb-3",
        ),
        dbc.Toast(
            [html.P("This is the content of the toast", className="mb-0")],
            id="auto-toast",
            header="This is the header",
            icon="primary",
            duration=4000,
        ),
    ],
    className="my-2",
)

tooltip = html.Div(
    [
        make_subheading("Tooltip", "tooltip/"),
        html.P(
            [
                "I wonder what ",
                html.Span("floccinaucinihilipilification", id="tooltip-target"),
                " means?",
            ]
        ),
        dbc.Tooltip(
            "Noun: rare, " "the action or habit of estimating something as worthless.",
            target="tooltip-target",
        ),
    ]
)

source_code = dcc.Markdown(
    """
    ## See the [source code](https://github.com/AnnMarieW/HelloDash/blob/main/apps/components.py)       
    """
)


layout = dbc.Container(
    [
        dbc.Card(
            [
                header,
                html.Hr(),

                alerts,
                html.Hr(),
                badges,
                html.Hr(),
                buttons,
                html.Hr(),
                dropdownmenu,
                html.Hr(),
                tabs,
                html.Hr(),
                cards,
                html.Hr(),
                dbc.Row([dbc.Col([form, input_group,]), dbc.Col([input_])]),
                html.Hr(),
                dbc.Row([dbc.Col([checklist_items]), dbc.Col([radio_items])]),
                html.Hr(),
                navbar,
                html.Hr(),
                jumbotron,
                html.Hr(),
                columns,
                html.Hr(),
                list_group,
                html.Hr(),
                table,
                html.Hr(),
                dbc.Row([dbc.Col([progress]), dbc.Col([spinner])]),
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col([modal, fade, collapse,]),
                        dbc.Col([popover, toast, tooltip]),
                    ]
                ),
                html.Hr(),
                html.Div(style={"height": "50px"}),
                source_code,
            ],
            className="my-2 p-4",
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("fade", "is_in"),
    [Input("fade-button", "n_clicks")],
    [State("fade", "is_in")],
)
def toggle_fade(n, is_in):
    if n:
        return not is_in
    return is_in


@app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("modal", "is_open"),
    [Input("button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(Output("auto-toast", "is_open"), [Input("auto-toast-toggle", "n_clicks")])
def open_toast(n):
    return True

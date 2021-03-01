import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

DBC_HOME = "https://dash-bootstrap-components.opensource.faculty.ai/"
DBC_GITHUB = "https://github.com/facultyai/dash-bootstrap-components"
DBC_DOCS = "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/"


from app import app

header = html.Div(
    [
        html.H3(
            [
                "Here are the components available in ",
                html.Code("dash-bootstrap-components"),
            ]
        )
    ],
)


alerts1 = html.Div(
    [
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Alert("This is a danger alert", color="danger"),
    ],
)
alerts2 = html.Div(
    [
        dbc.Alert("This is a secondary alert.", color="secondary"),
        dbc.Alert("This is an info alert.", color="info"),
    ],
)
alerts3 = html.Div(
    [
        dbc.Alert("This is a success alert", color="success"),
        dbc.Alert("This is a light alert", color="light"),
    ],
)
alerts4 = html.Div(
    [
        dbc.Alert("This is a warning alert. Scary!", color="warning"),
        dbc.Alert("This is a dark alert", color="dark"),
    ],
)

alerts = html.Div(
    [
        html.H2(dcc.Link("Alerts", href=DBC_DOCS + "alert/", target="_blank")),
        dbc.Row(
            [dbc.Col(alerts1), dbc.Col(alerts2), dbc.Col(alerts3), dbc.Col(alerts4)]
        ),
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
        html.H2(dcc.Link("Badges", href=DBC_DOCS + "badge/", target="_blank")),
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

buttons = html.Div(
    [
        html.H2(dcc.Link("Buttons", href=DBC_DOCS + "button/", target="_blank")),
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
        html.Br(),
        html.H4("Outline buttons"),
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
            ]
        ),
        html.Br(),
        html.H4("Button group"),
        html.Div(
            dbc.ButtonGroup(
                [
                    dbc.Button("Primary", color="primary"),
                    dbc.Button("Secondary", color="secondary"),
                    dbc.Button("Success", color="success"),
                    dbc.Button("Warning", color="warning"),
                    dbc.Button("Danger", color="danger"),
                    dbc.Button("Info", color="info"),
                ]
            )
        ),
    ]
)

cards = html.Div(
    [
        html.H2(dcc.Link("Cards", href=DBC_DOCS + "card/", target="_blank")),
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
        html.H2(dcc.Link("Collapse", href=DBC_DOCS + "collapse/", target="_blank")),
        dbc.Button(
            "Open collapse", id="collapse-button", style={"margin-bottom": "1rem"},
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
            id="collapse",
        ),
    ]
)

columns = html.Div(
    [
        html.H2(dcc.Link("Columns", href=DBC_DOCS + "layout/", target="_blank")),
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
        html.H2(
            dcc.Link("DropdownMenu", href=DBC_DOCS + "dropdown_menu/", target="_blank")
        ),
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
        html.H2(dcc.Link("Fade", href=DBC_DOCS + "fade/", target="_blank")),
        dbc.Button("Toggle fade", id="fade-button", style={"margin-bottom": "1rem"}),
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

form = html.Div(
    [
        html.H2(dcc.Link("Form", href=DBC_DOCS + "form/", target="_blank")),
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
                                    style={"text-decoration": "underline"},
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
                                    style={"text-decoration": "underline"},
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
        html.H2(dcc.Link("Input", href=DBC_DOCS + "input/", target="_blank")),
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
        html.H4(dcc.Link("Checklist", href=DBC_DOCS + "input/", target="_blank")),
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
        html.H4(
            dcc.Link("RadioItems", href=DBC_DOCS + "input/", target="_blank"),
            className="mt-5",
        ),
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
        html.H2(
            dcc.Link(
                "Input groups and addons",
                href=DBC_DOCS + "input_group/",
                target="_blank",
            )
        ),
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

jumbotron = html.Div(
    [
        html.H2(dcc.Link("Jumbotron", href=DBC_DOCS + "jumbotron/", target="_blank")),
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
        html.H2(dcc.Link("ListGroup", href=DBC_DOCS + "list_group/", target="_blank")),
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
        html.H2(dcc.Link("Modal", href=DBC_DOCS + "modal/", target="_blank")),
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
        html.H2(dcc.Link("Navbar", href=DBC_DOCS + "navbar/", target="_blank")),
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
        ),
    ]
)

popover = html.Div(
    [
        html.H2(dcc.Link("Popover", href=DBC_DOCS + "popover/", target="_blank")),
        html.P(["Click on the word ", html.Span("popover", id="popover-target")]),
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
        html.H2(dcc.Link("Progress", href=DBC_DOCS + "progress/", target="_blank")),
        dbc.Progress(id="progress", value=0, striped=True, animated=True),
    ]
)

spinner = html.Div(
    [
        html.H2(dcc.Link("Spinner", href=DBC_DOCS + "spinner/", target="_blank")),
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
        html.H2(dcc.Link("HTML Table", href=DBC_DOCS + "table/", target="_blank")),
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
        html.H2(dcc.Link("Tabs", href=DBC_DOCS + "tabs/", target="_blank")),
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
        html.H2(dcc.Link("Toast", href=DBC_DOCS + "toast/", target="_blank")),
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
    ]
)

tooltip = html.Div(
    [
        html.H2(dcc.Link("Tooltip", href=DBC_DOCS + "tooltip/", target="_blank")),
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
    ## See the [source code]('https://github.com/AnnMarieW/HelloDash/blob/main/apps/components.py')       
    """
)


layout = html.Div(
    [
        dbc.Container(
            [
                dcc.Interval(id="interval", interval=500, n_intervals=0),
                header,
                html.Hr(),
                alerts,
                html.Hr(),
                badges,
                html.Hr(),
                buttons,
                html.Hr(),
                cards,
                html.Hr(),
                collapse,
                html.Hr(),
                columns,
                html.Hr(),
                dropdownmenu,
                html.Hr(),
                fade,
                html.Hr(),
                form,
                html.Hr(),
                input_,
                html.Hr(),
                input_group,
                html.Hr(),
                jumbotron,
                html.Hr(),
                list_group,
                html.Hr(),
                modal,
                html.Hr(),
                navbar,
                html.Hr(),
                popover,
                html.Hr(),
                progress,
                html.Hr(),
                spinner,
                html.Hr(),
                table,
                html.Hr(),
                tabs,
                html.Hr(),
                toast,
                html.Hr(),
                tooltip,
                html.Hr(),
                html.Div(style={"height": "50px"}),
                source_code,
            ],
            className="m-4",
        ),
    ]
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


@app.callback(Output("progress", "value"), [Input("interval", "n_intervals")])
def advance_progress(n):
    # advance to 100 then pause for a bit
    return min(n % 111, 100)


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

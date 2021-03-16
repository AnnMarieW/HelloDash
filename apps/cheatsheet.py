import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def make_link(title, link):
    return dbc.ListGroupItem(title, href=link, target="_blank")


dash_links = dbc.ListGroup(
    [
        make_link("Dash Documentation", "https://dash.plotly.com/"),
        make_link(
            "dash-core-components", "https://dash.plotly.com/dash-core-components"
        ),
        make_link("DataTable", "https://dash.plotly.com/datatable"),
        make_link("DashTable Reference", "https://dash.plotly.com/datatable/reference"),
        make_link("Dash DAQ components", "https://dash.plotly.com/dash-daq"),
        make_link("Dash Community Forum", "https://community.plotly.com/c/dash/16"),
    ]
)


boostrap_links = dbc.ListGroup(
    [
        make_link(
            "dash-boostrap-components Documentation",
            "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/",
        ),
        make_link(
            "Bootstrap Cheatsheet", "https://hackerthemes.com/bootstrap-cheatsheet/"
        ),
        make_link(
            "Bootstrap Bootswatch Themes", "https://www.bootstrapcdn.com/bootswatch/"
        ),
    ]
)

plotly_links = dbc.ListGroup(
    [
        make_link(
            "Plotly discrete colors", "https://plotly.com/python/discrete-color/"
        ),
        make_link(
            "Plotly continuous colorscaes",
            "https://plotly.com/python/builtin-colorscales/",
        ),
        make_link(
            "Plotly Figure Reference", "https://plotly.com/python/reference/index/"
        ),
        make_link(
            "Plotly Figure Structure Tutorial",
            "https://plotly.com/python/figure-structure/",
        ),
        make_link(
            "Plotly Express Overview", "https://plotly.com/python/plotly-express/"
        ),
        make_link(
            "Plotly Express Reference",
            "https://plotly.com/python-api-reference/plotly.express.html",
        ),
    ]
)

getting_started_links = dbc.ListGroup(
    [
        make_link(
            "Getting started with HTML",
            "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started",
        ),
        make_link("Learn CSS", "https://developer.mozilla.org/en-US/docs/Learn/CSS"),
        make_link(
            "Browser developer tools",
            "https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools",
        ),
        make_link(
            "Dash Bootstrap video by Charming Data",
            "https://www.youtube.com/watch?v=0mfIK8zxUds",
        ),
        make_link(
            "10 minutes to Pandas",
            "https://pandas.pydata.org/pandas-docs/dev/user_guide/10min.html",
        ),
    ]
)

how_to_links = dbc.ListGroup(
    [
        make_link(
            "How to format numbers in a DataTable",
            "https://formattable.pythonanywhere.com/",
        ),
        make_link(
            "How to add sparkline to a DataTable",
            "https://community.plotly.com/t/sparklines-as-fonts-embedding-minimal-sparklines-in-tables-components/39468",
        ),
        make_link(
            "How to do pattern matching callback",
            "https://community.plotly.com/t/pattern-call-backs-regarding-adding-dynamic-graphs/40724",
        ),
        make_link(
            "How to deploy your app on Heroku",
            "https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723",
        ),
    ]
)

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Bootstrap Links")),
                            dbc.CardBody(boostrap_links),
                        ],
                        className="m-2",
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Dash Links")),
                            dbc.CardBody(dash_links),
                        ],
                        className="m-2",
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Plotly Links")),
                            dbc.CardBody(plotly_links),
                        ],
                        className="m-2",
                    )
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("Getting Started Links")),
                            dbc.CardBody(getting_started_links),
                        ],
                        className="m-2",
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H4("How to Links")),
                            dbc.CardBody(how_to_links),
                        ],
                        className="m-2",
                    )
                ),
            ]
        ),
    ],
    fluid=True,
    className="m-4",
)

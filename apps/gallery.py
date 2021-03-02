import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
import dash_bootstrap_components as dbc

from gallery import theme_explorer_app

from app import app

# gallery content  Update info here to add apps to gallery

card0_image = ""
card0_title = "Coming Soon"
card0_source_code = ""
card0_about = ""

card1_image = "https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.png"
card1_title = "Light Theme App"
card1_source_code = "https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.pn"
card1_about = theme_explorer_app.about

card2_image = "https://user-images.githubusercontent.com/72614349/109723317-28228480-7b6b-11eb-8a50-0ac06ec2bca1.png"
card2_title = "Dark Theme App"
card2_source_code = (
    "https://github.com/AnnMarieW/HelloDash/blob/main/apps/sample_app_1.py"
)
card2_about = theme_explorer_app.about

"""
======================================================================
"""

header = dbc.Jumbotron(
    [
        html.H1("Dash Bootstrap App Gallery", className="display-3"),
        html.P("Example apps using Boostrap", className="lead",),
        html.P(
            " Creating a beautiful design for your app starts here!", className="lead",
        ),
        html.Hr(className="my-2"),
        html.Div(
            [
                dbc.Button(
                    "Theme Explorer", color="primary", href="/v03", className="mr-2"
                ),
                dbc.Button(
                    "Dash Bootstrap Components",
                    color="primary",
                    target="_blank",
                    className="mr-2",
                    href="https://dash-bootstrap-components.opensource.faculty.ai/",
                ),
                dbc.Button(
                    "Dash Documentation",
                    color="primary",
                    target="_blank",
                    href="https://dash.plotly.com/",
                ),
            ],
        ),
    ]
)


def make_card(id, image, text, source_code, about):
    return dbc.Card(
        [
            dbc.CardImg(src=image, top=True, style={"height": 350}),
            dbc.CardBody(
                [
                    html.P(text, className="card-text"),
                    dbc.Button(
                        "Source Code",
                        color="primary",
                        className="mr-2",
                        target="_blank",
                        href=source_code,
                    ),
                    dbc.Button(
                        "About", id={"type": "modal_btn", "index": id}, color="primary"
                    ),
                ]
            ),
            dbc.Modal(
                dbc.ModalBody(dcc.Markdown(about, className="p-4")),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="lg",
            ),
        ],
    )


layout = dbc.Container(
    [
        header,
        dbc.CardDeck(
            [
                make_card(
                    "card1_id", card1_image, card1_title, card1_source_code, card1_about
                ),
                make_card(
                    "card2_id", card2_image, card2_title, card2_source_code, card2_about
                ),
                make_card(
                    "card0_id", card0_image, card0_title, card0_source_code, card0_about
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output({"type": "modal", "index": MATCH}, "is_open"),
    Input({"type": "modal_btn", "index": MATCH}, "n_clicks"),
)
def open_card_modal(n):
    """ opens a model in the how-to tables"""
    return True if n else False

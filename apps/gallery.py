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
#----------------------------------------
card1_image = "https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.png"
card1_title = "Light Theme App"
card1_source_code = "https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.pn"
card1_about = theme_explorer_app.about
#----------------------------------------
card2_image = "https://user-images.githubusercontent.com/72614349/109723317-28228480-7b6b-11eb-8a50-0ac06ec2bca1.png"
card2_title = "Dark Theme App"
card2_source_code = (
    "https://github.com/AnnMarieW/HelloDash/blob/main/apps/sample_app_1.py"
)
card2_about = theme_explorer_app.about
#------------------------------------------------
card3= dbc.Card([

    dbc.CardHeader(html.H3("New to Web Design?")),

    dcc.Markdown("""

Here are some great resources:

- [Getting started with HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)
- [Learn CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
- [Browser developer tools ](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)
-  [My favorite Boostrap Cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)
- [Theme Explorer](https://hellodash.pythonanywhere.com/)
 - [Dash Bootstrap video by Charming Data](https://www.youtube.com/watch?v=0mfIK8zxUds)

Have any other good references?  Please drop me a note [here](https://github.com/AnnMarieW/HelloDash/issues) and I'll add
them to the list!

""", className='p-4'),
],)
#------------------------------------------------
card4_image ="https://user-images.githubusercontent.com/72614349/109746748-22409980-7b93-11eb-9a04-fa3876e1cb3c.png"
card4_title = "Great Starter app"
card4_source_code = "https://github.com/facultyai/dash-bootstrap-components/tree/main/examples/gallery/telephones-by-region"
card4_about = "This is one of the example apps in  [dash-bootstrap-components GitHub](https://github.com/facultyai/dash-bootstrap-components/tree/main/examples)"

#------------------------------------------------

card5= dbc.Card([

    dbc.CardHeader(html.H3("Add your app to the gallery!")),

    dcc.Markdown("""

Open an issue [here](https://github.com/AnnMarieW/HelloDash/issues) and include:

 - An image of your app
 -  A short title to appear on the card in the gallery
 - A link to the code in GitHub, GitLab or other repo
 - An extended description of your app (optional).  This will be displayed when the "About"
 button is clicked.  Format: Text or Markdown.

""", className='p-4'),
],)







"""
======================================================================
"""

header = dbc.Jumbotron(
    [
        html.H1("Dash Bootstrap App Gallery", className="display-3"),
        html.P("Example apps using Bootstrap", className="lead",),
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
                        color="secondary",
                        className="mr-2",
                        target="_blank",
                        href=source_code,
                    ),
                    dbc.Button(
                        "About", id={"type": "modal_btn", "index": id}, color="secondary"
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
                card3,
            ], className='m-4'
        ),
        dbc.CardDeck(
            [
                make_card(
                    "card4_id", card4_image, card4_title, card4_source_code, card4_about
                ),
                card5,
                make_card(
                    "card0_id", card0_image, card0_title, card0_source_code, card0_about
                ),
            ],className='m-4'
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

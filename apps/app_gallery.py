"""
This module creates the app gallery

Enter details for new cards in the order you want them to appear in the gallery


"""


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, MATCH
import dash_bootstrap_components as dbc

from apps import text
from util import header
from app import app

from dataclasses import dataclass


@dataclass
class Card:
    image: str = ""
    title: str = "Coming Soon"
    source_code: str = ""
    about: str = ""


gallery = []
CARDS_PER_ROW = 3

"""
=====================================================================
Add Card details and set card order 
"""

# 0
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.png",
        title="Light Theme App",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/theme_explorer_app.py",
        about="""
### The first two images in the app gallery are the same app!  
Use the Theme Explorer to see how different Boostrap Themes, Plotly templates and graph colors look in a Dash app. 
The design for this app is updated by changing 1 line of code. """
        + text.tutorial,
    )
)

# 1
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/109723317-28228480-7b6b-11eb-8a50-0ac06ec2bca1.png",
        title="Dark Theme App",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/theme_explorer_app.py",
        about=gallery[0].about,
    )
)

# 2
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/110154006-fa268580-7da0-11eb-950d-d6f48de48b53.png",
        title="Oil & Gas App from the Plotly Dash Gallery -- modified to use Bootstrap theme and dbc components.  No custom CSS!",
        source_code="https://github.com/AnnMarieW/HelloDash/tree/main/gallery/oil_and_gas",
        about="""
        This app is based on the Plotly Dash Enterprise App Gallery "Oil & Gas Wells" example.
        
        - For more information and more apps see: [Dash App Gallery](https://dash-gallery.plotly.host/Portal/)
        - See the Dash Enterprise app running [here](https://dash-gallery.plotly.host/dash-oil-and-gas/)
        - The GitHub for the original Plotly version is [here.](https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-oil-and-gas)
        
        
        This app is re-written using dash-bootstrap-components and standard Bootstrap class names.
        No custom CSS stylesheets are needed!
        
        - The GitHub for the [Boostrap version is here.](https://github.com/AnnMarieW/HelloDash/tree/main/gallery/oil_and_gas)
        """,
    )
)

# 3
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/110656159-ed2cdc00-817c-11eb-988d-88f19edaa19b.png",
        title="How to style a Dash DataTable",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/datatable_theme_explorer.py",
        about="""
        ### The two DataTables in this image are the same app.  Only one line is changed to use a different theme!   
        """,
    )
)

# 4
gallery.append(
    Card(
        title="""
        ### Add your app to the gallery!
        
        Open an issue [here](https://github.com/AnnMarieW/HelloDash/issues) and include:

         - An image of your app
         -  A short title to appear on the card in the gallery
         - A link to the code in GitHub, GitLab or other repo
         - An extended description of your app (optional).  This will be displayed when the "About"
         button is clicked.  Format: Text or Markdown.
        """
    )
)

# 5
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/111547777-e7179c00-8736-11eb-8a9b-9635b9712628.png",
        title="Quickstart App #1:  Two graphs, side by side.  Only about 25 lines of code.",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/quickstart1.py",
        about="One of the most popular questions on the Dash Community forum!",
    )
)


# 6


gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/13702392/128953753-5947a626-6c7f-4101-809b-dd0952053124.png",
        title="App by @astrowonk - See it live at [Covid-19 Case Growth](https://marcoshuerta.com/dash/covid/) ",
        source_code="https://github.com/astrowonk/covid_dash",
        about="""
        This Dash app displays new cases of covid-19 per county and/or state normalized by population. 
        It uses data from the [New York Times](https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html),
         which hosts the data on [their github repository](https://github.com/nytimes/covid-19-data).
         
         See this app live at: [Covid-19 Case Growth](https://marcoshuerta.com/dash/covid/)
         
         Thanks @astrowonk for adding this app to the gallery!        
        
        """,
    )
)
# 6a
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/109746748-22409980-7b93-11eb-9a04-fa3876e1cb3c.png",
        title="Quickstart App #2   <75 lines of code! ",
        source_code="https://github.com/facultyai/dash-bootstrap-components/tree/main/examples/gallery/telephones-by-region",
        about="This is one of the example apps in  [dash-bootstrap-components GitHub](https://github.com/facultyai/dash-bootstrap-components/tree/main/examples)",
    )
)


# 7

gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/109823988-a6c40400-7bf5-11eb-8ee3-15b91e9c170d.png",
        title="Quickstart app #3  ~ 100 lines of code",
        source_code="https://github.com/facultyai/dash-bootstrap-components/blob/main/examples/gallery/wordcloud/app.py",
        about="""This is one of the example apps in  [dash-bootstrap-components GitHub](https://github.com/facultyai/dash-bootstrap-components/tree/main/examples)  
                  Note: You may need to `pip install wordcloud`""",
    )
)

# 8
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/109817256-f2bf7a80-7bee-11eb-9beb-dd6673e98549.png",
        title="Example Apps in the Dash Bootstrap Components docs",
        source_code="https://dash-bootstrap-components.opensource.faculty.ai/examples/",
        about="""
    These are some of the example apps included in the official Dash Bootstrap Components documentation and tutorial.
    Go to [this page](https://dash-bootstrap-components.opensource.faculty.ai/examples/) and just click on an app to 
    run it and see the source code.""",
    )
)


# 9
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/109827271-d0325f00-7bf8-11eb-9dc4-a24640b46690.png",
        title="Investment Asset Allocation App",
        source_code="https://github.com/AnnMarieW/wealthdashboard",
        about="""This app shows how asset allocation impacts portfolio returns over time.  See it live at 
        [wealthdashboard.app](https://www.wealthdashboard.app/)""",
    )
)


# 10


gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/110704339-1025b300-81b2-11eb-9b26-7a8815e722ce.png",
        title="Layout template #1",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/layout_template_1.py",
        about=""" This is a simple template for the app layout.  See larger image
    [here](https://user-images.githubusercontent.com/72614349/110704339-1025b300-81b2-11eb-9b26-7a8815e722ce.png)
    """,
    )
)

# 11
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/110702548-e79cb980-81af-11eb-96b0-d89a36d3fcb9.png",
        title="Layout template  #2",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/layout_template_2.py",
        about="""  This is a simple template for the app layout.  See larger image 
    [here](https://user-images.githubusercontent.com/72614349/110702548-e79cb980-81af-11eb-96b0-d89a36d3fcb9.png)
    """,
    )
)

# 12
gallery.append(
    Card(
        image="https://user-images.githubusercontent.com/72614349/110704060-bb823800-81b1-11eb-8ac3-e866944beee6.png",
        title="Layout template  #3",
        source_code="https://github.com/AnnMarieW/HelloDash/blob/main/gallery/layout_template_3.py",
        about=""" This is a simple template for the app layout.  See larger image
    [here](https://user-images.githubusercontent.com/72614349/110704060-bb823800-81b1-11eb-8ac3-e866944beee6.png)
    """,
    )
)

# 13

gallery.append(
    Card(
        title="""
        ### New to Web Design?       

        Here are some great resources:

        - [Getting started with HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)
        - [Learn CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
        - [Browser developer tools ](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)
        -  [My favorite Boostrap Cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)
        - [Theme Explorer](https://hellodash.pythonanywhere.com/)
         - [Dash Bootstrap video by Charming Data](https://www.youtube.com/watch?v=0mfIK8zxUds)

        Have any other good references?  Please drop me a note [here](https://github.com/AnnMarieW/HelloDash/issues) and I'll add
        them to the list!

        """
    )
)

"""
======================================================================
Gallery Helper Functions
"""


def fill_empty_row():
    while len(gallery) % CARDS_PER_ROW:
        gallery.append(Card())


fill_empty_row()


def make_card(id, image, text, source_code, about):
    className_about = "d-none" if about == "" else ""
    className_source_code = "d-none" if source_code == "" else "mr-2"
    className_title = (
        "" if about == "" and image == "" and source_code == "" else "font-weight-bold"
    )
    return dbc.Card(
        [
            dbc.CardImg(
                src=image,
                top=True,
                style={"height": "auto", "width": "100%"},
                className="p-2",
            ),
            dbc.CardBody(
                [
                    dcc.Markdown(text, className=className_title),
                    dbc.Button(
                        "Source Code",
                        color="secondary",
                        className=className_source_code,
                        target="_blank",
                        href=source_code,
                        size="sm",
                        outline=True,
                    ),
                    dbc.Button(
                        "About",
                        id={"type": "modal_btn", "index": id},
                        color="secondary",
                        size="sm",
                        outline=True,
                        className=className_about,
                    ),
                ],
                className="p-",
            ),
            dbc.Modal(
                dbc.ModalBody(dcc.Markdown(about, className="p-4")),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="lg",
            ),
        ],
        className="mb-4 shadow",
    )


def make_gallery_row(row):
    return dbc.Row(
        dbc.CardDeck(
            [
                make_card(
                    f"id_card{i+row}",
                    gallery[i + row].image,
                    gallery[i + row].title,
                    gallery[i + row].source_code,
                    gallery[i + row].about,
                )
                for i in range(CARDS_PER_ROW)
            ],
            className=" mx-2",
        )
    )


"""
=====================================================================
Layout and Callbacks
"""
layout = dbc.Container(
    [
        header,
        html.H2(
            "Dash Bootstrap App Gallery",
            className="bg-primary text-white m-1 mb-4 p-2",
        ),
        html.Div([make_gallery_row(i) for i in range(0, len(gallery), CARDS_PER_ROW)]),
    ],
    fluid=True,
)


@app.callback(
    Output({"type": "modal", "index": MATCH}, "is_open"),
    Input({"type": "modal_btn", "index": MATCH}, "n_clicks"),
)
def open_card_modal(n):
    """ opens a model for the "About" button """
    return True if n else False

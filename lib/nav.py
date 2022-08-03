"""
This is a collection of nav components and headers

"""
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
import pathlib

# set relative path
PATH = pathlib.Path(__file__).parent
GALLERY_PATH = PATH.joinpath("./gallery").resolve()


# Links
dbc_logo = "https://user-images.githubusercontent.com/72614349/133677816-5ea52424-bfd3-4405-9ccf-8ad0dbd18020.png"
bootstrap_logo = "https://user-images.githubusercontent.com/72614349/133683669-eef08b42-2eff-49df-b0a5-33a7754a2b86.png"
bootstrap_url = "https://getbootstrap.com/docs/5.1/getting-started/introduction/"
dbc_home_url = "https://dash-bootstrap-components.opensource.faculty.ai/"
cheatsheet_url = "https://dashcheatsheet.pythonanywhere.com/"
theme_explorer_url = "https://hellodash.pythonanywhere.com/theme_explorer"
examples_index_url = "https://dash-example-index.herokuapp.com/"
dash_docs_url = "https://dash.plotly.com/"
dbt_url = "https://github.com/AnnMarieW/dash-bootstrap-templates"


theme_changer = ThemeChangerAIO(
    aio_id="theme",
    button_props={"color": "primary", "outline": True},
    radio_props={"value": dbc.themes.SPACELAB},
)


def make_header(text, spacing="mt-4"):
    return html.H2(
        text,
        className="text-white bg-primary p-2 " + spacing,
    )


theme_explorer_header = html.Div(
    dbc.Container(
        [
            html.H1(
                "Dash Bootstrap Theme Explorer",
                className="display-3 text-dark",
            ),
            html.P(
                "A guide for styling Plotly Dash apps with a Bootstrap theme",
                className="fst-italic lead",
            ),
            html.Div(
                [
                    html.A(
                        html.Img(src=dbc_logo, height=90, className="m-2"),
                        href=dbc_home_url,
                        target="_blank",
                    ),
                    html.A(
                        html.Img(src=bootstrap_logo, height=90, className="m-2"),
                        href=bootstrap_url,
                        target="blank",
                    ),
                ],
            ),
            html.Div(
                [
                    dbc.Button(
                        "Component Gallery",
                        color="primary",
                        outline=True,
                        href="/theme-explorer/gallery",
                        className="me-2",
                        size="sm",
                    ),
                    dbc.Button(
                        "Theme Change Components",
                        id="app_gallery",
                        color="primary",
                        outline=True,
                        href="/adding-themes/theme-switch",
                        className="me-2",
                        size="sm",
                    ),
                    dbc.Button(
                        "Figure Templates",
                        color="primary",
                        outline=True,
                        href="/adding-themes/figure-templates",
                        className="me-2",
                        size="sm",
                    ),
                    dbc.Button(
                        "Bootstrap Cheatsheet",
                        id="cheatsheet",
                        color="primary",
                        outline=True,
                        href=cheatsheet_url,
                        external_link=True,
                        target="_blank",
                        className="me-2",
                        size="sm",
                    ),
                ],
                className="mt-4",
            ),
        ],
        fluid=True,
        className="py-2",
    ),
    className="p-3 bg-light text-dark rounded-3 mb-4  position-relative",
    style={"minHeight": 375},
)


def make_sidebar_category(category="/", title=""):
    include_home = category == "/theme-explorer"
    return dbc.AccordionItem(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"]),
                    ],
                    href=page["path"],
                    active="exact",
                    className="py-2",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith(category)
                or (page["path"] == "/" and include_home)
            ],
            vertical=True,
            pills=True,
            # className="bg-light",
        ),
        title=title,
    )


def make_side_nav():
    return html.Div(
        [
            theme_changer,
            html.Hr(),
            dbc.Accordion(
                [
                    make_sidebar_category(
                        category="/theme-explorer", title="Theme Explorer"
                    )
                ],
            ),
            dbc.Accordion(
                [
                    make_sidebar_category(
                        category="/adding-themes", title="Adding Themes"
                    )
                ],
            ),
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dbc.Nav(
                            [
                                dbc.NavLink(
                                    "Dash Bootstrap Cheatsheet",
                                    href=cheatsheet_url,
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "Dash Examples Index",
                                    href=examples_index_url,
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    "Dash Docs", href=dash_docs_url, target="_blank"
                                ),
                                dbc.NavLink(
                                    "Dash Bootstrap Components Docs",
                                    href=dbc_home_url,
                                    target="_blank",
                                ),
                                dbc.NavLink(
                                    [
                                        html.I(className="fa-brands fa-github me-2"),
                                        "Dash Bootstrap Templates",
                                    ],
                                    href=dbt_url,
                                    target="_blank",
                                ),
                            ],
                            vertical=True,
                        ),
                        title="Other Sites",
                    )
                ],
            ),
        ],
        className="sticky-top",
    )


###############################  OLD #############################################
#
# side_nav = html.Div(
#     [
#         ThemeChangerAIO(
#             aio_id="theme",
#             button_props={"color": "primary", "outline": False},
#             radio_props={"value": dbc.themes.SPACELAB},
#         ),
#
#
#         dbc.Nav(
#             [
#                 html.Div("Component Gallery:", className="mt-4"),
#                 dbc.NavLink(
#                     "Dash Bootstrap Components", href="/theme_explorer#dbc", external_link=True
#                 ),
#                 dbc.NavLink("Bootstrap-themed Dash Core Components and DataTable", href="/about_dbc_css", external_link=True),
#
#
#               #  html.Div("Theme Change:", className="mt-4"),
#                 dbc.NavLink("Theme Change Components", href="/theme_change_components", external_link=True),
#
#                 html.Div("Figure Templates:", className="mt-4"),
#                 dbc.NavLink("Bootstrap-themed Figures Templates", href="/figure_templates", external_link=True),
#
#                 html.Div("More info:", className="mt-4"),
#                 dbc.NavLink(
#                     "Bootstrap Cheatsheet",
#                     href="https://dashcheatsheet.pythonanywhere.com/",
#                     external_link=True,
#                     target="_blank",
#                 ),
#                 dbc.NavLink(
#                     "Github -Theme Explorer",
#                     href="https://github.com/AnnMarieW/HelloDash",
#                     external_link=True,
#                     target="_blank",
#                 ),
#             ],
#             vertical=True,
#             pills=True,
#
#         ),
#     ],
#     className="sticky-top",
# )
#


# move to code and show
# def get_code_file(filename):
#     """
#     :param filename: (str) file name of python file in the gallery directory
#     :return: a string to display the code with highlighting in dcc.Markdown(code)
#
#     Note: be sure to include a blank line and docstring at start of source file so highlighting
#       works correctly
#     """
#     with open(GALLERY_PATH.joinpath(filename)) as f:
#         code = f.read()
#     return f"```{code}```"

# move to code and show
# def make_code_card(code, id=id, height=600, width=None):
#     return dbc.Card(
#         [
#             dcc.Markdown(
#                 code,
#                 id=id,
#                 className="p-2 mt-4"
#             ),
#             dcc.Clipboard(
#                 target_id=id,
#                 title="copy snippet",
#                 className="position-absolute top-0 end-0 fs-5",
#             ),
#         ],
#         className="position-relative mb-2",
#         style={"maxHeight": height, 'maxWidth': width, "overflow": "auto"},
#     )

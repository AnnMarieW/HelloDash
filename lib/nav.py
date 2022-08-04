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
dash_forum_url = "https://community.plotly.com/"

# other:
dmc_docs_url = "https://www.dash-mantine-components.com/"
dash_extensions_docs = "https://www.dash-extensions.com/"
dash_tools_url = "https://github.com/andrew-hossack/dash-tools"
multi_page_app_demos = "https://github.com/AnnMarieW/dash-multi-page-app-demos"

# tutorials
formattable_url = "https://formattable.pythonanywhere.com/"
legend_and_annotations = "https://plotly-annotations.herokuapp.com/"


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


other_dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem("Dash Mantine Components docs", href=dmc_docs_url),
        dbc.DropdownMenuItem("Dash Extensions docs", href=dash_extensions_docs),
        dbc.DropdownMenuItem("Multi-Page App examples", href=multi_page_app_demos),
        dbc.DropdownMenuItem(
            "Deploy to Heroku",
            href=dash_tools_url,
        ),
    ],
    label="more",
    toggle_class_name="m-3",
    color="light",
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
                                    "Dash Forum", href=dash_forum_url, target="_blank"
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
                                other_dropdown,
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

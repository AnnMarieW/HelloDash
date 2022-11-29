"""
This is a collection of nav components and headers

"""
import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
import pathlib

# set relative path
PATH = pathlib.Path(__file__).parent
GALLERY_PATH = PATH.joinpath("./gallery").resolve()


# Links
dbc_logo = "https://user-images.githubusercontent.com/72614349/133677816-5ea52424-bfd3-4405-9ccf-8ad0dbd18020.png"
bootstrap_logo = "https://user-images.githubusercontent.com/72614349/133683669-eef08b42-2eff-49df-b0a5-33a7754a2b86.png"
bootstrap_url = "https://getbotstrap.com/docs/5.1/getting-started/introduction/"
plotly_logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"
plotly_ddk_url = "https://plotly.com/dash/design-kit/"
dbc_home_url = "https://dash-bootstrap-components.opensource.faculty.ai/"
dbc_components_url = "https://dash-bootstrap-components.opensource.faculty.ai/docs/components/"
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
    html.Div(
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
                        html.Img(src=plotly_logo, height=80, className="m-2"),
                        href=plotly_ddk_url,
                        target="blank",
                        title="Plotly",
                    ),
                    html.A(
                        html.Img(src=dbc_logo, height=80, className="m-2"),
                        href=dbc_home_url,
                        target="_blank",
                        title="Dash Bootstrap Components",
                    ),
                    html.A(
                        html.Img(src=bootstrap_logo, height=80, className="m-2"),
                        href=bootstrap_url,
                        target="blank",
                        title="Bootstrap",
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
                        className="m-2",
                        size="sm",
                    ),
                    dbc.Button(
                        "Theme Change Components",
                        id="app_gallery",
                        color="primary",
                        outline=True,
                        href="/adding-themes/theme-switch",
                        className="m-2",
                        size="sm",
                    ),
                    dbc.Button(
                        "Figure Templates",
                        color="primary",
                        outline=True,
                        href="/adding-themes/figure-templates",
                        className="m-2",
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
                        className="m-2",
                        size="sm",
                    ),
                ],
                className="mt-4",
            ),
        ],
    ),
    className="p-3 bg-light text-dark rounded-3 mb-4 position-relative",
    style={"minHeight": 375, "minWidth": 800},
    id="header"
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


def make_sidebar_category_hash(page, title):
    """
    Use this to create an accordion item with links containing hashtags to scroll to a positions on the page.
    when registering the page include a list of ids to scroll to in a `hashtags` prop


    Args:
        page: A page in the dash.page_registry
        title: The title to show as the Accordion label

    Returns: navlinks with hashtags.

    """
   # dbc.Nav(dbc.NavLink("position", href="/adding-themes/bootstrap-utility-classes#position", external_link=True)),

    return dbc.AccordionItem(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        tag,
                    ],
                    href=f"{page['path']}#{tag}",
                    external_link=True, # must be true for scroll to work
                    active="exact",
                    className="py-2",
                )
                for tag in page.get("hashtags")

            ],
            vertical=True,
            pills=True,

        ),
        title=title,
    )



other_dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem(
            "Dash Mantine Components docs",
            href=dmc_docs_url,
            target="_blank",
        ),
        dbc.DropdownMenuItem(
            "Dash Extensions docs",
            href=dash_extensions_docs,
            target="_blank",
        ),
        dbc.DropdownMenuItem(
            "Multi-Page App examples",
            href=multi_page_app_demos,
            target="_blank",
        ),
        dbc.DropdownMenuItem(
            "DataTable Number Formatting",
            href=formattable_url,
            target="_blank",
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
                        category="/adding-themes", title="Applying Themes"
                    )
                ],
            ),
            dbc.Accordion(
                [
                    make_sidebar_category_hash(
                        page=dash.page_registry["pages.bootstrap_utility_classes.bootstrap_utility_classes"],
                        title="Bootstrap Utility Classes"
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
                                    href=dbc_components_url,
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
                        title="Other Helpful Sites",
                    )
                ],
            ),
        ],
        className="sticky-top vh-100 overflow-scroll",
    )


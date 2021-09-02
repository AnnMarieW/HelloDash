import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import theme_explorer as te, text
import util


"""
=====================================================================
Helper functions and components
"""

df = px.data.gapminder()

code = util.get_code_file("dash_bootstrap_templates_app.py")
copy_code_div = util.get_copy_code_div(code, id="copy_template_code")

# make control panel
use_templates = dbc.RadioItems(
    options=[
        {"label": "Use figure templates from dash-bootstrap-templates", "value": 1},
        {"label": "Use Plotly default figure template", "value": 2},
    ],
    value=1,
    id="use_figure_template",
)

control_panel_text = dcc.Markdown(
    text.dash_bootstrap_templates_text, className="border mb-5 p-4"
)

# needed because the theme dropdown also updates "css" on Theme Explorer page but not here
dummy_output = html.Div(id="css", className='d-none')

control_panel = [control_panel_text, te.boostrap_card, use_templates, dummy_output]

carousel = dbc.Carousel(
    ride="carousel",
    items=[
        {
            "key": "1",
            "src": "https://user-images.githubusercontent.com/72614349/129459807-30c22ffe-7a8c-44b9-9555-6cfd50ec355b.png",
        },
        {
            "key": "2",
            "src": "https://user-images.githubusercontent.com/72614349/129459808-40032148-82e1-47ce-a49a-05e598c69400.png",
        },
    ],
)

carousel_text = dcc.Markdown(text.dash_bootstrap_templates_app_text)


"""
===============================================================================
Layout
"""
layout = dbc.Container(
    [
        util.header,
        dbc.Row(
            [
                dbc.Col(control_panel, lg=4, sm=12),
                dbc.Col(
                    html.Div(
                        id="db_templates_sample_app", className="mx-1 mb-4 shadow p-4",
                    ),
                    lg=8,
                    sm=12,
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col([carousel_text, carousel], lg=4, sm=12),
                dbc.Col(html.Div(copy_code_div,), lg=8, sm=12,),
            ],
        ),
    ],
    fluid=True,
    id="bootstrap_templates",
)


"""
=====================================================================
Display Sample App based on theme selected
"""


@app.callback(
    Output("db_templates_sample_app", "children"),
    Input("themes", "value"),
    Input("use_figure_template", "value"),
)
def update_graphs(theme, use_template):

    template = util.url_dbc_themes[theme].lower() if use_template == 1 else {}

    heading_txt = (
        "App with dash-bootstrap-templates"
        if use_template == 1
        else "App with Plotly default figure template"
    )
    heading = html.H3(heading_txt, className="bg-primary text-white p-2")

    dff = df[df.year.between(1952, 1982)]
    dff = dff[dff.continent.isin(df.continent.unique()[1:])]

    line_fig = px.line(
        dff,
        x="year",
        y="gdpPercap",
        color="continent",
        line_group="country",
        template=template,
    )

    dff = dff[dff.year == 1982]
    scatter_fig = px.scatter(
        dff,
        x="lifeExp",
        y="gdpPercap",
        size="pop",
        color="pop",
        size_max=60,
        template=template,
    ).update_traces(marker_opacity=0.8)

    avg_lifeExp = (dff["lifeExp"] * dff["pop"]).sum() / dff["pop"].sum()
    map_fig = px.choropleth(
        dff,
        locations="iso_alpha",
        color="lifeExp",
        title="%.0f World Average Life Expectancy was %.1f years" % (1982, avg_lifeExp),
        template=template,
    )

    hist_fig = px.histogram(
        dff, x="lifeExp", nbins=10, title="Life Expectancy", template=template
    )

    graph_height = 300
    graphs = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=line_fig, style={"height": graph_height}), lg=6
                    ),
                    dbc.Col(
                        dcc.Graph(figure=scatter_fig, style={"height": graph_height}),
                        lg=6,
                    ),
                ],
                className="mt-4",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        dcc.Graph(figure=hist_fig, style={"height": graph_height}), lg=6
                    ),
                    dbc.Col(
                        dcc.Graph(figure=map_fig, style={"height": graph_height}), lg=6
                    ),
                ],
                className="mt-4",
            ),
        ]
    )

    # These buttons are added to the app just to show the Boostrap theme colors
    buttons = html.Div(
        [
            dbc.Button("Primary", color="primary", className="mr-1"),
            dbc.Button("Secondary", color="secondary", className="mr-1"),
            dbc.Button("Success", color="success", className="mr-1"),
            dbc.Button("Warning", color="warning", className="mr-1"),
            dbc.Button("Danger", color="danger", className="mr-1"),
            dbc.Button("Info", color="info", className="mr-1"),
            dbc.Button("Light", color="light", className="mr-1"),
            dbc.Button("Dark", color="dark", className="mr-1"),
            dbc.Button("Link", color="link"),
        ],
    )

    return [heading, buttons, graphs]


@app.callback(
    Output("bootstrap_templates", "className"), Input("light_dark", "value"),
)
def update_css(value):
    return "dbc_light" if value == "Light Themes" else "dbc_dark"

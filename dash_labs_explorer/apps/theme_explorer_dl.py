
import dash_labs as dl
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from dash_labs_explorer.apps import (
    HtmlCard_app,
    DbcCard_app,
    DbcRow_app,
    DbcSidebar_app,
    FlatDiv_app,
    DbcSidebarTabs_app,
)
from apps import theme_explorer as te
import util


tpl = dl.templates.DbcCard(title="App Design Selection", columns=12)
tpl._inline_css = ""

"""
=====================================================================
Helper functions and components
"""

checkbox = dbc.Checklist(
    id="checkbox",
    options=[{"label": "use theme", "value": "theme"}],
    value=["theme"],
    className="ml-2",
)


def make_spacer(height):
    return html.Div(style={"height": height})


badges = html.Div(
    [
        dbc.Badge("Primary", color="primary", className="mr-1"),
        dbc.Badge("Secondary", color="secondary", className="mr-1"),
        dbc.Badge("Success", color="success", className="mr-1"),
        dbc.Badge("Warning", color="warning", className="mr-1"),
        dbc.Badge("Danger", color="danger", className="mr-1"),
        dbc.Badge("Info", color="info", className="mr-1"),
        dbc.Badge("Light", color="light", className="mr-1"),
        dbc.Badge("Dark", color="dark", className="mr-1"),
    ]
)

css_options = [
    {"label": "className='dbc_light'", "value": "dbc_light"},
    {"label": "className='dbc_dark'", "value": "dbc_dark"},
    {
        "label": "className='dbc_light dbc_row_hover'",
        "value": "dbc_light dbc_row_hover",
    },
    {"label": "className='dbc_dark dbc_row_hover'", "value": "dbc_dark dbc_row_hover",},
    {"label": "className='dbc_dl' ", "value": "dbc_dl"},
    {"label": "none", "value": "dl"},
]

graph_color_modals = html.Div(
    [te.discrete_modal, te.continuous_modal, checkbox],
    className="d-inline-flex",
    id="graph_colors",
)

dl_code = html.Div(
    dcc.Markdown(id="dl_code"),
    className='p-4',

)


"""
=====================================================================
Build App Design Selection Panel
"""


tpl.add_component(
    te.make_dropdown("dl_template", util.dash_labs_templates),
    label="Dash Labs Templates",
)

tpl.add_component(make_spacer(10))
tpl.add_component(dcc.Dropdown(id="themes"), label="Bootstrap Themes")
tpl.add_component(te.make_radio_items("light_dark", ["Light Themes", "Dark Themes"]),)
tpl.add_component(make_spacer(10))


tpl.add_component(
    dcc.Dropdown(id="dl_css", options=css_options, value="dbc_light", clearable=False,),
    label="Custom CSS",
)
tpl.add_component(html.Div(id="css_text"))

tpl.add_component(
    te.make_dropdown("graph_template", util.plotly_template), label="Graph Templates"
)

tpl.add_component(graph_color_modals, label="Graph Color")

tpl.add_component(make_spacer(10))
tpl.add_component(badges, label="Selected Bootstrap Theme Colors")
tpl.add_component(
    dcc.Link(
        "See more Themes",
        href="https://www.bootstrapcdn.com/bootswatch/",
        target="_blank",
    )
)


"""
===============================================================================
Layout
"""
layout = dbc.Container(
    [
        util.header,
        dbc.Row(
            [
                dbc.Col(tpl.layout(app), lg=4),
                dbc.Col(
                    html.Div(
                        id="dl_sample_app", style={"marginLeft": 90, "minWidth": 600}
                    ),
                    lg=8,
                ),
            ],
        ),
        html.Hr(),
        dbc.Row(dbc.Col(dl_code))
    ],
    fluid=True,
    id="dl_app_container",
)


"""
=====================================================================
Display Sample App
"""


@app.callback(
    Output("dl_sample_app", "children"),
    Output('dl_code', "children"),
    Input("dl_template", "value"),
)
def display_sample_app(template):
    if template == "HtmlCard":
        return HtmlCard_app.tpl.layout(app), util.get_code_file(f"dl_{template}.py")
    elif template == "DbcCard":
        return DbcCard_app.tpl.layout(app), util.get_code_file(f"dl_{template}.py")
    elif template == "DbcRow":
        return DbcRow_app.tpl.layout(app), util.get_code_file(f"dl_{template}.py")
    elif template == "DbcSidebar":
        return DbcSidebar_app.tpl.layout(app), util.get_code_file(f"dl_{template}.py")
    elif template == "DbcSidebarTabs":
        return DbcSidebarTabs_app.tpl.layout(app), util.get_code_file(f"dl_{template}.py")
    else:
        return FlatDiv_app.tpl.layout(app), util.get_code_file(f"dl_{template}.py")


@app.callback(Output("dl_app_container", "className"), Input("dl_css", "value"))
def update_stylesheet(css):
    return "" if css == "none" else css

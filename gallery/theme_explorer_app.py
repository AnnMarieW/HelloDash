# -*- coding: utf-8 -*-
"""
Sample app with two different themes
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

"""
=====================================================================
Set details for your selected theme here
"""

# ------  App version 1  Minty theme   ------------
MINTY = {
    "external_stylesheets": [dbc.themes.MINTY],
    "graph_template": "simple_white",
    "color_discrete_sequence": px.colors.qualitative.Pastel,
    "color_continuous_scale": "darkmint",
    "app_background_color": "#F3F6F3",
}

# -------- App version 2 Darkly theme     -------------
DARKLY = {
    "external_stylesheets": [dbc.themes.DARKLY],
    "graph_template": "plotly_dark",
    "color_discrete_sequence": px.colors.qualitative.Dark24,
    "color_continuous_scale": "ice",
    "app_background_color": "",
}

"""
=====================================================================
Change THEME  to apply design themes to app
"""
THEME = MINTY
# THEME = DARKLY

app = dash.Dash(__name__, external_stylesheets=THEME["external_stylesheets"])

df = px.data.gapminder()

dropdown = dcc.Dropdown(
    id="indicator",
    options=[{"label": str(i), "value": i} for i in ["gdpPercap", "lifeExp", "pop"]],
    value="gdpPercap",
    clearable=False,
)

checklist = dbc.Checklist(
    id="continents",
    options=[{"label": i, "value": i} for i in df.continent.unique()],
    value=df.continent.unique()[3:],
    inline=True,
)

years = df.year.unique()
range_slider = dcc.RangeSlider(
    id="slider_years",
    min=years[0],
    max=years[-1],
    step=5,
    marks={int(i): str(i) for i in years},
    value=[1982, years[-1]],
)

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
    ]
)

controls = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.FormGroup([dbc.Label("Select indicator (y-axis)"), dropdown])
                ),
                dbc.Col(dbc.FormGroup([dbc.Label("Select continents"), checklist])),
            ]
        ),
        dbc.FormGroup([dbc.Label("Select years"), range_slider, buttons,]),
    ],
    className="m-4 px-2",
)

app.layout = dbc.Container(
    [
        html.H1("Theme Explorer App", className="bg-primary text-white",),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="line_chart"), lg=6),
                dbc.Col(dcc.Graph(id="scatter_chart"), lg=6),
            ]
        ),
        controls,
        html.Hr(),
    ],
    id="layout_container",
    fluid=True,
    style={"backgroundColor": THEME["app_background_color"]},
)


@app.callback(
    Output("line_chart", "figure"),
    Output("scatter_chart", "figure"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("slider_years", "value"),
)
def update_charts(indicator, continents, years):
    if continents == [] or indicator is None:
        return {}, {}

    dff = df[df.year.between(years[0], years[1])]
    fig = px.line(
        dff[dff.continent.isin(continents)],
        x="year",
        y=indicator,
        color="country",
        template=THEME["graph_template"],
        color_discrete_sequence=THEME["color_discrete_sequence"],
    )
    dff = df[df.year == years[1]]
    fig2 = px.scatter(
        dff[dff.continent.isin(continents)],
        x="lifeExp",
        y=indicator,
        color="lifeExp",
        template=THEME["graph_template"],
        color_continuous_scale=THEME["color_continuous_scale"],
        hover_data=["country", "year"],
    )
    return fig, fig2


if __name__ == "__main__":
    app.run_server(debug=True)

"""
Note:  For dark themed apps, add the following the css file in the assets folder.  This 
       styles the dropdown menu items to make them visible in both light and dark theme apps.
       See more info here: https://dash.plotly.com/external-resources

       For more custom CSS for other Dash Components see the dbc_light.css and dbc_dark.css
       here: https://github.com/AnnMarieW/HelloDash/tree/main/assets


.VirtualizedSelectOption {
    background-color: white;
    color: black;
}

.VirtualizedSelectFocusedOption {
    background-color: lightgrey;
    color: black;
}

"""

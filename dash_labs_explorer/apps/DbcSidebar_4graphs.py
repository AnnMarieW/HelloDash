"""
This is a demo of the `load_figure_template(themes)` function from dash_bootstrap_templates library
The `load_figure_templates(theme) loads the Bootstrap theme template,
adds it to plotly.io and makes it the default.  Do not use with `figure_template=True` in the

"""


import dash
from dash.dependencies import Input
import dash_labs as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc

from app import app
import util


# templates from dash-bootstrap-templates library
tpl = dl.templates.dbc.DbcSidebar(
    app, title="Dash Bootstrap Template Demo", sidebar_columns=3
)


df = px.data.gapminder()

dropdown = dcc.Dropdown(
    options=[{"label": str(i), "value": i} for i in ["gdpPercap", "lifeExp", "pop"]],
    value="gdpPercap",
    clearable=False,
)


checklist = dbc.Checklist(
    options=[{"label": i, "value": i} for i in df.continent.unique()],
    value=df.continent.unique()[1:],
    inline=True,
)

years = df.year.unique()
range_slider = dcc.RangeSlider(
    min=years[0],
    max=years[-1],
    step=5,
    marks={int(i): str(i) for i in [1952, 2007]},
    tooltip={"placement": "bottom"},
    value=[1982, years[-1]],
)


@app.callback(
    dl.Output(html.Div(), "children"),
    dl.Input(dropdown, label="Select indicator (y-axis)"),
    dl.Input(checklist, label="Select continents"),
    dl.Input(range_slider, label="Select time period"),
    Input("themes", "value"),
    Input("graph_template", "value"),
    Input("discrete_selected", "children"),
    Input("continuous_selected", "children"),
    Input("checkbox", "value"),
    template=tpl,
)
def update_charts(
    indicator,
    continents,
    yrs,
    theme,
    template,
    color_discrete,
    color_continuous,
    checkbox,
):
    if continents == [] or indicator is None:
        return {}

    color_discrete = color_discrete.split(": ")[1].strip()
    color_continuous = color_continuous.split(": ")[1].strip()
    line_colors = util.discrete_colors[color_discrete]
    if checkbox == []:
        line_colors = None
        color_continuous = None
    if template == "bootstrap":
        template = util.url_dbc_themes[theme].lower()

    dff = df[df.year.between(yrs[0], yrs[1])]
    dff = dff[dff.continent.isin(continents)]
    line_fig = px.line(
        dff,
        x="year",
        y=indicator,
        color="continent",
        line_group="country",
        template=template,
        color_discrete_sequence=line_colors,
    )

    dff = dff[dff.year == yrs[1]]
    scatter_fig = px.scatter(
        dff,
        x="lifeExp",
        y=indicator,
        size="pop",
        color="pop",
        size_max=60,
        template=template,
        color_continuous_scale=color_continuous,
    ).update_traces(marker_opacity=0.8)

    avg_lifeExp = (dff["lifeExp"] * dff["pop"]).sum() / dff["pop"].sum()
    map_fig = px.choropleth(
        dff,
        locations="iso_alpha",
        color="lifeExp",
        template=template,
        title="%.0f World Average Life Expectancy was %.1f years"
        % (yrs[1], avg_lifeExp),
    )

    hist_fig = px.histogram(
        dff, x="lifeExp", nbins=10, title="Life Expectancy", template=template
    )

    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=line_fig), lg=6),
                    dbc.Col(dcc.Graph(figure=scatter_fig), lg=6),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=hist_fig), lg=6),
                    dbc.Col(dcc.Graph(figure=map_fig), lg=6),
                ]
            ),
        ]
    )

# -*- coding: utf-8 -*-

"""
This shows the template defaults when using `figure_template=True in the template definition

"""


import dash
import dash_labs as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])

# Current dbc template themes
tpl = dl.templates.dbc.DbcSidebar(
    app,
    title="Dash Bootstrap Template Demo",
    sidebar_columns=3,
    theme=dbc.themes.JOURNAL,  # change theme here
    figure_template=True,
)

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
    value=df.continent.unique()[1:],
    inline=True,
)

years = df.year.unique()
range_slider = dcc.RangeSlider(
    id="slider_years",
    min=years[0],
    max=years[-1],
    step=5,
    marks={int(i): str(i) for i in [1952, 1962, 1972, 1982, 1992, 2002, 2007]},
    value=[1982, years[-1]],
)

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


@app.callback(
    dl.Input(dropdown, label="Select indicator (y-axis)"),
    dl.Input(checklist, label="Select continents"),
    dl.Input(range_slider, label="Select time period"),
    template=tpl,
)
def update_charts(indicator, continents, years):
    if continents == [] or indicator is None:
        return {}, {}

    dff = df[df.year.between(years[0], years[1])]
    dff = dff[dff.continent.isin(continents)]
    line_fig = px.line(
        dff, x="year", y=indicator, color="continent", line_group="country"
    )

    dff = dff[dff.year == years[1]]
    scatter_fig = px.scatter(
        dff, x="lifeExp", y=indicator, size="pop", color="pop", size_max=60
    ).update_traces(marker_opacity=0.8)

    avg_lifeExp = (dff["lifeExp"] * dff["pop"]).sum() / dff["pop"].sum()
    map_fig = px.choropleth(
        dff,
        locations="iso_alpha",
        color="lifeExp",
        title="%.0f World Average Life Expectancy was %.1f years"
        % (years[1], avg_lifeExp),
    )

    hist_fig = px.histogram(dff, x="lifeExp", nbins=10, title="Life Expectancy")

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


tpl.add_component(badges, location="sidebar", after=2)
app.layout = dbc.Container(fluid=True, children=tpl.children)


if __name__ == "__main__":
    app.run_server(debug=True)

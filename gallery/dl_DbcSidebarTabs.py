# -*- coding: utf-8 -*-
"""
Dash Labs demo of DbcSidebar Template
"""

import dash_labs as dl
import dash
import dash_table
import dash_core_components as dcc
import plotly.express as px
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])


tpl = dl.templates.DbcSidebarTabs(
    ["Line", "Scatter", "Table"],
    title="Dash Labs App - DbcSidebarTabs Template",
    figure_template=True,
    theme=dbc.themes.PULSE,
)

df = px.data.gapminder()

indicators = dcc.Dropdown(
    options=[{"label": str(i), "value": i} for i in ["gdpPercap", "lifeExp", "pop"]],
    value="gdpPercap",
    clearable=False,
)

continents = dbc.Checklist(
    options=[{"label": i, "value": i} for i in df.continent.unique()],
    value=[df.continent.unique()[0]],
    inline=True,
)

df_yrs = df.year.unique()
years = dcc.RangeSlider(
    min=df_yrs[0],
    max=df_yrs[-1],
    step=5,
    #   marks={int(i): str(i) for i in df_yrs},
    tooltip={"placement": "bottom", "always_visible": True},
    value=[df_yrs[2], df_yrs[-2]],
)


def make_table(dff):
    return (
        dash_table.DataTable(
            id="dl_table",
            columns=[{"name": i, "id": i, "deletable": True} for i in dff.columns],
            data=dff.to_dict("records"),
            page_size=10,
            editable=True,
            cell_selectable=True,
            filter_action="native",
            sort_action="native",
            style_table={"overflowX": "auto"},
        ),
    )


@app.callback(
    dl.Input(continents, label="Select continents"),
    dl.Input(indicators, label="Select indicator (y-axis)"),
    dl.Input(years, label="Select years"),
    output=[
        tpl.graph_output(role="Line"),
        tpl.graph_output(role="Scatter"),
        tpl.div_output(role="Table"),
    ],
    template=tpl,
)
def update_line_chart(continents_sel, indicator_sel, yrs):

    if continents_sel == [] or indicator_sel is None:
        return {}, {}, ""

    dff = df[df.year.between(yrs[0], yrs[1])]
    dff = dff[dff.continent.isin(continents_sel)]
    table = make_table(dff)

    line_fig = px.line(dff, x="year", y=indicator_sel, color="country",)

    dff = df[df.year == yrs[1]]
    scatter_fig = px.scatter(
        dff[dff.continent.isin(continents_sel)],
        x="lifeExp",
        y=indicator_sel,
        size="pop",
        color="pop",
        hover_name="country",
        size_max=60,
    ).update_traces(marker_opacity=0.8)

    return line_fig, scatter_fig, table


app.layout = tpl.layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)

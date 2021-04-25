from dash.dependencies import Input
import dash_labs as dl
import plotly.express as px
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table


from app import app
import util

tpl = dl.templates.DbcSidebarTabs(
    ["Line", "Scatter", "Table"], title="Dash Labs App - DbcSidebarTabs Template"
)

df = px.data.gapminder()

dl_indicators = dcc.Dropdown(
    options=[{"label": str(i), "value": i} for i in ["gdpPercap", "lifeExp", "pop"]],
    value="gdpPercap",
    clearable=False,
)

dl_continents = dbc.Checklist(
    options=[{"label": i, "value": i} for i in df.continent.unique()],
    value=df.continent.unique()[1:],
    inline=True,
)

df_yrs = df.year.unique()
dl_years = dcc.RangeSlider(
    min=df_yrs[0],
    max=df_yrs[-1],
    step=5,
    #   marks={int(i): str(i) for i in df_yrs},
    tooltip={"placement": "bottom", "always_visible": True},
    value=[df_yrs[2], df_yrs[-2]],
)


def make_table(dff):
    return html.Div(
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
            style_data_conditional=[
                {
                    "if": {"state": "active"},
                    "border": ".5px solid ",
                    "fontWeight": 1000,
                },
                {"if": {"state": "selected"}, "fontWeight": 700,},
            ],
            #  This is an example to show  it's not possible to change the background and
            #  text color when using the DL table styles.
            #
            # style_data_conditional=[
            #     {
            #         'if': {
            #             'column_id': 'continent',
            #         },
            #         'backgroundColor': 'dodgerblue',
            #         'color': 'white',
            #         'textAlign': 'left'
            #     },
            # ],
        ),
    )


@app.callback(
    dl.Input(dl_continents, label="Select continents"),
    dl.Input(dl_indicators, label="Select indicator (y-axis)"),
    dl.Input(dl_years, label="Select years"),
    Input("themes", "value"),
    Input("graph_template", "value"),
    Input("discrete_selected", "children"),
    Input("continuous_selected", "children"),
    Input("checkbox", "value"),
    Input("store", "data"),
    output=[
        tpl.graph_output(role="Line"),
        tpl.graph_output(role="Scatter"),
        tpl.div_output(role="Table"),
    ],
    template=tpl,
)
def update_line_chart(
    continents_sel,
    indicator_sel,
    yrs,
    theme,
    template,
    color_discrete,
    color_continuous,
    checkbox,
    dbc_template,
):
    if continents_sel == [] or indicator_sel is None:
        return {}, {}, ""

    # figure line colors default is from the generated Bootstrap figure template.  These can be changed
    # in the app by selecting a different color sequence
    color_discrete = color_discrete.split(": ")[1].strip()
    color_continuous = color_continuous.split(": ")[1].strip()
    line_colors = util.discrete_colors[color_discrete]
    if checkbox == []:
        line_colors = None
        color_continuous = None
    if template == "bootstrap":
        template = dbc_template[theme]

    dff = df[df.year.between(yrs[0], yrs[1])]
    dff = dff[dff.continent.isin(continents_sel)]
    table = make_table(dff)

    line_fig = px.line(
        dff,
        x="year",
        y=indicator_sel,
        color="continent",
        line_group="country",
        template=template,
        color_discrete_sequence=line_colors,
    )

    dff = df[df.year == yrs[1]]
    scatter_fig = px.scatter(
        dff[dff.continent.isin(continents_sel)],
        x="lifeExp",
        y=indicator_sel,
        size="pop",
        color="pop",
        hover_name="country",
        template=template,
        color_continuous_scale=color_continuous,
        size_max=60,
    ).update_traces(marker_opacity=0.8)

    return line_fig, scatter_fig, table

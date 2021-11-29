from dash import dcc, html, dash_table, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc
import util

# model
df = px.data.gapminder()
years = df.year.unique()
continents = df.continent.unique()

code = util.get_code_file("theme_explorer_app.py")
code_card = util.make_code_card(code, id="copy_theme_explorer_app_code")

header = html.H3("Sample Dash App - Before", className="p-2 my-2", style={"backgroundColor": "gray", "color":"white"})


table = dash_table.DataTable(
    id="table1",
    columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
    data=df.to_dict("records"),
    page_size=10,
    editable=True,
    cell_selectable=True,
    filter_action="native",
    sort_action="native",
    style_table={"overflowX": "auto"},
)


dropdown = html.Div(
    [
        dbc.Label("Select indicator (y-axis)"),
        dcc.Dropdown(
            id="indicator1",
            options=[
                {"label": str(i), "value": i} for i in ["gdpPercap", "lifeExp", "pop"]
            ],
            value="pop",
            clearable=False,
        ),
    ],
    className="mb-4",
)

checklist = html.Div(
    [
        dbc.Label("Select Continents"),
        dcc.Checklist(
            id="continents1",
            options=[{"label": i, "value": i} for i in continents],
            value=continents[2:],
           # inline=True,
        ),
    ],
    className="mb-4",
)

slider = html.Div(
    [
        dbc.Label("Select Years"),
        dcc.RangeSlider(
            id="years1",
            min=years[0],
            max=years[-1],
            tooltip={"placement": "bottom", "always_visible": True},
            value=[years[2], years[-2]],
        ),
    ],
    className="mb-4",
)


controls = dbc.Card([dropdown, checklist, slider], body=True,)

my_code = dcc.Markdown(f"```{code}```")

tab1 = dcc.Tab([dcc.Graph(id="line-chart1")], label="Graph",)
tab2 = dcc.Tab([table], label="Table1", className="p-4")
tab3 = dcc.Tab(code_card, label="Source Code")
tabs = dcc.Tabs([tab1, tab2, tab3])

layout = dbc.Container(
    [header, dbc.Row([dbc.Col([controls], width=12, lg=4), dbc.Col(tabs, width=12, lg=8)])],
    fluid=True,
)


@callback(
    Output("line-chart1", "figure"),
    Output("table1", "data"),
    Input("indicator1", "value"),
    Input("continents1", "value"),
    Input("years1", "value"),
)
def update_line_chart(indicator, continent, yrs):
    if continent == [] or indicator is None:
        return {}, []

    dff = df[df.year.between(years[0], yrs[1])]
    dff = dff[dff.continent.isin(continent)]
    data = dff.to_dict("records")

    fig = px.line(
        dff,
        x="year",
        y=indicator,
        color="continent",
        line_group="country",
    )
    fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))

    return fig, data

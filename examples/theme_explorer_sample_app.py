"""
This app applies Bootstrap themes to Dash components and Plotly figures by
using the stylesheet, figure templates and theme change component
from the dash-bootstrap-templates library: https://github.com/AnnMarieW/dash-bootstrap-templates

`className="dbc"`  Use this with Dash Core Components and the DataTable to:
- make the text readable in both light and dark themes.
- use the font from the Bootstrap theme's font-family.
- change the accent color to the theme's primary color

The figure templates applies Bootstrap themes to Plotly figures.  These figure
templates are included in the theme change component.

If you run this app locally, add the theme change component to the layout
"""

from dash import Dash, dcc, html, dash_table, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

df = px.data.gapminder()
years = df.year.unique()
continents = df.continent.unique()

# stylesheet with the .dbc class
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

header = html.H4(
    "Theme Explorer Sample App", className="bg-primary text-white p-2 mb-2 text-center"
)

table = dash_table.DataTable(
    id="theme-explorer-sample-app-x-table",
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
            ["gdpPercap", "lifeExp", "pop"],
            "pop",
            id="theme-explorer-sample-app-x-indicator",
            clearable=False,
        ),
    ],
    className="mb-4",
)

checklist = html.Div(
    [
        dbc.Label("Select Continents"),
        dbc.Checklist(
            id="theme-explorer-sample-app-x-continents",
            options=[{"label": i, "value": i} for i in continents],
            value=continents,
            inline=True,
        ),
    ],
    className="mb-4",
)

slider = html.Div(
    [
        dbc.Label("Select Years"),
        dcc.RangeSlider(
            years[0],
            years[-1],
            5,
            id="theme-explorer-sample-app-x-years",
            marks=None,
            tooltip={"placement": "bottom", "always_visible": True},
            value=[years[2], years[-2]],
        ),
    ],
    className="mb-4",
)
theme_colors = [
    "primary",
    "secondary",
    "success",
    "warning",
    "danger",
    "info",
    "light",
    "dark",
    "link",
]
colors = html.Div(
    [dbc.Button(f"{color}", color=f"{color}", size="sm") for color in theme_colors]
)
colors = html.Div(["Theme Colors:", colors], className="mt-2")


controls = dbc.Card(
    [dropdown, checklist, slider],
    body=True,
)

tab1 = dbc.Tab(
    [dcc.Graph(id="theme-explorer-sample-app-x-line-chart")], label="Line Chart"
)
tab2 = dbc.Tab(
    [dcc.Graph(id="theme-explorer-sample-app-x-scatter-chart")], label="Scatter Chart"
)
tab3 = dbc.Tab([table], label="Table", className="p-4")
tabs = dbc.Tabs([tab1, tab2, tab3])

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(
                    [
                        controls,
                        # When running this app locally, un-comment this line:
                        # ThemeChangerAIO(aio_id="theme")
                    ],
                    width=4,
                ),
                dbc.Col([tabs, colors], width=8),
            ]
        ),
    ],
    fluid=True,
    className="dbc",
)


@callback(
    Output("theme-explorer-sample-app-x-line-chart", "figure"),
    Output("theme-explorer-sample-app-x-scatter-chart", "figure"),
    Output("theme-explorer-sample-app-x-table", "data"),
    Input("theme-explorer-sample-app-x-indicator", "value"),
    Input("theme-explorer-sample-app-x-continents", "value"),
    Input("theme-explorer-sample-app-x-years", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_line_chart(indicator, continent, yrs, theme):
    if continent == [] or indicator is None:
        return {}, {}, []

    dff = df[df.year.between(yrs[0], yrs[1])]
    dff = dff[dff.continent.isin(continent)]
    data = dff.to_dict("records")

    fig = px.line(
        dff,
        x="year",
        y=indicator,
        color="continent",
        line_group="country",
        template=template_from_url(theme),
    )

    fig_scatter = px.scatter(
        df.query(f"year=={yrs[1]} & continent=={continent}"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template_from_url(theme),
        title="Gapminder %s: %s theme" % (yrs[1], template_from_url(theme)),
    )

    return fig, fig_scatter, data


if __name__ == "__main__":
    app.run_server(debug=True)

#

"""
This app applies Bootstrap themes to Dash components and Plotly figures by
using the stylesheet, figure templates and theme change component
from the dash-bootstrap-templates library: https://github.com/AnnMarieW/dash-bootstrap-templates

`className="dbc"`:
- Makes the text readable in both light and dark themes.
- Uses the font from the Bootstrap theme's font-family.
- Changes the accent color to the theme's primary color

The figure templates applies Bootstrap themes to Plotly figures.  These figure
templates are included in the theme change component.
"""

from dash import Dash, dcc, html, dash_table, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

df = px.data.gapminder()
years = df.year.unique()
continents = df.continent.unique()

# stylesheet with the .dbc class
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

header = html.H4("Sample Dash App", className="bg-primary text-white p-2 mb-2 text-center")

table = dash_table.DataTable(
    id="table",
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
            id="indicator",
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
        dbc.Checklist(
            id="continents",
            options=[{"label": i, "value": i} for i in continents],
            value=continents[2:],
            inline=True,
        ),
    ],
    className="mb-4",
)

slider = html.Div(
    [
        dbc.Label("Select Years"),
        dcc.RangeSlider(
            id="years",
            min=years[0],
            max=years[-1],
            tooltip={"placement": "bottom", "always_visible": True},
            value=[years[2], years[-2]],
        ),
    ],
    className="mb-4",
)

colors = html.Div(
    [
        html.Span("Theme Colors: "),
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ],
    className="mb-2",
)

controls = dbc.Card(
    [
        dropdown,
        checklist,
        slider
    ],
    body=True,
)

tab1 = dbc.Tab([dcc.Graph(id="line-chart"), colors], label="Graph")
tab2 = dbc.Tab([table], label="Table", className="p-4")
tabs = dbc.Tabs([tab1, tab2])

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col([controls, ThemeChangerAIO(aio_id="theme")], width=4),
                dbc.Col(tabs, width=8),
            ]
        ),
    ],
    fluid=True,
    className="dbc",
)


@callback(
    Output("line-chart", "figure"),
    Output("table", "data"),
    Input("indicator", "value"),
    Input("continents", "value"),
    Input("years", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_line_chart(indicator, continent, yrs, theme):
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
        template=template_from_url(theme),
    )
    fig.update_layout(margin=dict(l=75, r=20, t=10, b=20))

    return fig, data


if __name__ == "__main__":
    app.run_server(debug=True)

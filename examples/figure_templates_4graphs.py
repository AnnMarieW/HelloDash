from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template


templates = [
    "bootstrap",
    "cerulean",
    "cosmo",
    "cyborg",
    "darkly",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "morph",
    "pulse",
    "quartz",
    "sandstone",
    "simplex",
    "sketchy",
    "slate",
    "solar",
    "spacelab",
    "superhero",
    "united",
    "vapor",
    "yeti",
    "zephyr",
]

dropdown = dcc.Dropdown(templates, "spacelab", clearable=False, className="m-3")
output_container = html.Div()

# This loads all the figure template from dash-bootstrap-templates library,
# adds the templates to plotly.io and makes the first item the default figure template.
load_figure_template(templates)


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.gapminder()

heading = html.H2("Figure Template Demo", className="bg-primary text-white p-2 mb-3")

app.layout = dbc.Container(
    [
        heading,
        html.Label("Select a figure template"),
        dropdown,
        dcc.Loading(output_container),
    ],
    fluid=True,
)


@app.callback(Output(output_container, "children"), Input(dropdown, "value"))
def update(template):
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
        template=template,
        title="%.0f World Average Life Expectancy was %.1f years" % (1982, avg_lifeExp),
    )

    hist_fig = px.histogram(
        dff, x="lifeExp", nbins=10, title="Life Expectancy", template=template
    )

    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=line_fig, className="border"), lg=6),
                    dbc.Col(dcc.Graph(figure=scatter_fig, className="border"), lg=6),
                ],
                className="mt-4",
            ),
            dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=hist_fig, className="border"), lg=6),
                    dbc.Col(dcc.Graph(figure=map_fig, className="border"), lg=6),
                ],
                className="mt-4",
            ),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)

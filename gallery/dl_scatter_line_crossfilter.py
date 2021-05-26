import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_labs as dl
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

# Make app and template
app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])
tpl = dl.templates.DbcRow(app, title="Gapminder", input_cols=4, figure_template=True)

# Load and preprocess dataset
df = px.data.gapminder()
years = sorted(df.year.drop_duplicates())
continents = list(df.continent.drop_duplicates())


@app.callback(
    args=dict(
        year=tpl.slider_input(
            years[0], years[-1], step=5, value=years[-1], label="Year"
        ),
        continent=tpl.checklist_input(continents, value=continents, label="Continents"),
        logs=tpl.checklist_input(["log(x)"], value="log(x)", label="Axis Scale"),
    ),
    output=tpl.graph_output(id="scatter_graph"),
    template=tpl,
)
def callback(year, continent, logs):
    # Let parameterize infer output component
    year_df = df[df.year == year]
    if continent:
        year_df = year_df[year_df.continent.isin(continent)]

    if not len(year_df):
        return go.Figure()

    title = f"Life Expectancy ({year})"
    return (
        px.scatter(
            year_df,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x="log(x)" in logs,
            size_max=60,
            title=title,
        )
        .update_layout(margin=dict(l=0, r=0, b=0))
        .update_traces(marker_opacity=0.8)
    )


line_chart = dcc.Graph(id="line_chart")
tpl.add_component(line_chart, role="output", after=0)


@app.callback(Output("line_chart", "figure"), Input("scatter_graph", "clickData"))
def display_click_data(clickData):
    country = ""
    fig = px.line(title=f"Country selected: {country}")
    if clickData:
        country = clickData["points"][0]["hovertext"]
        fig = px.line(
            df[df.country == country],
            x="year",
            y="lifeExp",
            title=f"Country selected: {country}",
        )
    return fig


app.layout = dbc.Container(tpl.children, fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)

from dash import Dash, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px

df = px.data.gapminder()

# Makes the Bootstrap Themed Plotly templates available
load_figure_template("minty")

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    log_x=True,
    size_max=60,
    template="minty",  # use the minty themed figure template
    title="Gapminder 2007: Minty Theme",
)

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

app.layout = dbc.Container(dcc.Graph(figure=fig, className="m-4"))

if __name__ == "__main__":
    app.run_server(debug=True)

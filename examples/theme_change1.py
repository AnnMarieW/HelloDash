from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url

df = px.data.stocks()

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

theme_change = ThemeChangerAIO(aio_id="theme")
graph = html.Div(dcc.Graph(id="theme-change-graph"), className="m-4")

app.layout = dbc.Container([theme_change, graph], className="m-4 dbc")


@app.callback(
    Output("theme-change-graph", "figure"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_graph_theme(theme):
    return px.line(df, x="date", y="GOOG", template=template_from_url(theme))


if __name__ == "__main__":
    app.run_server(debug=True)

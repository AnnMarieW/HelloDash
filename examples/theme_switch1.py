from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

df = px.data.stocks()

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

theme_switch = ThemeSwitchAIO(
    aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.CYBORG]
)
graph = html.Div(dcc.Graph(id="theme-switch-graph"), className="m-4")

app.layout = dbc.Container([theme_switch, graph], className="m-4 dbc")


@app.callback(
    Output("theme-switch-graph", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    template = "cosmo" if toggle else "cyborg"
    return px.line(df, x="date", y="GOOG", template=template)


if __name__ == "__main__":
    app.run_server(debug=True)

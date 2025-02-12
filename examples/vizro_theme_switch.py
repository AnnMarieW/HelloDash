
from dash import Dash, html, dcc, Input, Output, Patch, clientside_callback, callback
import plotly.express as px
import plotly.io as pio
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template

# Load data and figure templates
gapminder = px.data.gapminder().query("year==2007")
load_figure_template(["vizro", "vizro_dark"])


# Alternatively, you could do:
# You need to install vizro>=0.1.34
#import vizro
#app = Dash(__name__, external_stylesheets=[vizro.bootstrap])

vizro_bootstrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@main/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[vizro_bootstrap])

# Create components for the dashboard
color_mode_switch = html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="vizro-switch"),
        dbc.Switch(id="vizro-switch", value=False, className="d-inline-block ms-1"),
        dbc.Label(className="fa fa-sun", html_for="vizro-switch"),
    ]
)
scatter = dcc.Graph(
    id="vizro-scatter", figure=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", size_max=60, color="continent")
)
box = dcc.Graph(id="vizro-box", figure=px.box(gapminder, x="continent", y="lifeExp", color="continent"))


tabs = dbc.Tabs(
    [
        dbc.Tab(box, label="Box Plot"),
        dbc.Tab(scatter, label="Scatter Plot"),
    ]
)

app.layout = dbc.Container(
    [html.H3("Vizro Bootstrap Demo", className="bg-primary p-2 mt-4"), color_mode_switch, tabs],
    fluid=True,
)


# Add callbacks to switch between dark / light
@callback(
    [Output("vizro-scatter", "figure"), Output("vizro-box", "figure")],
    Input("vizro-switch", "value"),
)
def update_figure_template(switch_on):
    """Sync the figure template with the color mode switch on the bootstrap template."""
    template = pio.templates["vizro"] if switch_on else pio.templates["vizro_dark"]
    patched_figure = Patch()
    patched_figure["layout"]["template"] = template

    return patched_figure, patched_figure


clientside_callback(
    """
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    """,
    Output("vizro-switch", "id"),
    Input("vizro-switch", "value"),
)


if __name__ == "__main__":
    app.run(debug=True)

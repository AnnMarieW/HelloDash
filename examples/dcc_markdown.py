from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# stylesheet with the .dbc class from dash-bootstrap-templates library
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])

markdown = dcc.Markdown(
    """
The dcc.Markdown component works well for regular markdown text in both light and
dark themes.  For code highlighting, adding `className="dbc"` will make code snippets styled in the 
"GitHub Dark Dimmed" theme which (I think) looks better in both light and dark Bootstrap themes. 

See this forum post to learn more about [changing the theme of code highlights.](https://community.plotly.com/t/how-to-change-the-theme-of-code-highlights-in-dcc-markdown/58004)

Here's a sample:

```python

from datetime import date

datepicker_single = html.Div(
    [dcc.DatePickerSingle(date=date(2021, 5, 10))], className="dbc"
)

```

    """,
    className="p-4 border",
)

with_theme = html.Div(
    [html.H3("Markdown"), dbc.Label("dcc.Markdown with Bootstrap theme"), markdown],
    className="dbc",
)

app.layout = dbc.Container([with_theme])

if __name__ == "__main__":
    app.run_server(debug=True)

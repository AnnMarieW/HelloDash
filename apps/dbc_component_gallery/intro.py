from dash import dcc, html
import dash_bootstrap_components as dbc

intro_text = dcc.Markdown(
    """
The Bootstrap theme is automatically applied to the components in the [`dash-boostrap-templates`](https://dash-bootstrap-components.opensource.faculty.ai/) library.
    """
)

intro = dbc.Alert(intro_text, color="primary", className="p-2")

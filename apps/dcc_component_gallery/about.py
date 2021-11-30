from dash import dcc
import dash_bootstrap_components as dbc

about_text = dcc.Markdown("""
This sample app uses:
- `dbc.css` stylesheet to apply Bootstrap themes to  Dash components.`
- Bootstrap-themed Plotly figure templates to style the figures with the selected Bootstrap theme
- Theme switch component   

See the code in the "source code" tab

You can find all these features in the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
 Requires `dash>=2.0.0`, `dash-bootstrap-components>=1.0.0`, `dash-boostrap-templates>=1.0.2`
""",
                          )
about_md = dbc.Alert(about_text, color="secondary", className="p-2")

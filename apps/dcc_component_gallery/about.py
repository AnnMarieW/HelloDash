from dash import dcc
import dash_bootstrap_components as dbc

about_text = dcc.Markdown("""
Use the stylesheet and the figure templates from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library
to apply Bootstrap themes to  Dash components.  

`className="dbc"`:
- Makes the text readable in both light and dark themes.
- Uses the font from the Bootstrap theme's font-family.
- Changes the accent color to the theme's primary color

The figure templates automatically applies Bootstrap themes to Plotly figures.
""",
                          )
about_md = dbc.Alert(about_text, color="primary", className="p-2")

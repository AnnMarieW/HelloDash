from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

title = dcc.Markdown(
    """
### Spacing - Padding and Margin 
------------
"""
)

intro = dcc.Markdown(
    """
The classes are named using the format {property}{sides}-{size} for xs and {property}{sides}-{breakpoint}-{size} for sm, md, lg, xl, and xxl.

Where property is one of:

- m - sets margin
- p - sets padding

Where sides is one of:

- t - sets margin-top or padding-top
- b - sets margin-bottom or padding-bottom
- s - (start) sets margin-left or padding-left in LTR, margin-right or padding-right in RTL
- e - (end) sets margin-right or padding-right in LTR, margin-left or padding-left in RTL
- x - sets both *-left and *-right
- y - sets both *-top and *-bottom
- blank - sets a margin or padding on all 4 sides of the element

Where size is one of:

- 0 - eliminates the margin or padding by setting it to 0
- 1 - sets the margin or padding to .25rem
- 2 - sets the margin or padding to .5rem
- 3 - sets the margin or padding to 1rem
- 4 - sets the margin or padding to 1.5rem
- 5 - sets the margin or padding to 3rem
- auto - sets the margin to auto

### Example App
"""
)


spacing = html.Div(
    [
        html.Div(
            "bg-light text-dark border", className="p-1 bg-light text-dark border"
        ),
        html.Div(
            "p-1 bg-light text-dark border", className="p-1 bg-light text-dark border"
        ),
        html.Div(
            "p-2 bg-light text-dark border", className="p-2 bg-light text-dark border"
        ),
        html.Div(
            "p-3 bg-light text-dark border", className="p-3 bg-light text-dark border"
        ),
        html.Div(
            "p-4 bg-light text-dark border", className="p-5 bg-light text-dark border"
        ),
        html.Div(
            "p-5 bg-light text-dark border", className="p-5 bg-light text-dark border"
        ),
        html.Div(
            "m-1 bg-light text-dark border", className="m-1 bg-light text-dark border"
        ),
        html.Div(
            "m-2 bg-light text-dark border", className="m-2 bg-light text-dark border"
        ),
        html.Div(
            "m-3 bg-light text-dark border", className="m-3 bg-light text-dark border"
        ),
        html.Div(
            "m-4 bg-light text-dark border", className="m-5 bg-light text-dark border"
        ),
        html.Div(
            "m-5 bg-light text-dark border", className="m-5 bg-light text-dark border"
        ),
        html.Div(
            "m-5 p-5 bg-light text-dark border",
            className="m-5 p-5 bg-light text-dark border",
        ),
        html.H4("See more spacing examples in the Cheatsheet"),
    ]
)

app.layout = html.Div([title, intro, spacing])

if __name__ == "__main__":
    app.run(debug=True)

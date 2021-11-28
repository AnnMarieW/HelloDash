from dash import dcc, html, dash_table
import plotly.express as px

import dash_bootstrap_components as dbc


from .util import datatable_make_subheading


df = px.data.tips()

table = dash_table.DataTable(
    columns=[{"name": i, "id": i, "deletable": True} for i in df.columns],
    data=df.to_dict("records"),
    page_size=5,
    editable=True,
    cell_selectable=True,
    filter_action="native",
    sort_action="native",
    style_table={"overflowX": "auto"},
)

datatable_md = dcc.Markdown(
    """
`className="dbc"` minimally styles the Datatable with your selected Bootstrap theme:
- Makes the text readable in both light and dark themes by using the theme's "body" color for the text and background.
- Uses the font from the Bootstrap theme's font-family.
- Changes the accent color for the icons to he theme's primary color instead of the default Hot Pink. Icons include:
   - Pagination buttons (if any)
   - In the columns headers if the column is deleteable, hideable
   - the case sensitive icons if the table includes filters
- Changes the background color of the active and selected cells to colors based on the theme's Primary color instead of the default Hot Pink.
""",
    className="dbc mt-4 p-4",
)


datatable = html.Div([datatable_make_subheading(), dbc.Row(table)], className="mb-4",)

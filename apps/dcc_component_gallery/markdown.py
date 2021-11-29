import dash_bootstrap_components as dbc
from dash import html, dcc

from .util import dcc_make_subheading


markdown = dcc.Markdown(
    """
The dcc.Markdown component works well for regular markdown text in both light and
dark themes.  Adding `className="dbc"` will make code snippets styled in the 
"GitHub Dark Dimmed" theme which looks better in both light and dark Boostrap themes. 
Here's a sample:

```python

from datetime import date

datepicker_single = html.Div(
    [dcc.DatePickerSingle(date=date(2021, 5, 10))], className="dbc"
)

```
    
    """,
    className="mb-2",
)


dcc_markdown = html.Div(
    [dcc_make_subheading("dcc.Markdown", "markdown"), dbc.Row(markdown)],
    className="mb-4",
)

from dash import dcc, html
import dash_bootstrap_components as dbc
from .util import dcc_make_subheading

dcc_content = dcc.Markdown(
    """
Note that the dcc.Tabs are easy to customizable with inline styles or css.  
See the Dash documentation [here](https://dash.plotly.com/dash-core-components/tab).
    """
)

dbc_content = dcc.Markdown(
    """    
Rather than using dcc.Tabs, These tabs are from the dash-bootstrap-components library. 
They are automatically styled according to the theme

    """
)


tabs = html.Div(
    [
        dcc.Tabs(
            value="tab-1",
            children=[
                dcc.Tab(
                    label="Tab one",
                    value="tab-1",
                    children=html.Div(dcc_content, className="p-4"),
                ),
                dcc.Tab(
                    label="Tab two",
                    value="tab-2",
                    children=html.Div("Tab 2 Content", className="p-4"),
                ),
            ],
        ),
    ]
)


dcc_tabs = html.Div(
    [dcc_make_subheading("dcc.Tabs", "tabs"), dbc.Row(tabs)], className="mb-4",
)

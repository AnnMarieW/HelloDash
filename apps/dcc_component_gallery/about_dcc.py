from dash import dcc
import dash_bootstrap_components as dbc

intro_text = dcc.Markdown(
    """
Bootstrap themes are not automatically applied to Dash Core Components and the Dash DataTable.  The 
`dbc` class is designed to minimally style Dash components with your selected theme.  See 
below for more information on how to add the stylesheet with the `dbc` class to your app.    
    """
)

about_dcc_md = dbc.Alert(intro_text, color="primary", className="p-2")

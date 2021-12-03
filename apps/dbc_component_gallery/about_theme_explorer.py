from dash import dcc
import dash_bootstrap_components as dbc

about_explorer_md = dcc.Markdown(
    """
#### Select Your Bootstrap Theme 
 - The [`dash-bootstrap-components`](https://dash-bootstrap-components.opensource.faculty.ai/) library offers 26 free Bootstrap and Bootswatch themes.
  Use the "Change Theme" button to select a theme then see what it looks like in the Bootstrap-themed Dash app and the Dash Bootstrap Component gallery below.  
#### Apply Bootstrap theme to Dash DataTable and Core Components
- The Theme Explorer styles the Dash `DataTable` and the `dash-core-components`  with your
 selected Bootstrap theme.  It does this by using the `dbc.css` stylesheet from the 
 [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. See how to add this to your
  Dash apps in the "Bootstrap-themed Dash Core Components" section of the Component Gallery.
 
#### How to add a Theme Change Component to your app
  - The Theme Explorer uses the `ThemeChangerAIO` to select from multiple themes. There is also a `ThemeSwitchAIO` 
  component to toggle between two themes. Find these components in the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
  See examples in the Theme Change Components section.
  
#### How to apply a Bootstrap Theme to Figures
 -  The Theme Explorer applies Bootstrap themes to figures by using one of the 26 Bootstrap-themed Plotly figure templates available in the 
 [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. See examples in the Figure Templates section

#### Bootstrap Cheatsheet
  - See all the Bootstrap classes available with examples of how to use them with Dash.
  

The sample app below is a live demo of all these features.  Click the "Change Theme" button and see how the components
and figures are automatically updated with your selected theme.  See the code in the "source code" tab.

Requires `dash>=2.0.0`, `dash-bootstrap-components>=1.0.0`, `dash-bootstrap-templates>=1.0.4`    
    """
)

about_explorer = dbc.Accordion(
    dbc.AccordionItem(about_explorer_md, title="Hide/Show intro"),
)

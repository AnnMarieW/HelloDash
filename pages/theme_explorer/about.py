from dash import register_page

from dash import dcc, html
import dash_bootstrap_components as dbc
import lib.nav

register_page(__name__, order=0, name="About")

about_explorer_md = dcc.Markdown(
    """
#### Select Your Bootstrap Theme 
 - The [`dash-bootstrap-components`](https://dash-bootstrap-components.opensource.faculty.ai/) library offers 26 free Bootstrap and Bootswatch themes.
  Use the "Change Theme" button to select a theme then see how it looks in the Bootstrap-themed Dash app and the Dash Bootstrap Components gallery.  

#### Apply Bootstrap theme to your App
- Adding a Bootstrap theme will apply only to Bootstrap components in your app. However, to fully implement the theme
 into your app, you will likely need it to apply to the Dash DataTable, Dash Core Components, and Plotly figures as well.
  The Theme Explorer styles the Dash DataTable and the dash-core-components in the demo app with your selected Bootstrap theme. It does
   this by using the dbc.css stylesheet from the [dash-bootstrap-templates library](https://github.com/AnnMarieW/dash-bootstrap-templates). See how to add this to your Dash apps
    in the [Bootstrap-themed Dash Core Components and DataTable](https://hellodash.pythonanywhere.com/about_dbc_css)
    section. 

#### Apply a Bootstrap Theme to Figures
 -  The Theme Explorer applies Bootstrap themes to figures by using one of the 26 Bootstrap-themed Plotly figure templates available in the 
 [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. See examples of how to add 
 these to your app in the [Figure Templates](https://hellodash.pythonanywhere.com/figure_templates) section.

#### How to add a Theme Change Component to your app
  - The Theme Explorer uses the `ThemeChangerAIO` to select from multiple themes. There is also a `ThemeSwitchAIO` 
  component to toggle between two themes. Find these components in the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
  See examples in the [Theme Change Components](https://hellodash.pythonanywhere.com/theme_change_components) section.

#### Bootstrap Cheatsheet
  - See the [cheatsheet](https://dashcheatsheet.pythonanywhere.com/) with all the Bootstrap classes available with examples of how to use them with Dash.


The sample app below is a live demo of all these features.  Click the "Change Theme" button and see how the components
and figures are automatically updated with your selected theme.  See the code in the "source code" tab.

Requires `dash>=2.0.0`, `dash-bootstrap-components>=1.0.0`, `dash-bootstrap-templates>=1.0.4`    
    """
)

about_explorer = dbc.Accordion(
    dbc.AccordionItem(about_explorer_md, title="Hide/Show intro"),
)

layout = html.Div(
    [
        lib.nav.make_header("About Theme Explorer", spacing=""),
        about_explorer_md,
    ]
)

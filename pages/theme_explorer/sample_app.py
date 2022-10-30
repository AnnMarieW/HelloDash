import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_tabs

from lib.utils import app_description

dash.register_page(
    __name__,
    path="/",
    order=1,
    name="Sample App",
    description=app_description,
    title="Theme Explorer",
    redirect_from=["/theme_explorer", "/adding-themes/getting-started", "/about"],
)


about_explorer_md = dcc.Markdown(
    """

### Welcome to the Dash Bootstrap Theme Explorer 🤗


The sample app above demonstrates a Plotly Dash app with Bootstrap themes. It uses components from the dash-bootstrap-components
library which automatically update based on your selected theme.  To update Dash Core Components, the DataTable and
Plotly figures it uses the dbc.css stylesheet and the Bootstrap themed figure templates from the  [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.

In the sample app, you'll see:
  - the text is readable in both light and dark themes
  - all the components and figures use the font-family and colors from the selected theme


` `  
` `  

### Installation
 - If you're new to Dash, see the [Dash Tutorial](https://dash.plotly.com/) and the [Dash Boostrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) documentation.
 - The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library requires `dash>=2.0.0`, `dash-bootstrap-components>=1.0.0`

 ```
 pip install dash-bootstrap-templates -U
 ``` 

#### Select Your Bootstrap Theme 
 - The [`dash-bootstrap-components`](https://dash-bootstrap-components.opensource.faculty.ai/) library offers 26 free Bootstrap and [Bootswatch](https://bootswatch.com/) themes.
  Use the "Change Theme" button to select a theme then see how it looks in the sample app above and the  <dccLink href="/theme-explorer/gallery" children="dbc Gallery" /> sections.  

#### Apply Bootstrap theme to your App
- Adding a Bootstrap theme will apply only to Bootstrap components in your app. However, to fully implement the theme
 into your app, you will likely need it to apply to the Dash DataTable, Dash Core Components, and Plotly figures as well.
  This Theme Explorer app styles the Dash DataTable and the dash-core-components with your selected Bootstrap theme. It does
   this by using the dbc.css stylesheet from the [dash-bootstrap-templates library](https://github.com/AnnMarieW/dash-bootstrap-templates). See how to add this to your Dash apps in the
    in the  <dccLink href="/adding-themes/dcc-components" children="dash-core-components" /> and <dccLink href="/adding-themes/datatable" children="DataTable" /> sections. 

#### Apply a Bootstrap Theme to Figures
 -  The Theme Explorer applies Bootstrap themes to figures by using one of the 26 Bootstrap-themed Plotly figure templates available in the 
 [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library. See examples of how to add 
 these to your app in the  <dccLink href="/adding-themes/figure-templates" children="Figure templates" /> section.

#### Add a Theme Change Component to your app
  - The Theme Explorer uses the `ThemeChangerAIO` to select from multiple themes. There is also a `ThemeSwitchAIO` 
  component to toggle between two themes. Find these components in the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
  See examples in the  <dccLink href="/adding-themes/theme-switch" children="Theme change components" /> section.

#### Use Bootstrap Utility Classes
  - Bootstrap includes dozens of utility classes for showing, hiding, aligning, spacing and styling content. See all the
   Bootstrap classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/) 
  - See a live demo and more examples in the <dccLink href="/adding-themes/bootstrap-utility-classes" children="Bootstrap Utility Classes" /> section.


    """,
    dangerously_allow_html=True,
    link_target="_blank",
    className="m-5 p-3"
)

icon = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
icon_text = html.Span(
    [
        icon,
        "Use 'Change Theme' button to see this app with all 26 themes! ",
    ]
)

layout = html.Div(
    [
        html.Div(
            dbc.Alert(
                icon_text, is_open=True, dismissable=True, style={"maxWidth": 350}
            ),
        ),
        example_app("sample_app", make_layout=make_tabs),
        about_explorer_md,
    ],
    className="dbc",
)

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

### Welcome to Dash Bootstrap Theme Explorer 🤗

This is a guide for styling your Plotly Dash app with a Bootstrap theme.  Use the sample app above to help
select a theme, then I'll show you how to create an app with a Bootstrap theme applied not only to the components
in the `dash-bootstrap-components` library but also to `dash-core-components`, the `DataTable` and Plotly figures as well.

When you change the theme, you'll see that:
  - the text is readable in both light and dark themes
  - all the components and figures use the font-family and colors from the selected theme
  
This is easy when you use the stylesheet, Bootstrap themed figure templates and theme change components from the `dash-bootstrap-templates`
library.

` `  
` `  

### Installation
 - If you're new to Dash, see the [Dash Tutorial](https://dash.plotly.com/) and the [Dash Boostrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) documentation.
 - The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library requires `dash>=2.0.0`, `dash-bootstrap-components>=1.0.0`

 ```
 pip install dash-bootstrap-templates -U
 ``` 

##### Select Your Bootstrap Theme 
 - The [`dash-bootstrap-components`](https://dash-bootstrap-components.opensource.faculty.ai/) library includes links to 26 free Bootstrap and [Bootswatch](https://bootswatch.com/) themes.
  Use the "Change Theme" button to select a theme then see how it looks in the sample app above and the  <dccLink href="/theme-explorer/gallery" children="dbc Gallery" /> sections.  

##### Add Bootstrap Stylesheets
- Adding a stylesheet from the dash-bootstrap-components library will apply the theme to Bootstrap components in 
your app. To apply the Bootstrap theme to the Dash DataTable or Dash Core Components, add the stylesheet from the [dash-bootstrap-templates library](https://github.com/AnnMarieW/dash-bootstrap-templates). 
Learn more in the <dccLink href="/adding-themes/dcc-components" children="dash-core-components" /> and <dccLink href="/adding-themes/datatable" children="DataTable" /> sections. 

##### Apply a Bootstrap Theme to Figures
 -  The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library has 26 Bootstrap themed
 figure templates.  Learn how to use them in your app in the  <dccLink href="/adding-themes/figure-templates" children="Figure templates" /> section.

##### Add a Theme Change Component
  - The Theme Explorer uses the `ThemeChangerAIO` to select from multiple themes. There is also a `ThemeSwitchAIO` 
  component to toggle between two themes. Find these components in the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
  Learn more in the  <dccLink href="/adding-themes/theme-switch" children="Theme change components" /> section.

##### Use Bootstrap Utility Classes
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

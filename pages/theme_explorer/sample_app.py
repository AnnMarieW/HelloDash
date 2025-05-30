import dash
from dash import html, dcc
from lib.other_components import change_theme_alert
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

This is a guide for styling your Plotly Dash app with a Bootstrap theme.  If you're new to Dash, see the
 [Dash Tutorial](https://dash.plotly.com/) and the [Dash Bootstrap Components](https://dash-bootstrap-components.com/) documentation.

Use the sample app above to help select a theme, then I'll show you how to apply the theme to:
- Dash Bootstrap Components
- Dash Core Components
- Dash HTML Components
- Dash DataTable
- Plotly figures

You'll learn how to:
  - Make the text readable in both light and dark themes
  - Make the components and figures use the font-family and colors from the selected theme
  - Use the theme change components from the [dash-bootstrap-templates]([dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates)) library.
  - Use Bootstrap utility classes for showing, hiding, aligning, spacing and styling content.

` `  
` `  

### Installation 
 - The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library requires a minimum of `dash>=2.0.0`, `dash-bootstrap-components>=1.0.0`

 ```
 pip install dash-bootstrap-templates -U
 ``` 

##### Select Your Bootstrap Theme 
 - The [`dash-bootstrap-components`](https://dash-bootstrap-components.com/) library includes links to 26 free Bootstrap and [Bootswatch](https://bootswatch.com/) themes.
  Use the "Change Theme" button to select a theme then see how it looks in the sample app above and the  <dccLink href="/theme-explorer/gallery" children="dbc Gallery" /> sections.  
  
 - Add a color mode switch to toggle between a light and dark mode of any theme.  (Requires `dash-bootstrap-components>=1.5.0`)

##### Add Bootstrap Stylesheets
- Adding a stylesheet from the dash-bootstrap-components library will apply the theme to Bootstrap components in 
your app. To apply the Bootstrap theme to the Dash DataTable or Dash Core Components, add the stylesheet from the [dash-bootstrap-templates library](https://github.com/AnnMarieW/dash-bootstrap-templates). 
Learn more in the <dccLink href="/adding-themes/dcc-components" children="dash-core-components" /> and <dccLink href="/adding-themes/datatable" children="DataTable" /> sections. 

##### Apply a Bootstrap Theme to Figures
 -  The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library has 52 Bootstrap themed
 figure templates.  Learn how to use them in your app in the  <dccLink href="/adding-themes/figure-templates" children="Figure templates" /> section.

##### Add a Theme Change Component
  - The Theme Explorer uses the `ThemeChangerAIO` to select from multiple themes. To toggle between light and dark mode of
   your selected theme, see the   <dccLink href="/adding-themes/color-modes" children="Light Dark Color Mode" /> section.

##### Use Bootstrap Utility Classes
  - Bootstrap includes dozens of utility classes for showing, hiding, aligning, spacing and styling content. See all the
   Bootstrap classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/) 
  - See a live demo and more examples in the <dccLink href="/adding-themes/bootstrap-utility-classes" children="Bootstrap Utility Classes" /> section.

` `  
` `  


-----------------  

### Next:  
Apply Bootstrap theme to <dccLink href="/adding-themes/dcc-components" children="dash-core-components" />


    """,
    dangerously_allow_html=True,
    link_target="_blank",
    className="m-5 p-3"
)

layout = html.Div(
    [
        change_theme_alert(
            text="See the Sample App with all 26 themes in light or dark mode",
            auto_dismiss=False
        ),
        example_app("sample_app", make_layout=make_tabs),
        about_explorer_md,
    ],
    className="dbc",
)

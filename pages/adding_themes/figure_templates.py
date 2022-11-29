from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_app_first, make_tabs
from lib.utils import app_description, theme_dark_md, themes_light_md


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Adding Themes/Figure Templates",
    name="Figure templates",
)

intro = """
## Styling Plotly Figures with a Bootstrap theme

Plotly has built-in [figure templates](https://plotly.com/python/templates/) to make it easy to change the look of figures.
We'll show you how to add Bootstrap themed figure templates from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates)
 library and use them in your Dash app.


---------------
` `  
` `  


### Plotly Default Figure Template

Before showing the Bootstrap templates, let's take a look at a plotly figure with the default "plotly" figure template.

```
from dash import Dash, dcc, html
import plotly.express as px

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

app=Dash(__name__)
app.layout = html.Div(dcc.Graph(figure=fig))

if __name__ == "__main__":
    app.run(debug=True)
```
![plotly default](https://user-images.githubusercontent.com/72614349/198302294-64d9bbd2-1c52-4b42-be2b-bdf000aaf3c4.png#fluid)

------------
` `  
` `  
### Bootstrap Figure Templates


Here is the same figure, with the Bootstrap "sketchy" themed figure template.  We use the `load_figure_template` function from the
  `dash_bootstrap_templates` library to load the template and set it as the default.  Now unless you specify a different template,
  all the figures will have the "sketchy" theme.  

```
from dash import Dash, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# loads the "sketchy" template and sets it as the default
load_figure_template("sketchy")

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

app=Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
app.layout = dbc.Container(dcc.Graph(figure=fig))

if __name__ == "__main__":
    app.run(debug=True)
```


![image](https://user-images.githubusercontent.com/72614349/198308642-d13c4a21-5b5a-4402-8e64-4efcf716c9ef.png#fluid)

-----------------
` `  
` `  
### Changing the Figure Template

Use the `template` prop in the figure to change the theme.  Here's how to change it back to the default ("plotly") figure
 template:

```
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", template="plotly")
```


--------------
` `  
` `  
### Loading multiple Figure Templates

To add more Bootstrap themed figure templates, use a list instead of a string in the `load_figure_template` function:

```
load_figure_template(["sketchy", "cyborg", "minty"])
```

The "sketchy" theme is the default because it's the first template in the list. However, the other templates
 can now be used in the app by setting the `template` prop:
```
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", template="cyborg")
```

![cyborg template](https://user-images.githubusercontent.com/72614349/198323822-2d3ae46f-ba08-4401-93e3-56f91921cb47.png#fluid)

-------------
` `  
` `  

### Using Figure Templates with a theme change component

When using the `ThemeChangerAIO` or the `ThemeSwitchAIO` components: 
- The figure template is not automatically changed when the app theme changes.  You will need to update the figure in a callback to update the figure
 template.  
- It is not necessary to use the `load_figure_template()` function  -  the theme change component does that step for you.

See examples in the <dccLink href="/adding-themes/theme-switch" children="Theme change" /> section. 

-------------

### Examples

"""



theme_accordion = dbc.Accordion(
    [
        dbc.AccordionItem(dcc.Markdown(theme_dark_md, className="px-4"), title="See dark theme colors"),
        dbc.AccordionItem(dcc.Markdown(themes_light_md, className="px-4"), title="See light theme colors"),
    ],
    start_collapsed=True,
    className="mx-5 px-3",
)

all_templates = """
### All Templates

This example shows the Bootstrap themed figure templates, plus all the built-in Plotly figure templates.  Use the
Change Theme button to see different figure templates when the dropdown selection is "bootstrap_theme".

Thank you [Tuomas Poukkula](https://github.com/tuopouk)for this example!

"""

next = """
-----------------  

### Next:  
Adding a  <dccLink href="/adding-themes/theme-switch" children="Theme change component" />

"""


layout = html.Div(
    [
        dcc.Markdown(intro, dangerously_allow_html=True, className="mx-5 px-3"),
        theme_accordion,
        html.Div(
            example_app("figure_templates_4graphs", make_layout=make_tabs),
            className="dbc",
        ),
        dcc.Markdown("### Example of the 'minty' theme applied to the figure.", dangerously_allow_html=True,className="mx-5 px-3" ),

        example_app("adding_theme_figure_template", make_layout=make_tabs),
        dcc.Markdown("### Now see this figure with all themes:", dangerously_allow_html=True, className="mx-5 px-3"),
        html.Div(
            example_app(
                "figure_templates_all",
                show_code=False,
                make_layout=make_app_first,
            ),
           # className="p-4",
        ),

        dcc.Markdown(all_templates,  className="mx-5 px-3", link_target="_blank"),
        example_app("figure_template_change", make_layout=make_tabs),

        dcc.Markdown(
            next,
            className="m-5 px-3 dbc",
            dangerously_allow_html=True,
        ),

    ],
    className="dbc",
)

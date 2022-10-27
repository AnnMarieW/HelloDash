from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_app_first, make_tabs
from lib.utils import app_description


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Adding Themes/Figure Templates",
    name="Figure templates",
)

intro = """
## Plotly Figure Templates with a Bootstrap theme

Plotly has several built-in [figure templates](https://plotly.com/python/templates/) to quickly change the look of your figure.
We sill show you how to add figure templates with a Bootstrap theme from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates)
 library and use them in your Dash app.


---------------

### Plotly Default Figure Template

Here is a plotly figure with the default "plotly" figure template.

```
from dash import Dash, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

app=Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
app.layout= html.Div(dcc.Graph(figure=fig))

if __name__ == "__main__":
    app.run(debug=True)
```
![plotly default](https://user-images.githubusercontent.com/72614349/198302294-64d9bbd2-1c52-4b42-be2b-bdf000aaf3c4.png)

------------

### Bootstrap Figure Template


Here is the same figure, but it now uses the "sketchy" themed figure template.  We make this template available in our app by using
the `load_figure_template` function from the  `dash_bootstrap_templates` library.  This function will add the "sketchy"
 template and make it the default, so you don't need to specify the template when you define your figure. All of the figures in the app will now
have the "sketchy" theme.  

```
from dash import Dash, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# loads the "sketchy" template and sets it as the default
load_figure_template("sketchy")

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

app=Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
app.layout= html.Div(dcc.Graph(figure=fig))

if __name__ == "__main__":
    app.run(debug=True)
```


![image](https://user-images.githubusercontent.com/72614349/198308642-d13c4a21-5b5a-4402-8e64-4efcf716c9ef.png)

-----------------

### Changing the Figure Template

In the app above, you can change back to the default ("plotly") figure template by using the `template` prop in the figure:

```
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", template="plotly")
```


--------------

### Loading multiple Figure Templates

You can make other Bootstrap themed figure templates available in your app by using a list instead of a string in the
`load_figure_template` function:

```
load_figure_template(["sketchy", "cyborg", "minty"])
```

The "sketchy" theme will still be the default (because it's the first template in the list). However, the other templates
 are now available and can be used in a figure by setting the `template` prop:
```
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", template="cyborg")
```

![cyborg template](https://user-images.githubusercontent.com/72614349/198323822-2d3ae46f-ba08-4401-93e3-56f91921cb47.png)

-------------

### Using Figure Templates with a theme change component

When you change the app theme with the `ThemeChangerAIO` or the `ThemeSwitchAIO` components, the figure template is not
automatically changed.  You will need to update the figure in a callback to update the figure template.  See examples in the
[Theme change components](https://hellodash.pythonanywhere.com/adding-themes/theme-switch) section. 

-------------

### Examples

"""


layout = html.Div(
    [
        dcc.Markdown(intro),
        html.Div(
            example_app(
                "figure_templates_all",
                show_code=False,
                make_layout=make_app_first,
            ),
            className="p-4",
        ),
        dcc.Markdown("### Example of the 'minty' theme applied to the figure."),
        example_app("adding_theme_figure_template",make_layout=make_tabs),
        html.Div(
            example_app("figure_templates_4graphs", make_layout=make_tabs),
            className="dbc",
        ),
    ],
    className="dbc",
)

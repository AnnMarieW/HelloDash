from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_app_first, make_tabs
from lib.utils import app_description, theme_dark_md, themes_light_md


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Vizro Bootstrap Theme",
    name="Vizro Bootstrap Theme",
)

intro = """

## Vizro Bootstrap Theme
In addition to the 26 themes available in the dash-bootstrap-components library, you can now style your Dash app with a Vizro theme as well!

Learn more at [Vizro](), and the [Visual Vocabulary](https://vizro-demo-visual-vocabulary.hf.space/) site.

` `
` `

-----   



![image](https://github.com/user-attachments/assets/e82ef1d4-a2aa-4e86-9882-94611d47b24b#fluid400)
![image](https://github.com/user-attachments/assets/0b66409a-a100-43c8-b96e-cc6b3b0055fd#fluid400)

-------------

` `
` `

### What is Vizro?  

[Vizro](https://github.com/plotly/Vizro) is an open-source dashboarding framework developed by McKinsey. Built with Plotly and Dash, Vizro provides a high-level API for creating interactive, production-ready dashboards with minimal code. It includes pre-configured layouts, themes, and components, making it easier to build data-driven applications.  


Even if you're not creating a Vizro app, you can still use its styling and design system in your Dash applications.  

### Vizro Features Available for Dash Apps  

- **Vizro Bootstrap-themed figure templates** are available in the dash-bootstrap-templates library starting from version 2.1.0. Both dark and light-themed templates are included.  

- **Vizro Bootstrap theme** provides styling for Bootstrap components, allowing them to match the Vizro light or dark theme.  

- **Vizro theme for other Dash components** extends styling beyond Bootstrap. Vizro includes custom CSS to theme additional Dash components that are not part of Bootstrap. You can explore all the custom CSS files in their [GitHub repository](https://github.com/mckinsey/vizro/tree/main/vizro-core/src/vizro/static/css).  

- **Vizro KPI cards** like the ones shown in the image above can be added to a regular Dash app, bringing a visually consistent way to display key performance indicators. For more details, see this [Plotly forum post](https://community.plotly.com/t/introducing-new-kpi-cards-in-vizro-based-on-dbc/86711).  


### Vizro Bootstrap Figure Templates

Apply Vizro-themed styling to all Plotly figures in your Dash app. Learn more in the <dccLink href="/adding-themes/figure-templates" children="Figure templates section" /> 

Available in `dash-bootstrap-templates>=V2.1.0`

Make Vizro templates available in your app:
```
from dash_bootstrap_templates import load_figure_template
load_figure_template(["vizro", "vizro_dark"])
```


The default theme for all Plotly figures in the app will be "vizro" which is the light theme.  To change it to the "vizro_dark" theme:

```
fig=px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", size_max=60, color="continent", template="vizro_dark")

```
"""

theme_switch = """

### Vizro Bootstrap Theme

You can add the Vizro Bootstrap theme to your app like this:

```
pip install vizro>=0.1.34
```

```
import vizro
from dash import Dash
app = Dash(__name__, external_stylesheets=[vizro.bootstrap])

```
You can also use the Vizro Bootstrap theme without importing vizro in your app.  The `vizro.bootstrap` is a is a predefined URL that links to the Vizro Bootstrap CSS stylesheet.  To find the link you can use

```
print(vizro.bootstrap)
```

You can then use it in your app like this:

```
vizro_bootstrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@0.1.34/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css"
app = Dash(__name__, external_stylesheets=[vizro_bootstrap])

```
### Example: Vizro light dark color mode

![Vizro Theme switch](https://github.com/user-attachments/assets/ec8d3994-5619-4ad5-b5a8-c47574720677#fluid600)
"""

theme_change = """
### Adding Vizro theme to ThemeChangerAIO

If you would like to switch between multiple themes, use the <dccLink href="/adding-themes/theme-switch" children="ThemeChangerAIO component" />

By default this component includes the 26 themes available from the dash-bootstrap-components library.  If you would like
to add custom themes, like Vizo, you can use the `custom_themes` prop:

```

vizro_boostrap = "https://cdn.jsdelivr.net/gh/mckinsey/vizro@0.1.34/vizro-core/src/vizro/static/css/vizro-bootstrap.min.css"

theme_changer = ThemeChangerAIO(
    aio_id="theme",   
    custom_themes={'Vizro': vizro_boostrap},
)
```

"""


next = """
-----------------  

### Next:  
Adding a  <dccLink href="/adding-themes/theme-switch" children="Theme change component" />

"""


layout = html.Div(
    [
        dcc.Markdown(intro, dangerously_allow_html=True, className="mx-5 px-3"),
        example_app("vizro_figure_templates", make_layout=make_tabs),

        dcc.Markdown(theme_switch, dangerously_allow_html=True, className="mx-5 px-3"),
        html.Div(example_app(
            "vizro_theme_switch",
            make_layout=make_app_first,
            run=False,
        ), className="mx-4"),

        dcc.Markdown(theme_change, dangerously_allow_html=True, className="mx-5 px-3"),


        dcc.Markdown(
            next,
            className="m-5 px-3 dbc",
            dangerously_allow_html=True,
        ),

    ],
    className="dbc",
)

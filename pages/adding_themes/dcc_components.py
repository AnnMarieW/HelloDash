from dash import html, dcc, register_page

from lib.code_and_show import example_app, make_tabs
from lib.other_components import change_theme_alert
from lib.utils import app_description


register_page(
    __name__,
    order=1,
    description=app_description,
    title="Adding Themes/dcc",
    name="dash-core-components",
)

heading = """
## Dash Core Components with a Bootstrap Theme

Add this stylesheet to your app:
```
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])
```

Then add `className="dbc"`. 

That's it!  

So how does it work?  The style sheet uses component's CSS selectors and updates the style using Bootstrap
 variable names.  When the theme changes, the components are automatically updated based on the theme's named theme colors. 
  
Here's an example:

```css
.dbc .Select input {
  color: var(--bs-body-color);
}
```


#### Tips
- To see a [human readable stylesheet,](https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css) 
change the the url above to `/dbc.css` instead of `/dbc.min.css`. 
- If you add `className="dbc"` to the outer container of your app, you do not need to add it to every component.  See an
example in the <dccLink href="/adding-themes/getting-started" children="Getting Started" /> section.
- In the examples below, use the Theme Change button to see the components with different themes. You will see the biggest style difference in a dark theme.


### Examples
"""

docs_datepicker = """
Dash docs:  [dcc.DatePickerRange](https://dash.plotly.com/dash-core-components/datepickerrange)  [dcc.DatePickerSinge](https://dash.plotly.com/dash-core-components/datepickerrange)
"""


docs_sliders = """
Dash docs:  [dcc.Slider](https://dash.plotly.com/dash-core-components/slider)  [dcc.RangeSlider](https://dash.plotly.com/dash-core-components/rangeslider)
"""


docs_dropdown = """
Dash docs:  [dcc.Dropdown](https://dash.plotly.com/dash-core-components/dropdown) 
"""


docs_tabs = """
See also [dbc.Tabs](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tabs/) which are automatically styled with a Bootstrap theme.    

Note that the dcc.Tabs can also be styled using Bootstrap utility classes in the `className` prop
or CSS in the `style` prop.  See the Dash documentation [dcc.Tab](https://dash.plotly.com/dash-core-components/tab).
    """


docs_markdown = """
Dash docs:  [dcc.Markdown](https://dash.plotly.com/dash-core-components/markdown) 
"""


layout = html.Div(
    [
        change_theme_alert(auto_dismiss=False),
        dcc.Markdown(
            heading, link_target="_blank", dangerously_allow_html=True, className="p-4"
        ),
        example_app("dcc_slider", make_layout=make_tabs, notes=docs_sliders),
        example_app("dcc_dropdown_multi", make_layout=make_tabs, notes=docs_dropdown),
        example_app(
            "dcc_dropdown",
            make_layout=make_tabs,
            notes=docs_dropdown,
        ),
        example_app("dcc_datepickers", make_layout=make_tabs, notes=docs_datepicker),
        example_app("dcc_tabs", make_layout=make_tabs, notes=docs_tabs),
        example_app(
            "dcc_markdown", make_layout=make_tabs, notes=docs_markdown, show_code=False
        ),
    ]
)

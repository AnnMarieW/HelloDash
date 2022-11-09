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

intro = """
## Styling Dash Core Components with a Bootstrap Theme

To style Dash Core Components with a Bootstrap theme, simply add this stylesheet to your app:
```
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])
```

Then add `className="dbc"` to the component, or outer container of the app. 

That's it!  

So how does it work?  The stylesheet defines the "dbc" class.  It uses Bootstrap variable names --  so when the theme
 changes, the components are automatically updated based on the named theme colors. For example, this makes the dropdown
  options readable in both light and dark themes:

```css
/* dropdown menu options */
.dbc .VirtualizedSelectOption {
  background-color: var(--bs-body-bg);
  color: var(--bs-body-color);
}
```

--------------

` `  
` `  

#### Tips
- To see a [human readable stylesheet,](https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css) 
change the the url above to `/dbc.css` instead of `/dbc.min.css`. 
- To customize this stylesheet, download it and place it in a .css file in the `assets` folder.  More info in the [dash-docs](https://dash.plotly.com/external-resources)
- If you find a better way that works for all themes, please [open an issue](https://github.com/AnnMarieW/dash-bootstrap-templates/issues). Pull requests are welcome!

` `  
` `  

### Using the `"dbc"` class

You can add the `className="dbc"` to a component:
```
dcc.RangeSlider(0, 20, value=[5, 15], className="dbc")
```

If you add `className="dbc"` to the outer container of the app then it will apply to the entire app so you don't have to add it
to every component.  For example:
```
app.layout = dbc.Container(
    [
        ...
    ],
    fluid=True,
    className="dbc"
)
```
` `  
` `  

### Examples  

These apps show Dash Core Components both with and without a Bootstrap theme.  Try changing the theme --
 you'll see the biggest difference in dark themes.  See the code in the "view code" tab.
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

next = """

` `  
` `  


-----------------  

### Next:  
Apply Bootstrap theme to the Dash <dccLink href="/adding-themes/datatable" children="DataTable" />

"""

layout = html.Div(
    [

        dcc.Markdown(
            intro, link_target="_blank", dangerously_allow_html=True, className="mx-5 px-3"
        ),
        change_theme_alert(auto_dismiss=False),
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
        dcc.Markdown(
            next, dangerously_allow_html=True, className="mx-5 px-3"
        ),
    ]
)

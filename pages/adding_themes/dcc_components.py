from dash import html, register_page

from lib.code_and_show import example_app, make_tabs
from lib.other_components import change_theme_alert


register_page(__name__, order=1, description="", name="dash-core-components")

notes_first = """
## Dash Core Components with a Bootstrap Theme

Add `className="dbc"`  See the [TODO]() for more information.
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

Note that the dcc.Tabs are easy to customizable with inline styles or css.  
See the Dash documentation [dcc.Tab](https://dash.plotly.com/dash-core-components/tab).
    """


docs_markdown = """
Dash docs:  [dcc.Markdown](https://dash.plotly.com/dash-core-components/markdown) 
"""


layout = html.Div(
    [
        change_theme_alert(auto_dismiss=False),
        example_app(
            "dcc_dropdown",
            make_layout=make_tabs,
            notes_first=notes_first,
            notes=docs_dropdown,
        ),
        example_app("dcc_dropdown_multi", make_layout=make_tabs, notes=docs_dropdown),
        example_app("dcc_slider", make_layout=make_tabs, notes=docs_sliders),
        example_app("dcc_datepickers", make_layout=make_tabs, notes=docs_datepicker),
        example_app("dcc_tabs", make_layout=make_tabs, notes=docs_tabs),
        example_app(
            "dcc_markdown", make_layout=make_tabs, notes=docs_markdown, show_code=False
        ),
    ]
)

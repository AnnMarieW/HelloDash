from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_tabs, make_app_first
from lib.other_components import change_theme_alert, bootstrap_utils_alert
from lib.utils import app_description


register_page(
    __name__, order=5, description=app_description, title="Adding Themes/Utility Classes"
)

intro = dcc.Markdown("""
## Bootstrap utility classes
Bootstrap includes dozens of utility classes for showing, hiding, aligning, spacing and styling content. See all the Bootstrap classes at the Dash Bootstrap Cheatsheet site.

Bootstrap utility classes can be applied to any Dash component to quickly style them without the need to write custom CSS rules. Use the Bootstrap utility classes in the Dash component’s `className` prop.

For example, instead of using CSS in the `style` prop:
```
style={
    "backgroundColor": "blue",
    "padding": 16,
    "marginTop": 32,
    "textAlign": "center",
    "fontSize": 32,
}
```
You can use  Boostrap utilities in the `className` prop:
```
className="bg-primary p-1 mt-2 text-center h2",
```
""")

alerts = html.Div(
    [
        change_theme_alert(auto_dismiss=False),
        bootstrap_utils_alert
    ], className="hstack gap-3"
)

examples =dcc.Markdown("""
## Examples
Here are just a few examples to get you started.  See all the utility classes in the [Dash Boostrap Cheatsheet!](https://dashcheatsheet.pythonanywhere.com/)
""",  link_target="_blank")


layout = html.Div(
    [
        alerts,
        intro,

        example_app("utl_interactive", make_layout=make_app_first, show_code=False ),
        examples,
        example_app("utl_color_text", make_layout=make_tabs),
        example_app("utl_color_bg", make_layout=make_tabs),
        example_app("utl_color_bg_opacity", make_layout=make_tabs),
        example_app("utl_spacing", make_layout=make_tabs),
    ],
)

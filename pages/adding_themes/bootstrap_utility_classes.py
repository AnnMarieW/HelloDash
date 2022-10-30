



# bg-secondary text-primary  fs-1 fw-bold p-4 text-center
# m-4 w-50 rounded-pill border border-primary border-4

from dash import html, dcc, register_page
import dash_bootstrap_components as dbc

from lib.code_and_show import example_app, make_tabs, make_app_first
from lib.other_components import change_theme_alert, bootstrap_utils_alert
from lib.utils import app_description


register_page(
    __name__, order=6, description=app_description, title="Adding Themes/Dash Bootstrap Utility Classes",
    name="Bootstrap Utility Classes"
)

intro = dcc.Markdown("""
## Bootstrap utility classes
Bootstrap includes dozens of utility classes for showing, hiding, aligning, spacing and styling content. See all the Bootstrap classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/).

Bootstrap utility classes can be applied to any Dash component to quickly style them without the need to write custom CSS rules. Just add them to the Dash component’s `className` prop.

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
You can use  Bootstrap utilities in the `className` prop:
```
className="bg-primary p-1 mt-2 text-center h2",
```
""", className="mx-5 px-3")






alerts = html.Div(
    [
        change_theme_alert(auto_dismiss=False),
        bootstrap_utils_alert
    ], className="hstack gap-3"
)

examples =dcc.Markdown("""
### Bootstrap Utility Classes Examples
Here are just a few to get you started.  See all the utility classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/)
""",  link_target="_blank", className="mx-5 px-3")

footer = dcc.Markdown("""
#### See all the utility classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/)
""",  link_target="_blank", className="m-5 px-3")

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
        example_app("utl_border", make_layout=make_tabs),
        example_app("utl_text_align", make_layout=make_tabs),
        example_app("utl_text", make_layout=make_tabs),
        footer

    ],
)

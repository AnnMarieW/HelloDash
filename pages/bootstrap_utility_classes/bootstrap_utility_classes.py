
from dash import html, dcc, register_page
from lib.code_and_show import example_app, make_tabs, make_app_first
from lib.other_components import change_theme_alert, bootstrap_utils_alert
from lib.utils import app_description
import pages.bootstrap_utility_classes.bootstrap_utility_classes_md as md_text


register_page(
    __name__, order=6, description=app_description, title="Dash Bootstrap Utility Classes",
    name="Bootstrap Utility Classes", hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
    redirect_from=["/adding-themes/bootstrap-utility-classes"]
)

def make_md(text):
    return dcc.Markdown(text, className="mx-5 px-3")


alerts = html.Div(
    [
        change_theme_alert(auto_dismiss=False),
        bootstrap_utils_alert
    ], className="hstack gap-3"
)

examples =dcc.Markdown("""
### Bootstrap Utility Classes Examples
Here are a few utility classes to get you started.  See all the utility classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/)
""",  link_target="_blank", className="mx-5 px-3")


summary = dcc.Markdown("""
#### See all the utility classes in the [Dash Bootstrap Cheatsheet](https://dashcheatsheet.pythonanywhere.com/)
""",  link_target="_blank", className="m-5 px-3")

up_next = dcc.Markdown(
    md_text.next,
    className="m-5 px-3 dbc",
    dangerously_allow_html=True,
)

layout = html.Div(
    [
        html.Div(id="intro"),
        alerts,
        make_md(md_text.intro),
        example_app("utl_interactive", make_layout=make_app_first, show_code=False ),
        examples,

        html.Div(id="background"),
        example_app("utl_color_bg", make_layout=make_tabs),

        html.Div(id="border"),
        example_app("utl_border", make_layout=make_tabs),
        example_app("utl_color_bg_opacity", make_layout=make_tabs),

        html.Div(id="color"),
        example_app("utl_color_text", make_layout=make_tabs),

        html.Div(id="spacing"),
        example_app("utl_spacing", make_layout=make_tabs),

        html.Div(id="text"),
        example_app("utl_text_align", make_layout=make_tabs),
        example_app("utl_text", make_layout=make_tabs),

        html.Div(id="position"),
        make_md(md_text.arrange_elements_intro),
        example_app("utl_position"),
        make_md(md_text.translate_middle_intro),
        example_app("utl_position_translate_middle"),
        make_md(md_text.translate_middle_xy_intro),
        example_app("utl_position_translate_middle_xy"),
        example_app("utl_position_examples", make_layout=make_tabs),
        example_app("utl_position_example2", make_layout=make_tabs),
        summary,
        up_next,

    ],
)

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import util


# intro ------------------------------------------------------------------

intro = dcc.Markdown(
    """
The `dash-bootstrap-template` library has **Two [All-in-One](https://dash.plotly.com/all-in-one-components) components** to change themes in a Dash app.
  - `ThemeSwitchAIO` toggles between two themes. 
  - `ThemeChangerAIO` select from multiple themes.

We use the `ThemeChangerAIO` in this app to demonstrate all the themes available.  See the `ThemeSwitchAIO` to toggle 
between a light and a dark theme.
    """
)
intro_md = dbc.Alert(intro, color="primary", className="p-2")


# ThemeChangerAIO ------------------------------------------------------------------

ThemeChangerAIO_code = util.get_code_file("demo_theme_changer_all.py")
ThemeChangerAIO_code_card = util.make_code_card(
    ThemeChangerAIO_code, id="ThemeChangerAIO_code", height=450
)

ThemeChangerAIO_intro = dcc.Markdown(
    """
Below you will find a minimal example of changing themes with the ThemeChangerAIO component.  Use this component when you would
like to select from multiple themes.  This example demos how to:
 - update the figure for the new theme in a callback
 - change the starting theme (The default for the component is "BOOTSTRAP")
 - add the "dbc" class to apply Bootstrap themes to Dash components. 
  
Note that the ThemeChangerAIO component updates the stylesheet for the theme, and all the Dash and Dash Boostrap Components
 are updated, however the figures must be updated in a callback in order to render with the new Bootstrap-themed 
 figure template.  
 
 To get the currently selected theme, you can access the `value` prop of the radio buttons in the theme changer in a 
  callback like this:
  ```
  Input(ThemeChangerAIO.ids.radio("theme"), "value")
  ```
 The `value` is the url of the selected theme.  Use the helper function `template_from_url` to get the name of the
 Bootstrap-themed Plotly figure template.
 
 ```
 template=template_from_url(theme)
 ```
    """
)


# ThemeSwitchAIO ------------------------------------------------------------------


ThemeSwitchAIO_code = util.get_code_file("demo_toggle.py")
ThemeSwitchAIO_code_card = util.make_code_card(
    ThemeSwitchAIO_code, id="ThemeSwitchAIO_code", height=450
)

ThemeSwitchAIO_intro = dcc.Markdown(
    """    
Below you will find a minimal example of changing themes with the `ThemeSwitchAIO` component.  Use this component when you would
like to switch between two themes.  This example demos how to:
 - update the figure for the new theme in a callback 
 - add the "dbc" class to apply Bootstrap themes to Dash components. 
    """
)
ThemeSwitchAIO_image = dcc.Markdown(
    """
![theme_toggle1](https://user-images.githubusercontent.com/72614349/143920785-62217d9c-1bbb-4a51-bda4-b943b690609d.gif)
    """
)


# ThemeSwitchAIO example 2 ------------------------------------------------------------------


ThemeSwitchAIO_icons_code = util.get_code_file("demo_toggle_icons.py")
ThemeSwitchAIO_code_icons_card = util.make_code_card(
    ThemeSwitchAIO_icons_code, id="ThemeSwitchAIO_icons_code", height=450
)

ThemeSwitchAIO_icons_intro = dcc.Markdown(
    """        
The ThemeSwitchAIO component updates the Plotly default figure template when the
theme changes, but the figures must be updated in a callback in order to render with the new template.

This example demos:
 - how to update the figure for the new theme in a callback
 - how to use different icons to the left and right of the toggle switch.
 - using the Bootstrap icons rather than the default FontAwesome icons.
 - add the "dbc" class to apply Bootstrap themes to Dash components. 
    """
)


ThemeSwitchAIO_icon_image = dcc.Markdown(
    """
![theme_toggle2](https://user-images.githubusercontent.com/72614349/143920794-7ecca2c2-45ff-424a-a34e-e4bf435eb22f.gif)
    """
)


# Reference ------------------------------------------------------------------

reference = dcc.Markdown(
    """

## ThemeChangerAIO Reference
**ThemeChangerAIO** is an All-in-One component  composed  of a parent `html.Div` with
the following components as children:

- `dbc.Button` ("`switch`") Opens the Offcanvas component for user to select a theme.
- `dbc.Offcanvas` ("`offcanvas`")
- `dbc.RadioItems` ("`radio`").  The themes are displayed as RadioItems inside the `dbc.Offcanvas` component.
  The `value` is a url for the theme
- `html.Div` is used as the `Output` of the clientside callbacks.

The ThemeChangerAIO component updates the stylesheet  when the `value` of radio changes. (ie the user selects a new theme)

- param: `radio_props` A dictionary of properties passed into the dbc.RadioItems component. The default `value` is `dbc.themes.BOOTSTRAP`
- param: `button_props`  A dictionary of properties passed into the dbc.Button component.
- param: `offcanvas_props`. A dictionary of properties passed into the dbc.Offcanvas component
- param: `aio_id` The All-in-One component ID used to generate components' dictionary IDs.

The All-in-One component dictionary IDs are available as:

- ThemeChangerAIO.ids.radio(aio_id)
- ThemeChangerAIO.ids.offcanvas(aio_id)
- ThemeChangerAIO.ids.button(aio_id)
    

## ThemeSwitchAIO Reference

**ThemeSwitchAIO** is an All-in-One component  composed  of a parent `html.Div` with the following components as children:

- `dbc.Switch` ("`switch`") with icons to the left and right of the switch.
- `dcc.Store` ("`store`") The `themes` are stored in the `data` prop.
- `html.Div` is used as the `Output` of the clientside callbacks.

The ThemeSwitchAIO component updates the stylesheet when triggered by changes to the `value` of `switch` or when
the themes are updated in the "`store`" component.  The themes in the switch may be updated in a callback
by changing the theme urls in the "`store`" component.

- param: `themes` A list of two urls for the external stylesheets. The default is `[dbc.themes.CYBORG, dbc.themes.BOOTSTRAP]`.
- param: `icons`  A dict of the icons to the left and right of the switch. The default is  
  `{"left" :"fa fa-moon", "right" :"fa fa-sun"}`.
- param: `aio_id` The All-in-One component ID used to generate component's dictionary IDs.

The All-in-One component dictionary IDs are available as
- ThemeSwitchAIO.ids.switch(aio_id)
- ThemeSwitchAIO.ids.store(aio_id)    
    """
)


# layout ------------------------------------------------------------------

layout = html.Div(
    [
        util.make_header("Theme Change Components", spacing=""),
        intro_md,
        util.make_header("ThemeChangerAIO"),
        ThemeChangerAIO_intro,
        ThemeChangerAIO_code_card,
        util.make_header("ThemeSwitchAIO"),
        ThemeSwitchAIO_intro,
        ThemeSwitchAIO_code_card,
        ThemeSwitchAIO_image,
        util.make_header("ThemeSwitchAIO with Bootstrap icons"),
        ThemeSwitchAIO_icons_intro,
        ThemeSwitchAIO_code_icons_card,
        ThemeSwitchAIO_icon_image,
        reference,
    ],
    className="dbc pb-4",
)

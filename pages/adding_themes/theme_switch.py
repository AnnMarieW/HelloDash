from dash import html, register_page
from lib.code_and_show import example_app, make_app_first
from lib.utils import app_description

register_page(
    __name__,
    order=5,
    description=app_description,
    title="Adding Themes/Theme Change Components",
    name="Theme change components",
    redirect_from=["/theme_change_components"],
)



notes_first = """
## Adding a Theme Switch component

The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library has **Two  [All-in-One](https://dash.plotly.com/all-in-one-components) components** to change themes in a Dash app.
  - `ThemeSwitchAIO` toggles between two themes. 
  - `ThemeChangerAIO` select from multiple themes.

This example shows how to use the `ThemeSwitchAIO`  

👈 To add `ThemeChangerAIO`, like in this Theme Explorer app, see the <dccLink href="/" children="Sample App" />

----------


![theme_toggle](https://user-images.githubusercontent.com/72614349/141466191-13709102-a2fb-45b5-a984-383d3e6ab373.gif)
----------
"""


customize = """
## Customizing a theme change component

You can customize the `ThemeSwitchAIO` and the `ThemeChangerAIO` by passing props in a dict to the underlying components.
See the reference section below for more details and see the `dash-bootstraps-components` docs for information on the props 
available for each component.

For example, you can set `persistence=True` in the underlying `dbc.RadiioItems` component in the `ThemeChangerAIO`:

```python
ThemeChangerAIO(aio_id="theme", radio_props={"persistence": True})
```
Here isn an example of how to customize the "theme change" button:

```
ThemeChangerAIO(
    aio_id="theme",
    button_props={
        "color": "danger",
        "children": "select theme",
    },
)
```

This ThemeChangerAIO will open the `Offcanvas` component on the bottom of the screen:

```
ThemeChangerAIO(aio_id="theme", offcanvas_props={"placement":"bottom"})
```

Change the icons in the theme switch component to Bootstrap icons instead of the default FontAwesome icons like this:

```
 ThemeSwitchAIO(
    aio_id="theme",
    icons={"left": "bi bi-moon", "right": "bi bi-sun"},
),
```



"""


reference = """
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


layout = html.Div(
    example_app(
        "theme_switch",
        make_layout=make_app_first,
        notes_first=notes_first,
        notes=customize + reference,
        run=False,
    ),
    className="dbc",
)

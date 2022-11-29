


from dash import html, dcc, register_page
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

intro = """
## Theme Change Components 

The [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library has **Two  [All-in-One](https://dash.plotly.com/all-in-one-components) components** to change themes in a Dash app.
  - `ThemeSwitchAIO` toggles between two themes. 
  - `ThemeChangerAIO` select from multiple themes.
  
---------------
` `  
` `  
### ThemeSwitchAIO  Example 1

Below is a minimal example of switching between two themes, Cosmo and Cyborg. When the switch is `True` it will use the
 first theme, `dbc.themes.COSMO`. Here is how the theme switch component is defined:
```
ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.CYBORG])
```

This example demos:
 - switching between two themes
 - updating the figure for the new theme in a callback.  Note that the figure template names are the theme names in all lower
  case. See more information in the  <dccLink href="/adding-themes/figure-templates" children="Figure templates" /> section
 - making the first theme the same as the theme in the `external_stylesheets`
   
-----------------------
` `  
` `  

![simple_theme_switch](https://user-images.githubusercontent.com/72614349/198901305-7d4a7c87-4917-4200-8b7a-08cc8955464e.gif#fluid600)
"""





theme_switch_example2 = """

### ThemeSwitchAIO Example 2

Here is a another minimal example of the ThemeSwitchAIO component

This example demos:
 - using variable names for the figure templates and themes
 - updating the figure for the new theme in a callback
 - adding the stylesheet from dash-bootstrap-templates to style `dash-core-components` and the `DataTable` with a Bootstrap Theme
 
----------
` `  
` `  

![theme_toggle](https://user-images.githubusercontent.com/72614349/141466191-13709102-a2fb-45b5-a984-383d3e6ab373.gif#fluid600)

----------
` `  
` `  

"""






theme_change1 = """
### ThemeChangerAIO Example 1

Here is a simple example to show how to use the `ThemeChangerAIO` component.  It's the same app as the first theme switch
example, but instead of toggling two themes, you can select any theme.

We start by importing the `ThemeChangerAIO` component and the `template_from_url` function from the `dash-bootstrap-templates` library.
 The `template_from_url` function returns the name of the template based on the current theme.  We use this in the callback to update the figure template.

```
from dash_bootstrap_templates import ThemeChangerAIO, template_from_url
```

The theme change component is simply defined as: 
```
ThemeChangerAIO(aio_id="theme")
```
![changer-simple](https://user-images.githubusercontent.com/72614349/198904509-62b65af4-3eca-473b-a8e6-656ed8fa0431.gif#fluid600)

-----------
"""


theme_change2 = """

### ThemeChangerAIO Example 2
👈 See the <dccLink href="/" children="Sample App" /> section for another example for the `ThemeChangerAIO` component.
This one shows how to update the `dash-core-components` and the `DataTable` with a Bootstrap theme as well.
"""






customize = """
` `  
` `  

## Customizing theme change components

You can customize the `ThemeSwitchAIO` and the `ThemeChangerAIO` by passing props in a dict to the underlying components.
See the reference section below for more details and see the `dash-bootstraps-components` docs for information on the props 
available for each component.  Here are just a few examples:

#### Persistence
You can set `persistence=True` in the underlying `dbc.RadioItems` component in the `ThemeChangerAIO`:

```python
ThemeChangerAIO(aio_id="theme", radio_props={"persistence": True})
```

Set the `persistence=True` in the underlying `dbc.Switch` component in the `ThemeSwitchAIO`:
```
ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.COSMO, dbc.themes.CYBORG], switch_props={"persistence":True})
```

#### Styling the button
Here's an example of customizing the "Change Theme" button:

```
ThemeChangerAIO(
    aio_id="theme",
    button_props={
        "color": "danger",
        "children": "select theme",
    },
)
```
  
#### ThemeChangerAIO menu position
This ThemeChangerAIO will open the `Offcanvas` component on the bottom of the screen:

```
ThemeChangerAIO(aio_id="theme", offcanvas_props={"placement":"bottom"})
```
  
#### Changing ThemeSwitchAIO Icons
Change the icons in the theme switch component to Bootstrap icons instead of the default FontAwesome icons like this:

```
 ThemeSwitchAIO(
    aio_id="theme",
    icons={"left": "bi bi-moon", "right": "bi bi-sun"},
),
```

If you are starting with a dark theme, swap the position of the icons:

```
 ThemeSwitchAIO(
    aio_id="theme",
    icons={"left": "bi bi-sun", "right": "bi bi-moon"},
),
```
` `  
` `  
"""


reference = """
## ThemeChangerAIO Reference
**ThemeChangerAIO** is an All-in-One component  composed  of a parent `html.Div` with
the following components as children:

- `dbc.Button` ("`switch`") Opens the Offcanvas component for user to select a theme
- `dbc.Offcanvas` ("`offcanvas`")
- `dbc.RadioItems` ("`radio`").  The themes are displayed as RadioItems inside the `dbc.Offcanvas` component
  The `value` is a url for the theme
- `html.Div` is used as the `Output` of the clientside callbacks

The `ThemeChangerAIO` component updates the stylesheet  when the `value` of radio changes. (i.e. the user selects a new theme)

- param: `radio_props` A dictionary of properties passed into the dbc.RadioItems component. The default `value` is `dbc.themes.BOOTSTRAP`
- param: `button_props`  A dictionary of properties passed into the dbc.Button component
- param: `offcanvas_props`. A dictionary of properties passed into the dbc.Offcanvas component
- param: `aio_id` The All-in-One component ID used to generate components' dictionary IDs

The All-in-One component dictionary IDs are available as:

- `ThemeChangerAIO.ids.radio(aio_id)`
- `ThemeChangerAIO.ids.offcanvas(aio_id)`
- `ThemeChangerAIO.ids.button(aio_id)`
    

## ThemeSwitchAIO Reference

**ThemeSwitchAIO** is an All-in-One component  composed  of a parent `html.Div` with the following components as children:

- `dbc.Switch` ("`switch`") with icons to the left and right of the switch.
- `dcc.Store` ("`store`") The `themes` are stored in the `data` prop.
- `html.Div` is used as the `Output` of the clientside callbacks.

The ThemeSwitchAIO component updates the stylesheet when triggered by changes to the `value` of `switch` or when
the themes are updated in the "`store`" component.  The themes in the switch may be updated in a callback
by changing the theme urls in the "`store`" component.

- param: `switch_props` A dictionary of properties passed into the dbc.Switch component.
- param: `themes` A list of two urls for the external stylesheets. 
- param: `icons`  A dict of the icons to the left and right of the switch. The default is  
  `{"left" :"fa fa-moon", "right" :"fa fa-sun"}`.
- param: `aio_id` The All-in-One component ID used to generate component's dictionary IDs.

The All-in-One component dictionary IDs are available as
- ThemeSwitchAIO.ids.switch(aio_id)
- ThemeSwitchAIO.ids.store(aio_id)
"""



next = """
-----------------  

### Next:  
Using  <dccLink href="/bootstrap-utility-classes/bootstrap-utility-classes" children="Bootstrap Utility Classes" />

"""


layout = html.Div(
    [
       # dcc.Markdown(intro, dangerously_allow_html=True, className="mx-5 px-3 img-fluid"),
        html.Div(example_app(
            "theme_switch1",
            make_layout=make_app_first,
            notes_first=intro,
            run=False,
        ), className="mx-4"),
        html.Div(example_app(
            "theme_switch2",
            make_layout=make_app_first,
            notes_first=theme_switch_example2,
            run=False,
        ), className="mx-4"),
        html.Div(example_app(
            "theme_change1",
            make_layout=make_app_first,
            notes_first=theme_change1,
            run=False,
        ), className="mx-4"),
        dcc.Markdown(theme_change2, dangerously_allow_html=True, className="m-5 p-3"),
        dcc.Markdown(customize + reference, dangerously_allow_html=True, className="mx-5 px-3"),
        dcc.Markdown(
            next,
            className="m-5 px-3 dbc",
            dangerously_allow_html=True,
        ),


    ],
    className="dbc my-4",
)


from dash import html, dcc, register_page
from lib.code_and_show import example_app, make_app_first
from lib.utils import app_description

register_page(
    __name__,
    order=6,
    description=app_description,
    title="Adding Themes/Light Dark Color Modes",
    name="Light Dark Color Modes",
)

intro = """
## Bootstrap Light & Dark Color Modes

---------------
  
  
__New in Dash Bootstrap Components 1.5.0 & Dash Bootstrap Templates V1.1.0__

Now it's  easier than ever to switch between light and dark modes in your Dash app using
 [Bootstrap Color Modes](https://getbootstrap.com/docs/5.3/customize/color-modes/).  You can set the color mode
  globally or on specific components and elements, by using the `data-bs-theme` attribute.

    
---------------
` `  
` `  



## Setting Color Modes 

` `  
` `  

### Setting Dark mode globally

You can set a dark version of your Bootstrap theme globally.  Do this if you __do not__ want to toggle between light
 and dark. Simply add the following to a `.js` file in the `/assets` folder:


```js
document.documentElement.setAttribute('data-bs-theme', 'dark')
```
This gives you even more dark themes to choose from as it can set a dark mode for any theme.  For example, you can
 have a dark mode for any of the 26 themes available in the `dash-bootstrap-components` library.


` `  
` `  

### Light Dark Color Mode Toggle

You can change the global color mode for a theme by using a component to trigger a clientside callback.  

For example, here is  the color mode switch component shown in Example 1 below:

```python

color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)

```

And here's the callback to change the theme:

```python

clientside_callback(
    " " " 
    (switchOn) => {
       switchOn
         ? document.documentElement.setAttribute('data-bs-theme', 'light')
         : document.documentElement.setAttribute('data-bs-theme', 'dark')
       return window.dash_clientside.no_update
    }
    " " ",
    Output("switch", "id"),
    Input("switch", "value"),
)

```


---------------
` `  
` `  
### Light Dark Color Mode  Example 1

This example shows the  "minty" theme in either light or dark mode. It shows how to use the theme switch and clientside
 callback shown above to update the global theme of the app.  It also shows how to change the theme of the figure
  by updating the figure template in a callback.


![color-mode-templates](https://github.com/AnnMarieW/HelloDash/assets/72614349/eea89279-c4fb-4ae1-ae47-ffae79d1052f#fluid)

"""


more_details = """

---------------
` `  
` `  

### Setting dark or light mode on components

After setting a global theme, it's possible to use a different color mode on individual components by setting the `data-bs-theme` attribute on a `html.Div` container.


Here is a `dbc.Card` in dark  mode:


```python
html.Div(
    [
        dbc.Card( # card content here)
    ]
    id="card",
    **{"data-bs-theme": "dark"}
)
```
Here is a card with a light mode
```python

html.div(
    [
        dbc.Card( # card content here)
    ]
    id="card",
    **{"data-bs-theme": "light"}
)
```
You can even change the color mode in a callback:

```
app.callback(
    Output("card", "data-bs-theme").
    ...
```

---------------
` `  
` `  
##  Applying Bootstrap themes to other component libraries

The Bootstrap theme is automatically applied __only__ to `dbc` components.  If you are using other libraries
 like `dash-core-components`, `DataTable`, `dash-ag-grid` you need to style them separately.  To save some time, you can
  use the stylesheet from the `dash-bootstrap-templates` library.  For more information, see
    <dccLink href="/adding-themes/dcc-components" children="Applying Themes" /> section.


---------------
` `  
` `  
## Applying Bootstrap themes to figures
When you change the color mode, the figures are not updated automatically.  One option is to update the figure template in
 a callback.  The built-in "plotly_white" and "plotly_dark" figure templates look nice with most Bootstrap themes.  If
  you would like your figures to have a closer match to your Bootstrap theme, you can use one of the 52 Bootstrap themed
   figure templates from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
  For more information see the <dccLink href="/adding-themes/figure-templates" children="Figure Templates" /> section.

The dash-bootstrap-templates >= V1.1.0  has a dark and light version of each of the 26 Bootstrap themes in the dbc
 library.
 
 
 
---------------
` `  
` `  
## Theme Change Components
 
If you would like to toggle between a light and a dark mode of your selected Bootstrap theme, then using the color
 modes as described above is the best method. However, if you would like to switch between two or more completely
  different themes (for example switch between "cyborg" and "minty" themes) then you can use the components as
   described in the <dccLink href="/adding-themes/theme-switch" children="Theme change component" /> section.
     

"""




next = """
-----------------  

### Next:  
Using  <dccLink href="/bootstrap-utility-classes/bootstrap-utility-classes" children="Bootstrap Utility Classes" />

"""


layout = html.Div(
    [

        html.Div(example_app(
            "color_modes",
            make_layout=make_app_first,
            notes_first=intro,
            run=False,
        ), className="mx-4"),
        dcc.Markdown(more_details, dangerously_allow_html=True, className="m-5 p-3"),

        dcc.Markdown(
            next,
            className="m-5 px-3 dbc",
            dangerously_allow_html=True,
        ),


    ],
    className="dbc my-4",
)

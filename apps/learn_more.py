import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

import pathlib

# set relative path
PATH = pathlib.Path(__file__).parent
APPS_PATH = PATH.joinpath(".").resolve()


"""
===============================================================================
Markdown Text
"""


with open(APPS_PATH.joinpath("sample_app_1.py")) as f:
    code = f.read()
example_app_code = f"```{code}```"


app_notes1 = dcc.Markdown(
    """

## These two images are the same app!  Only 5 lines are changed to set a different theme.


|Light Theme app     | Dark Theme app |
| ----------- | ----------- |
| ![minty](https://user-images.githubusercontent.com/72614349/108880577-aa390900-75bf-11eb-8cb2-d246b342f4b5.png#thumbnail) | ![dark](https://user-images.githubusercontent.com/72614349/108880544-a1483780-75bf-11eb-913d-09c10adbe537.png#thumbnail) |
| __Boostrap Theme:__ MINTY | DARKLY
| __Graph Template:__ simple_white | plotly_dark|
| __Graph Color Sequences:__ Pastel | Dark24|
| __Graph Continuous Colorscales:__ darkmint | ice|
| __App Background Color:__ #F3F6F3 | ""|

------
"""
)


app_notes2 = dbc.Card(
    dcc.Markdown(
        """

### Bootstrap Themes
This app makes it easy to see how a Bootstrap or [Bootswatch theme](https://www.bootstrapcdn.com/bootswatch/)
 will look in your Dash app.  Choose from one of 22 Bootstrap themes - or even create your own.   

Note that the light Bootstrap themes are the easiest themes to use with Dash.  The Dash components have a light 
background color and that works well with the Bootswatch light themes.  A dark theme will set the text color to 
white or some other light color making the text hard to read in some Dash components. 

 Here are some way to change the colors in Dash components:
-  Dash Core Components:  Try using the `className` or `style` parameter of the component or use the inspector in the browser to see how the colors are set and override it with custom CSS in the assets folder. 
See more information [here](https://dash.plotly.com/external-resources).   See the css we used here [ github link](https://github.com/AnnMarieW/HelloDash/blob/main/assets/mycss.css) 
-  Dash DataTables:  See how to set a dark theme [here](https://dash.plotly.com/datatable/style) in the Dash documentation
-  Dash DAQ components: Use the `theme` parameter:   `theme= {'dark': True}`
-  Figures: Use the [Graph template](https://plotly.com/python/templates/)  `plotly_dark`


### Graph Templates

Setting the Plotly graph template is a quick way to set the style of the figure  in your app.  Try selecting one of 
the 11 standard templates to see how they look with your  Boostrap themes.  Note that the  "plotly_dark" template 
works well with Bootstrap  dark themes.

The templates  can also be used to  can pre-populate a figure with visual elements like annotations, shapes,
images, and more. Learn more about Plotly templates and how to customize them [here](https://plotly.com/python/templates/)

### Discrete Colors & Continuous Colorscales

Selecting the Plotly trace colors that look nice with your selected Boostrap theme can really enhance your app design.
See the Dash documentation to learn more about [discrete colors](https://plotly.com/python/discrete-color/) and 
[continuous colorscaless](https://plotly.com/python/colorscales/)
"""
    ),
    className="m-4 p-4",
)


source_code = dcc.Markdown(
    """ 
## Source code
The code for the sample app is also available in the [GitHub](https://github.com/AnnMarieW/HelloDash).


"""
    + example_app_code,
    style={"backgroundColor": "white", "color": "black", "padding": 20},
)

layout = dbc.Container(
    [
        html.H1("Sample Apps and Source Code", className="bg-primary text-white mb-4"),
        dbc.Row(dbc.Col([app_notes2, app_notes1, source_code])),
    ]
)

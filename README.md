# HelloDash
## See this app at:  https://hellodash.pythonanywhere.com/

Note - this site is under active development and there will be frequent breaking changes.  If you have any suggestions
for improvements or features to add, I'd be delighted to hear from you!  Please don't hesitate to open an issue, or
create a pull request.  And of course I accept positive feedback too :-)

The purpose of this app is to help you see how different Bootstrap and Bootswatch themes, Plotly figure templates and colors 
will look in your Dash app.  

When you decide on a scheme you like, you can take note of the settings and add them into your own app, or use one of the
sample apps to get started.  So far there is only one sample app, but I have plans to add several more.  

-------------
------------

## The Theme Explorer helps you create a design theme for your Dash app

Choose from:
 - 22 [Boostrap Bootswatch themes](https://www.bootstrapcdn.com/bootswatch/)
 - 11 [Plotly Graph Templates](https://plotly.com/python/templates/)
 - 18 [Plotly Graph Discrete Color Sequences](https://plotly.com/python/builtin-colorscales/#discrete-color-sequences)
 - 94 [Plotly Graph Continuous Colorscales](https://plotly.com/python/builtin-colorscales/)
 - Any background color selected from a colorpicker


-------------


![theme](https://user-images.githubusercontent.com/72614349/108897468-5f28f100-75d3-11eb-9f5f-095315cc1516.gif)

--------------
---------------

### These two images are the same app!  Only 5 lines are changed to set a different theme.



|Light Theme app     | Dark Theme app |
| ----------- | ----------- |
| ![minty](https://user-images.githubusercontent.com/72614349/108880577-aa390900-75bf-11eb-8cb2-d246b342f4b5.png#thumbnail) | ![dark](https://user-images.githubusercontent.com/72614349/108880544-a1483780-75bf-11eb-913d-09c10adbe537.png#thumbnail) |
| __Boostrap Theme:__ MINTY | DARKLY
| __Graph Template:__ simple_white | plotly_dark|
| __Graph Color Sequences:__ Pastel | Dark24|
| __Graph Continuous Colorscales:__ darkmint | ice|
| __App Background Color:__ #F3F6F3 | ""|



------
-------


The light Bootstrap themes are the easiest themes to add to your Dash app.  The Dash components have a light background color and that works well with the Bootswatch light themes.

A dark theme will set the text color to white or some other light color making the text  hard  to read in some Dash components. Here are some way to change the colors:
-  Dash Core Components:  Try using the `className` or `style` parameter of the component or use the inspector in the browser to see how the colors are set and override it with custom CSS in the assets folder. 
See more information [here](https://dash.plotly.com/external-resources).   See the css we used here [ github link](https://github.com/AnnMarieW/HelloDash/blob/main/assets/mycss.css) 
-  Dash DataTables:  See how to set a dark theme [here](https://dash.plotly.com/datatable/style) in the Dash documentation
-  Dash DAQ components: Use the `theme` parameter:   `theme= {'dark': True}`
-  Figures: Use the [Graph template](https://plotly.com/python/templates/)  `plotly_dark`

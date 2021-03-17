# HelloDash
## See this app at:  https://hellodash.pythonanywhere.com/

Note - this site is under active development and there will be frequent breaking changes.  If you have any suggestions
for improvements or features to add, I'd be delighted to hear from you!  Please don't hesitate to open an issue, or
create a pull request.  And of course I accept positive feedback too :-)

The purpose of this app is to help you see how different Bootstrap and Bootswatch themes, Plotly figure templates and colors 
will look in your Dash app.  

When you decide on a scheme you like, you can take note of the settings and add them into your own app, or use one of the
sample apps to get started. 

See the app gallery for more examples.  If you have an app that you would like to include in the gallery, please open
an [issue](https://github.com/AnnMarieW/HelloDash/issues) and include the following information:

1) An image of your app
2) A short title to appear on the card in the gallery
3) A link to the Github/GitLab ect for your code
4) An extended description of your app.  This will be displayed in a dcc.Markdown component, so feel free to include any
compatible Markdown formatting and links etc.
   


-------------
------------

## The Theme Explorer helps you create a design theme for your Dash app

Choose from:
 - 22 [Boostrap Bootswatch themes](https://www.bootstrapcdn.com/bootswatch/)
 - 11 [Plotly Graph Templates](https://plotly.com/python/templates/)
 - 18 [Plotly Graph Discrete Color Sequences](https://plotly.com/python/builtin-colorscales/#discrete-color-sequences)
 - 94 [Plotly Graph Continuous Colorscales](https://plotly.com/python/builtin-colorscales/)
 - Any background color selected from a colorpicker


------------

![Peek 2021-03-17 06-57](https://user-images.githubusercontent.com/72614349/111480344-228e7800-86ef-11eb-9ac9-32740c1fab1e.gif)

--------------
---------------

### These two images are the same app!  Only 1 line of code is changed to set a different theme.



|Light Theme app     | Dark Theme app |
| ----------- | ----------- |
| ![theme_explorer_light](https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.png#thumbnail) | ![theme_explorer_dark](https://user-images.githubusercontent.com/72614349/109723317-28228480-7b6b-11eb-8a50-0ac06ec2bca1.png#thumbnail) |
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

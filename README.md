# HelloDash

## Dash Bootstrap Theme Explorer 
#### The Easy way to see Bootstrap themes and Plotly templates and colors in your Dash app

#### See it at:  https://hellodash.pythonanywhere.com/



 - The __Theme Explorer App__ makes it easy to see how different Bootstrap themes, Plotly figure templates and colors 
will look in your Dash app.  
   
   
 - The __Component Gallery__ shows a sample of all the components available from the dash-bootstrap-components library,
   dash-core-components, and the Dash DataTable. (Dash DAQ coming soon!) You can see how the style of the component changes when you change the
   Bootstrap theme.   For the DataTable and some Dash Core Components, there are examples of how to 
   use the `style` and `className` properties and custom CSS to make them look great with your selected theme.  
   
   
- The __App Gallery__ has examples of Dash Apps made with Bootstrap.  Add your app to the gallery!

  
- The __Cheatsheet__  has some of my favorite links to help with app design.  

---
---



Theme Explorer App demo: See a sample Dash app updated as you choose from:
 - 22 [Bootstrap Bootswatch themes](https://www.bootstrapcdn.com/bootswatch/)
 - 11 [Plotly Graph Templates](https://plotly.com/python/templates/)
 - 18 [Plotly Graph Discrete Color Sequences](https://plotly.com/python/builtin-colorscales/#discrete-color-sequences)
 - 94 [Plotly Graph Continuous Colorscales](https://plotly.com/python/builtin-colorscales/)
 - Any background color selected from a colorpicker



![Peek 2021-03-17 06-57](https://user-images.githubusercontent.com/72614349/111480344-228e7800-86ef-11eb-9ac9-32740c1fab1e.gif)

-----------


### These two images are the same app!  Only 1 line of code is changed to update the design.

|Light Theme app     | Dark Theme app |
| ----------- | ----------- |
| ![theme_explorer_light](https://user-images.githubusercontent.com/72614349/109723319-28bb1b00-7b6b-11eb-8942-20a109b3ed1e.png#thumbnail) | ![theme_explorer_dark](https://user-images.githubusercontent.com/72614349/109723317-28228480-7b6b-11eb-8a50-0ac06ec2bca1.png#thumbnail) |
| __Bootstrap Theme:__ MINTY | DARKLY
| __Graph Template:__ simple_white | plotly_dark|
| __Graph Color Sequences:__ Pastel | Dark24|
| __Graph Continuous Colorscales:__ darkmint | ice|
| __App Background Color:__ #F3F6F3 | ""|

------


This is still a work in progress and I'm planning to add a lot more content.  I would love to hear comments 
and suggestions for improvements.  If you have any design tips you would like to see here, please let me know.


If you have an app that you would like to add to the gallery, please open an [issue](https://github.com/AnnMarieW/HelloDash/issues) and include the following information:

1) An image of your app
2) A short title to appear on the card in the gallery
3) A link to the Github/GitLab ect for your code
4) An extended description of your app.  This will be displayed in a dcc.Markdown component, so feel free to include any
compatible Markdown formatting and links etc.
   

Special thanks to @tcbegley and @adamschroeder for their helpful input on this project.


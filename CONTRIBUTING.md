
# HelloDash Contributor Guide

## Getting Started

Comments, suggestion, constructive criticism, contributions and pull requests are
gladly accepted.  And positive remarks will be received with great glee and gratitude. :-)
Please open an issue here.

For now, this section is documentation for my future self, when I need to come back here
to maintain this project.

### App Structure
The app is structured as a multi-page app as shown in the [docs](https://dash.plotly.com/urls)

- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py

After cloning or forking this repo, run index.py

The apps directory contains seperate apps for each page.  There is also a text.py file where I keep
all the longer narratives and text code block examples.  These are imported into the appropriate
modules as needed.  This keeps the app pages shorter, easier to read and maintain.

The gallery directory contains the code for the stand-alone apps that are shown in the gallery. 
Note that the app to create the gallery is in the apps directory. 

### Images
The images for this app are not included in the file structure.  All the images are located in
Issue #1 in the HelloDash GitHub repo (If you can't find it, look for closed issues).  This is
done to keep the file size smaller so I don't run out of space on my free PythonAnywhere hosting
site.  Also, it seems to  load the images faster from the link than when the are in the
assets directory.  

To add images to the app, copy and paste or upload an image. Or edit an image that's currently
there.  Copy the address.  It can be included like this:

    dcc.Markdown(" [title](link)]

To control the size of the image add a hashtag ie link#thumbnail  at the end of the link, 
Then adjust the size in the .css file in the assets folder:

    img[src*="#thumbnail"] {
       width:100px;
       height:100px;
    }

Or add them in a card using:

```python
        dbc.CardImg(
                src=image,  #link
                top=True,
                style={"height": "auto", "width": "100%"},  # This makes the scale right when resized
                className="p-2",
            ),

```

### Code blocks

It would be great if I could just use dcc.Markdown( ``` my code block ``)  However, this
looks terrible in dark themed apps, especially if it's integrated on the page. (It's not too bad in a modal)
Here are a couple work-arounds I use:


- To show a compete app, it can be read from a file like the following.  It will format it as 
a string with the ``` code ``` so it can be displayed in Markdown.  I use this for the "Source Code" button
  on the main page.  When it's a modal, it doesn't look too bad even in a dark app.
```python
        # set relative path
        PATH = pathlib.Path(__file__).parent
        GALLERY_PATH = PATH.joinpath("../gallery").resolve()
        
        # be sure to include a blank line and docstring at start of source file so it formats correctly
        with open(GALLERY_PATH.joinpath("theme_explorer_app.py")) as f:
            code = f.read()
```
        code = f"```{code}```"

- For smaller code blocks that are in the text.py file, they are formated as follows.  Because of the
transparent background they look better in dark apps, but they don't have syntax hilighting. 

    ```   
    codebox = {
        "backgroundColor": "transparent",
        "borderStyle": "groove",
        "borderRadius": 15,
        "maxWidth": 900,
        "marginTop": 0,
        "marginBottom": 20,
    }
    html.Div(html.Pre(html.Code(" enter code here" )), style=codebox)  
  ```
   
- The app for the theme switcher is called theme_explorer.py.  The theme_explorer_app.py in the gallery
directory is a stand-alone version of the Sample Dash app you see in the theme_explorer.
- To add apps to the app gallery see app_gallery.py  There are more instructions in the docstring.
- To add cheatsheet cards see cheatsheet.py.  Any card that looks like the cheatsheet cards are created
here and imported where needed.


    




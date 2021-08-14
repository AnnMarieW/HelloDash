
# HelloDash Contributor Guide



Comments, suggestion, constructive criticism, contributions and pull requests are
gladly accepted.  Please open an issue here.

Caution - this page is mostly notes for my future self  -- for when I need to come back here
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
Issue #1 in the HelloDash GitHub repo (If you can't find it, check closed issues).  This is
done to keep the file size smaller so I don't run out of space on my free PythonAnywhere hosting
site.  Also, it seems to  load the images faster from the link than when they are in the
assets directory.  

To add images to the app, copy and paste or upload an image. Or edit an image that's currently
there.  Copy the address.  It can be included like this:

    dcc.Markdown("[title](link)"]

To control the size of the image add a hashtag ie link#thumbnail  at the end of the link, 
Then adjust the size in the .css file in the assets folder:

    img[src*="#thumbnail"] {
       width:100px;
       height:100px;
    }

The images in the app gallery use a card like this:

```python
        dbc.CardImg(
                src=image,  #link
                top=True,
                style={"height": "auto", "width": "100%"},  # This makes the scale right when resized
                className="p-2",
            ),

```

### Code blocks

This app uses several methods to display code.

#### Div with a copy to clipboard icon
See the `get_copy_code_div()` function in util.py. `dcc.Clipboard` was new in Dash 1.21.0
Will start updating all the code blocks to use this.  

#### Button with external link
The app gallery uses a button with a link to the github repo:
```python
        dbc.Button(
            "Source Code",
            color="secondary",            
            target="_blank",
            href=source_code,  # github link
            size="sm",
            outline=True,
        ),
```

#### Button with a modal
See helper functions in dcc_components.py.  Code can be displayed in dcc.Markdown("""\```code```""") or as described below 
which is better for dark themes.


        
#### Format code to display with dark themes
For smaller code blocks that are displayed in-line, it needs to have a transparent background so it looks OK with 
dark themed apps.  This is a work-around, but it doesn't have syntax highlighting:

This goes in `mycss.css` file in \assets
```css
.codebox  {
    background-color: transparent;
    border-style: double;
    border-radius: 15px;
    max-width: 900px;
    margin-top: 10px;
    margin-bottom:20px;
    padding:20px;
}
```

to use:
``` 
html.Div(html.Pre(html.Code(" enter code here" )), className="codebox")  
```
  

#### Get app code from gallery directory
To show a compete app from the gallery without an external link  - like in a modal using dcc.Markdown(code),
it can be read from a file like this:

```python
        # set relative path
        PATH = pathlib.Path(__file__).parent
        GALLERY_PATH = PATH.joinpath("../gallery").resolve()
        
        # be sure to include a blank line and docstring at start of source file so it formats correctly
        with open(GALLERY_PATH.joinpath("theme_explorer_app.py")) as f:
            code = f.read()
        code = f"```{code}```"
```

#### Get code from the text.py file
Most of the smaller code blocks are in this file

   
- The app for the theme switcher is called theme_explorer.py.  The theme_explorer_app.py in the gallery
directory is a stand-alone version of the Sample Dash app you see in the theme_explorer.
- To add apps to the app gallery see app_gallery.py  There are more instructions in the docstring.
- To add cheatsheet cards see cheatsheet.py.  Any card that looks like the cheatsheet cards are created
here and imported where needed.

(more details to follow)


    




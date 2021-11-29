
# HelloDash Contributor Guide


Comments, suggestion, constructive criticism, contributions and pull requests are
gladly accepted.  Please open an issue here.

Caution - this page is mostly notes for my future self  -- for when I need to come back here
to maintain this project.

### App Structure
The app is structured as a multi-page app as shown in the [docs](https://dash.plotly.com/urls)

- index.py
- apps  
   |-- __init__.py  
   |-- app1.py  
   |-- app2.py  

After cloning or forking this repo, run app.py

The apps directory contains separate apps for each page. 

The gallery directory contains the code for the stand-alone apps that are shown in the gallery or used in demos. 
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

#### Card with a copy to clipboard icon
See the `make_code_card()` function in util.py. `dcc.Clipboard` was new in Dash 1.21.0
See the `get_code_file()` function in util.py for reading code files from the gallery folder

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


        
#### Format code to display with dark themes
Use the className="dbc" which include the Github dimmed theme for code blocks.
More info on different themes for code highlighting:  https://community.plotly.com/t/how-to-change-the-theme-of-code-highlights-in-dcc-markdown/58004

  

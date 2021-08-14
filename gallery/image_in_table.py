"""
How to add images to a table
"""
import dash
import dash_html_components as html
import dash_table
import pandas as pd
from collections import OrderedDict

app = dash.Dash(__name__)

seattle = "![Seattle](https://upload.wikimedia.org/wikipedia/commons/8/80/SeattleQueenAnne2021-2.png#thumbnail)"
montreal = "![Montreal](https://upload.wikimedia.org/wikipedia/commons/d/d0/Montreal_August_2017_05.jpg#thumbnail)"
nyc = "![New York City](https://upload.wikimedia.org/wikipedia/commons/f/f7/Lower_Manhattan_skyline_-_June_2017.jpg#thumbnail)"

df = pd.DataFrame(
    OrderedDict(
        [
            ("temperature", [13, 43, 50]),
            ("city", ["NYC", "Montreal", "Seattle"]),
            ("image", [nyc, montreal, seattle]),
        ]
    )
)

app.layout = html.Div(
    [
        dash_table.DataTable(
            id="table-dropdown",
            data=df.to_dict("records"),
            columns=[
                {"id": "image", "name": "image", "presentation": "markdown"},
                {"id": "city", "name": "city"},
                {"id": "temperature", "name": "temperature"},
            ],
            style_cell_conditional=[{"if": {"column_id": "image"}, "width": "200px"},],
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

"""
Add to the css file in the assets folder:

img[src*="#thumbnail"] {
   width:200px;
   height:100px;
}
"""

"""
------------
More tips:
------------


If the image is in the assets directory, use this: dcc.Markdown('![]({})'.format(app.get_asset_url('my_image.svg#thumbnail')))

To embed the image with other text, it needs to be a single string:

dcc.Markdown("My intro text" + '![]({})'.format(app.get_asset_url('my_image.svg#thumbnail')) + "My other text")

"""

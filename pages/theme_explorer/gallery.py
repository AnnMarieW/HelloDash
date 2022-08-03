import dash
from pages.theme_explorer import dbc_gallery_layout

dash.register_page(__name__, layout=dbc_gallery_layout.layout, name="dbc Gallery")

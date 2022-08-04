import dash
from pages.theme_explorer import gallery_layout
from lib.utils import app_description

dash.register_page(
    __name__,
    layout=gallery_layout.layout,
    name="dbc Gallery",
    title="Theme Explorer dbc Gallery",
    description=app_description,
)

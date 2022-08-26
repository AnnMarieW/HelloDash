import dash
from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
from dash_before_after import BeforeAfter



deep_field = "https://user-images.githubusercontent.com/72614349/179115661-f8de6e4c-0dca-4628-ab67-3d525f5ac049.jpg"
stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115662-32d348da-fa8b-481d-b4fc-9f7414f49de0.jpg"
webb_stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115663-71578706-1ab5-45a5-b809-812c7c3028a7.jpg"
carina = "https://user-images.githubusercontent.com/72614349/179115665-9800b45c-e1dc-4aa7-8b34-885d48c61221.png"
southern_nebula = "https://user-images.githubusercontent.com/72614349/179115666-fdd204fc-e33d-4524-9ba5-a2611740f8a7.jpg"
webb_deep_field = "https://user-images.githubusercontent.com/72614349/179115668-2630e3e4-3a9f-4c88-9494-3412e606450a.jpg"
webb_southern_nebula = "https://user-images.githubusercontent.com/72614349/179115670-ef5bc561-d957-4e88-82dc-53ca53541b04.jpg"
webb_carina = "https://user-images.githubusercontent.com/72614349/179115673-15eaccb9-d17d-4667-84fb-e0a46fd444e8.jpg"
webb_cartwheel = "https://user-images.githubusercontent.com/72614349/184414634-fbd08745-94b9-4de6-8bce-c3607d9fd8db.png"
cartwheel = "https://user-images.githubusercontent.com/72614349/184414677-69e09ba2-9852-4dc7-9d3f-9024518dcd3c.png"


descr = "James Webb Space Telescope First Images. Compare before and after images of Hubble vs Webb.  Make an app like this with ~40 lines of Python using Plotly Dash."

dash.register_page(
    __name__,
    name="Galaxy Cluster SMACS 0723",
    title="James Webb Space Telescope First Images",
    description=descr,
    image="deep_field_meta.gif",
    path="/james-webb-telescope",
    redirect_from=['/jwt', '/cartwheel','/webb-carina', '/webb-southern-ring', '/webb-stephans-quintet' ]
)


header = html.Div(
    [
        html.H2("James Webb Space Telescope", className="display-3"),
        html.Div("First Images.  Compare before and after images of Hubble vs Webb.", className="mb-1"),
        dbc.Button(
            [html.I(className="bi bi-book me-2"), "webbtelescope.org"],
            color="light",
            className="text-white-50",
            href="https://webbtelescope.org/news/first-images/gallery",
        ),
        dbc.Button(
            [html.I(className="bi bi-github me-2"), "source code"],
            color="light",
            className="ms-2 text-white-50",
            href="https://github.com/AnnMarieW/webb-compare",
            title="Make an app like this with ~40 lines of Python using Plotly Dash",
        ),
    ],
)


def make_before_after(before, after):
    return html.Div(
        [
            html.Div(
                [html.Div("Hubble"), html.Div("Webb")],
                className="d-flex justify-content-between",
                style={"width": "auto"},
                id="label_div",
            ),
            BeforeAfter(before=before, after=after, id="before_after"),
        ],
        style={"marginTop": 50},
    )



tabs = dbc.Tabs(
    [
        dbc.Tab(make_before_after(webb_deep_field,deep_field), label="Galaxy Cluster SMACS 0723"),
        dbc.Tab(make_before_after(webb_cartwheel, cartwheel), label="Cartwheel Gallery"),
        dbc.Tab(make_before_after(webb_stephans_quintet, stephans_quintet), label="Stephans Quintet"),
        dbc.Tab(make_before_after(webb_carina, carina), label="Carina Nebula"),
        dbc.Tab(make_before_after(webb_southern_nebula, southern_nebula), label="Southern Ring Nebula"),
    ],
    className="mt-4",
)

layout = dbc.Container([header, tabs], style={"maxWidth": 1000})


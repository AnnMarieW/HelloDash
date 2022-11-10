from dash import dcc, html
import dash_bootstrap_components as dbc

icon_left = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
icon_up = html.I(className="fa-solid fa-hand-point-up fs-5 me-2")

# footer book ad
book_img = "https://user-images.githubusercontent.com/72614349/185497519-733bdfc3-5731-4419-9a68-44c1cad04a78.png"
nostarch = "https://nostarch.com/book-dash"
github = "fa-brands fa-github"
youtube = "fa-brands fa-youtube"
info = "fa-solid fa-circle-info"
cart = "fa-solid fa-cart-shopping"
plotly = "https://plotly.com/python/"
dash_url = "https://dash.plotly.com/"
forum = "https://community.plotly.com/"
plotly_logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"
book_github = "https://github.com/DashBookProject/Plotly-Dash"
amw = "https://github.com/AnnMarieW"
adam = "https://www.youtube.com/c/CharmingData/featured"
chris = "https://finxter.com/"
dbt_github = "https://github.com/AnnMarieW/dash-bootstrap-templates"
# end footer book ad



def change_theme_alert(text=None, auto_dismiss=True):
    if text is None:
        text = "Use the Change Theme button to see examples with all 26 themes."
    text = html.Span([icon_left, text])

    if auto_dismiss:
        return dbc.Alert(
            text, is_open=True, duration=4000, style={"maxWidth": 300}, className="py-2"
        )

    return dbc.Alert(
        text, is_open=True, dismissable=True, style={"maxWidth": 300}, className="py-2"
    )

bootstrap_utils_alert = dbc.Alert(
        html.Span([icon_up, "Use the Bootstrap Cheatsheet button to open a cheatsheet in a new window"]),
        is_open=True, dismissable=True, style={"maxWidth": 300}, className="py-2", color="primary"
    )





def make_link(text, icon, link):
    return html.Span(html.A([html.I(className=icon + " ps-1 pe-2"), text], href=link))


button = dbc.Button(
    [html.I(className=cart + " pe-2"),"Order"], color="primary", href=nostarch, size="sm", className="mt-2 ms-1"
)

cover_img = html.A(
    dbc.CardImg(
        src=book_img,
        className="img-fluid rounded-start",
    ),
    href=nostarch,

)

text = dcc.Markdown(
    "From basic components to advanced layouts, learn how to display data in effective, usable, and elegant ways.",
    className="ps-2",
)


authors = html.P(
    [
        "By ",
        make_link("Adam Schroeder ", youtube, adam),
        make_link("Christian Mayer", info, chris),
        make_link("Ann Marie Ward", github, amw),
    ],
    className="card-text p-2",
)


about_me1 = f"""
__This site is maintained by Ann Marie Ward,__  
co-author of ["The Book of Dash"]({nostarch})
"""
about_me1 = dcc.Markdown(about_me1,
    className="mt-5 text-center small",
    style={"maxWidth": "32rem"},
)

about_me2 = html.Div(
    [
        html.Div(["Questions?  Ask on the", make_link("Dash Community Forum", "", forum)]),
        html.Div(["Was this site helpful? Please star", make_link("dash-bootstrap-templates", github, dbt_github)]),
    ],
    className="text-center small"
)

about_me = html.Div([about_me1, about_me2])


book_card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(cover_img, width=3, className="p-1"),
                dbc.Col(
                    [text, button],
                    width=9,
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
        dbc.Row(dbc.Col(authors)),
    ],
    className="mt-4 mb-5 small shadow p-2",
    style={"maxWidth": "32rem"},
)

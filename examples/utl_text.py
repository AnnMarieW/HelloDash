from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

title = dcc.Markdown(
    """
### Text Styles
------------
"""
)


text_wrap = dbc.Card(
    [
        dbc.CardHeader("text-wrap, text-nowrap, text-break"),
        html.Div(
            [
                html.P(
                    dbc.Badge(
                        "text-wrap will wrap text onto the next line",
                        className="text-wrap",
                        style={"width": 100},
                    )
                ),
                html.P(
                    dbc.Badge(
                        "text-nowrap won't wrap text",
                        className="text-nowrap",
                        style={"width": 100},
                    )
                ),
                html.P(
                    className="text-break",
                    children="utilitysothisverylongtextstringwithoutspacesordasheswillbreaktostayinsidethecontainerthisisaverylongtextstringwithoutspacesthatwillbreaktostayinsidethecontainer",
                ),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)

text_option = dbc.Card(
    [
        dbc.CardHeader("text-lowercase, text-uppercase, text-capitalize"),
        html.Div(
            [
                html.P("Lowercased text", className="text-lowercase"),
                html.P("Uppercased text", className="text-uppercase"),
                html.P("Capitalized text", className="text-capitalize"),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)

fs_size = dbc.Card(
    [
        dbc.CardHeader("fs-* Font Size"),
        html.Div(
            [
                html.P("fs-1", className="fs-1 text"),
                html.P("fs-2", className="fs-2 text"),
                html.P("fs-3", className="fs-3 text"),
                html.P("fs-4", className="fs-4 text"),
                html.P("fs-5", className="fs-5 text"),
                html.P("fs-6", className="fs-6 text"),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)

fw_weight = dbc.Card(
    [
        dbc.CardHeader("fw-bold, fw-bolder, fw-light, fw-lighter"),
        html.Div(
            [
                html.P("Normal weight text"),
                html.P("Bold text", className="fw-bold"),
                html.P(
                    "Bolder weight text (relative to the parent element)",
                    className="fw-bolder",
                ),
                html.P("Light weight text", className="fw-light"),
                html.P(
                    "Lighter weight text (relative to the parent container)",
                    className="fw-lighter",
                ),
            ],
            className="p-4",
        ),
    ],
    className="border my-4",
)

fst_style = dbc.Card(
    [
        dbc.CardHeader("fst-italic fst-normal"),
        html.Div(
            [
                html.P("Italic text", className="fst-italic"),
                html.P("Text with normal font style", className="fst-normal"),
            ],
            className="p-4",
        ),
    ],
    className="border my-4",
)


lorem_text = "Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Donec sed odio dui. Cras mattis pannenkoek purus sit amet fermentum. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Cras mattis consectetur purus sit amet fermentum."
lh_style = dbc.Card(
    [
        dbc.CardHeader("Line Height lh-1, lh-sm, lh-base, lh-lg"),
        html.Div(
            [
                html.P(lorem_text, className="lh-1"),
                html.P(lorem_text, className="lh-sm"),
                html.P(lorem_text, className="lh-base"),
                html.P(lorem_text, className="lh-lg"),
            ],
            className="p-4",
        ),
    ],
    className="border my-4",
)

font_monospace = html.P(
    "font-monospace  This is in monospace", className="font-monospace"
)


text_decoration = dbc.Card(
    [
        dbc.CardHeader("Text Decoration"),
        html.Div(
            [
                html.P(
                    "This text has a line underneath it",
                    className="text-decoration-underline",
                ),
                html.P(
                    "This text has a line going through it",
                    className="text-decoration-line-through",
                ),
                html.A(
                    "This link has text decoration removed",
                    href="#",
                    className="text-decoration-none",
                ),
            ],
            className="p-4",
        ),
    ],
    className="my-4",
)


app.layout = html.Div(
    [
        title,
        text_wrap,
        text_option,
        fs_size,
        fw_weight,
        fst_style,
        lh_style,
        text_decoration,
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

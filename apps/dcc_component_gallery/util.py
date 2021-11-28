from dash import html

DCC_DOCS = "https://dash.plotly.com/dash-core-components/"


def dcc_make_subheading(label, link):

    return html.H3(
        html.Span(
            [
                label,
                html.A(
                    html.I(className="bi bi-book h5 ms-2"),
                    href=f"{DCC_DOCS}{link}",
                    target="_blank",
                ),
            ],
        ),
        className="mt-4",
    )


def datatable_make_subheading():

    return html.H3(
        html.Span(
            [
                "DataTable",
                html.A(
                    html.I(className="bi bi-book h5 ms-2"),
                    href="https://dash.plotly.com/datatable",
                    target="_blank",
                ),
            ],
        ),
        className="mt-4",
    )

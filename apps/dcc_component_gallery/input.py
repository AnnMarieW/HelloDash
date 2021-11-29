import dash_bootstrap_components as dbc
from dash import html, dcc

input = html.Div(
    [
        dcc.Input(
            placeholder="This is a dash dcc input...",
            type="text",
            value="",
            className="mt-4 mb-2",
        ),
        dcc.Input(
            placeholder='This is a dash dcc input with className="form-control" ...',
            type="text",
            value="",
            className="form-control",
        ),
        dbc.Input(
            placeholder="This is a dbc input...",
            type="text",
            value="",
            className="my-2",
        ),
    ]
)
textarea = html.Div(
    [
        dcc.Textarea(
            placeholder="Enter a value...",
            value="This is a TextArea component",
            style={"width": "100%"},
        )
    ]
)

options = [
    {"label": "New York City", "value": "NYC"},
    {"label": "Montréal", "value": "MTL"},
    {"label": "San Francisco", "value": "SF"},
]

checkboxes = html.Div([dcc.Checklist(options=options, value=["MTL", "SF"])])
checklist = dcc.Checklist(
    options=options, value=["MTL", "SF"], labelStyle={"display": "inline-block"}
)
radioitems = html.Div([dcc.RadioItems(options=options, value="MTL")])

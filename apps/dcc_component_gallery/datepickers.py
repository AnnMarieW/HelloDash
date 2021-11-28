import dash_bootstrap_components as dbc
from dash import html, dcc

from .util import dcc_make_subheading


from datetime import date

datepicker_single = html.Div(
    [dcc.DatePickerSingle(date=date(2021, 5, 10))], className="dbc"
)

datepicker_range = html.Div(
    [
        dcc.DatePickerRange(
            start_date=date(2021, 5, 3), end_date_placeholder_text="Select a date!"
        )
    ]
)


dcc_date_picker_single = html.Div(
    [
        dcc_make_subheading("dcc.DatePickerSingle", "datepickersingle"),
        dbc.Row(datepicker_single),
    ],
    className="my-4",
)

dcc_date_picker_range = html.Div(
    [
        dcc_make_subheading("dcc.DatePickerRange", "datepickerrange"),
        dbc.Row(datepicker_range),
    ],
    className="my-4",
)

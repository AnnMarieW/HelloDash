import dash_labs as dl
import dash  # Dash version==1.16.0 and Plotly version==4.10.0
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from pandas_datareader import wb

app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])
tpl = dl.templates.DbcSidebar(
    app, title="Comparison of World Bank Country Data", theme=dbc.themes.PULSE
)

indicators = {
    "IT.NET.USER.ZS": "Individuals using the Internet (% of population)",
    "SG.GEN.PARL.ZS": "Parliament seats % held by women",
    "EN.ATM.CO2E.KT": "CO2 emissions (kt)",
}

# get country name and ISO id for mapping on choropleth
countries = wb.get_countries()
countries["capitalCity"].replace({"": None}, inplace=True)
countries.dropna(subset=["capitalCity"], inplace=True)
countries = countries[["name", "iso3c"]]
countries = countries[countries["name"] != "Kosovo"]
countries = countries.rename(columns={"name": "country"})


def update_wb_data():
    # Retrieve specific world bank data from API
    df = wb.download(
        indicator=(list(indicators)), country=countries["iso3c"], start=2005, end=2016
    )
    df = df.reset_index()
    df.year = df.year.astype(int)

    # Add country ISO3 id to main df
    df = pd.merge(df, countries, on="country")
    df = df.rename(columns=indicators)
    return df


def make_figure(dff, indct_chosen):
    fig = px.choropleth(
        data_frame=dff,
        locations="iso3c",
        color=indct_chosen,
        scope="world",
        hover_data={"iso3c": False, "country": True},
        labels={
            indicators["SG.GEN.PARL.ZS"]: "% parliament women",
            indicators["IT.NET.USER.ZS"]: "pop % using internet",
        },
    )
    fig.update_layout(
        geo={"projection": {"type": "natural earth"}},
        margin=dict(l=50, r=50, t=50, b=50),
    )
    return dcc.Graph(figure=fig)


radio_indicators = dbc.RadioItems(
    options=[{"label": i, "value": i} for i in indicators.values()],
    value=list(indicators.values())[0],
    className="mb-4",
)

years_slider = dcc.RangeSlider(
    min=2005,
    max=2016,
    value=[2005, 2006],
    marks={
        2005: "2005",
        2006: "'06",
        2007: "'07",
        2008: "'08",
        2009: "'09",
        2010: "'10",
        2011: "'11",
        2012: "'12",
        2013: "'13",
        2014: "'14",
        2015: "'15",
        2016: "2016",
    },
)
submit_button = dbc.Button(children="Submit", color="primary", className="mt-4")
storage = dcc.Store(id="storage", storage_type="local", data={})
interval = dcc.Interval(id="timer", interval=1000 * 60, n_intervals=0)


@app.callback(Output("storage", "data"), Input("timer", "n_intervals"))
def store_data(n_time):
    dataframe = update_wb_data()
    return dataframe.to_dict("records")


@app.callback(
    args=dict(
        stored_dataframe=Input("storage", "data"),
        indct_chosen=dl.State(radio_indicators, label="Select Indicators"),
        years_chosen=dl.State(years_slider, label="Select Years"),
        n_clicks=dl.Input(submit_button, "n_clicks", label=""),
    ),
    template=tpl,
)
def update_graph(n_clicks, stored_dataframe, years_chosen, indct_chosen):
    dff = pd.DataFrame.from_records(stored_dataframe)
    if years_chosen[0] != years_chosen[1]:
        dff = dff[dff.year.between(years_chosen[0], years_chosen[1])]
        dff = dff.groupby(["iso3c", "country"])[indct_chosen].mean()
        dff = dff.reset_index()
        return make_figure(dff, indct_chosen)

    if years_chosen[0] == years_chosen[1]:
        dff = dff[dff["year"].isin(years_chosen)]
        return make_figure(dff, indct_chosen)


app.layout = dbc.Container(
    [dbc.Row(dbc.Col(tpl.children)), html.Div([interval, storage])], fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=True)


"""
=============================================================================
Original - (refactored) Dash 1 app
"""
#
# import dash  # Dash version==1.16.0 and Plotly version==4.10.0
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
# import plotly.express as px
# import dash_bootstrap_components as dbc
# import pandas as pd
# from pandas_datareader import wb
#
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# indicators = {
#     "IT.NET.USER.ZS": "Individuals using the Internet (% of population)",
#     "SG.GEN.PARL.ZS": "Parliament seats % held by women",
#     "EN.ATM.CO2E.KT": "CO2 emissions (kt)",
# }
#
# # get country name and ISO id for mapping on choropleth
# countries = wb.get_countries()
# countries["capitalCity"].replace({"": None}, inplace=True)
# countries.dropna(subset=["capitalCity"], inplace=True)
# countries = countries[["name", "iso3c"]]
# countries = countries[countries["name"] != "Kosovo"]
# countries = countries.rename(columns={"name": "country"})
#
#
# def update_wb_data():
#     # Retrieve specific world bank data from API
#     df = wb.download(
#         indicator=(list(indicators)), country=countries["iso3c"], start=2005, end=2016
#     )
#     df = df.reset_index()
#     df.year = df.year.astype(int)
#
#     # Add country ISO3 id to main df
#     df = pd.merge(df, countries, on="country")
#     df = df.rename(columns=indicators)
#     return df
#
#
# def make_figure(dff, indct_chosen):
#     fig = px.choropleth(
#         data_frame=dff,
#         locations="iso3c",
#         color=indct_chosen,
#         scope="world",
#         hover_data={"iso3c": False, "country": True},
#         labels={
#             indicators["SG.GEN.PARL.ZS"]: "% parliament women",
#             indicators["IT.NET.USER.ZS"]: "pop % using internet",
#         },
#     )
#     fig.update_layout(
#         geo={"projection": {"type": "natural earth"}},
#         margin=dict(l=50, r=50, t=50, b=50),
#     )
#     return fig
#
#
# radio_indicators = dbc.RadioItems(
#     id="radio-indicator",
#     options=[{"label": i, "value": i} for i in indicators.values()],
#     value=list(indicators.values())[0],
#     className="mb-4",
# )
#
# years_slider = dcc.RangeSlider(
#     id="years-range",
#     min=2005,
#     max=2016,
#     value=[2005, 2006],
#     marks={
#         2005: "2005",
#         2006: "'06",
#         2007: "'07",
#         2008: "'08",
#         2009: "'09",
#         2010: "'10",
#         2011: "'11",
#         2012: "'12",
#         2013: "'13",
#         2014: "'14",
#         2015: "'15",
#         2016: "2016",
#     },
# )
# submit_button = dbc.Button(
#     children="Submit", id="my-button", color="primary", className="mt-4"
# )
# storage = dcc.Store(id="storage", storage_type="local", data={})
# interval = dcc.Interval(id="timer", interval=100000 * 60, n_intervals=0)
#
#
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             dbc.Col(
#                 [
#                     html.H1(
#                         "Comparison of World Bank Country Data",
#                         style={"textAlign": "center"},
#                     ),
#                     dcc.Graph(id="my-choropleth", figure={}),
#                 ],
#                 width=12,
#             )
#         ),
#         dbc.Row(
#             dbc.Col(
#                 [
#                     dbc.Label(
#                         "Select Data Set:",
#                         className="font-weight-bold",
#                         style={"textDecoration": "underline", "fontSize": 20},
#                     ),
#                     radio_indicators,
#                 ],
#                 width=4,
#             )
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     [
#                         dbc.Label(
#                             "Select Years:",
#                             className="font-weight-bold",
#                             style={"textDecoration": "underline", "fontSize": 20},
#                         ),
#                         years_slider,
#                         submit_button,
#                     ],
#                     width=6,
#                 ),
#             ]
#         ),
#         storage,
#         interval,
#     ]
# )
#
#
# @app.callback(Output("storage", "data"), Input("timer", "n_intervals"))
# def store_data(n_time):
#     dataframe = update_wb_data()
#     return dataframe.to_dict("records")
#
#
# @app.callback(
#     Output("my-choropleth", "figure"),
#     Input("my-button", "n_clicks"),
#     Input("storage", "data"),
#     State("years-range", "value"),
#     State("radio-indicator", "value"),
# )
# def update_graph(n_clicks, stored_dataframe, years_chosen, indct_chosen):
#     dff = pd.DataFrame.from_records(stored_dataframe)
#     if years_chosen[0] != years_chosen[1]:
#         dff = dff[dff.year.between(years_chosen[0], years_chosen[1])]
#         dff = dff.groupby(["iso3c", "country"])[indct_chosen].mean()
#         dff = dff.reset_index()
#         return make_figure(dff, indct_chosen)
#
#     if years_chosen[0] == years_chosen[1]:
#         dff = dff[dff["year"].isin(years_chosen)]
#         return make_figure(dff, indct_chosen)
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)

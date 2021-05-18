import pandas as pd
import plotly.express as px

import dash_labs as dl
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Preparing your data  *******************************************

df = pd.read_csv(
    "https://raw.githubusercontent.com/DashBookProject/Dash-Plotly/master/Chapter-4/tweets.csv"
)
df["name"] = pd.Series(df["name"]).str.lower()
df["date_time"] = pd.to_datetime(df["date_time"])
df = (
    df.groupby([df["date_time"].dt.date, "name"])[
        ["number_of_likes", "number_of_shares"]
    ]
    .mean()
    .astype(int)
)
df = df.reset_index()

# Define app and template **************************************

app = dash.Dash(__name__, plugins=[dl.plugins.FlexibleCallbacks()])

tpl = dl.templates.dbc.DbcSidebar(
    app,
    title="Twitter Likes Analysis of Famous People",
    figure_template=True,
    theme=dbc.themes.SPACELAB,
)

#
# tpl = dl.templates.dbc.DbcRow(
#     app,
#     title="Twitter Likes Analysis of Famous People",
#     figure_template=True,
#     theme=dbc.themes.SUPERHERO,
# )

#
# tpl = dl.templates.dbc.DbcCard(
#     app,
#     title="Twitter Likes Analysis of Famous People",
#     figure_template=True,
#     theme=dbc.themes.BOOTSTRAP,
# )
#
#
# tpl = dl.templates.HtmlCard(
#     app, title="Twitter Likes Analysis of Famous People",
# )


# Define components ********************************************

dropdown = dcc.Dropdown(
    multi=True,
    options=[{"label": x, "value": x} for x in sorted(df["name"].unique())],
    value=["taylorswift13", "cristiano", "jtimberlake"],
)

twitter_link = html.A(
    children="Click here to Visit Twitter",
    href="https://twitter.com/explore",
    target="_blank",
)


def make_graph(df_filtered):
    fig = px.line(
        data_frame=df_filtered,
        x="date_time",
        y="number_of_likes",
        color="name",
        log_y=True,
        labels={"number_of_likes": "Likes", "date_time": "Date", "name": "Celebrity",},
    )
    return dcc.Graph(figure=fig)


# Callbacks ***************************************************************


@app.callback(dl.Input(dropdown), template=tpl)
def update_graph(chosen_value):
    if len(chosen_value) == 0:
        raise dash.exceptions.PreventUpdate
    else:
        df_filtered = df[df["name"].isin(chosen_value)]
        return make_graph((df_filtered))


# Layout ******************************************************************

tpl.add_component(twitter_link, role="output", after=0)
app.layout = tpl.children

if __name__ == "__main__":
    app.run_server(debug=True)


"""
=============================================================================
Original - (refactored) Dash 1 app
"""
#
# import pandas as pd
# import plotly.express as px
#
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
#
# # Preparing your data for usage *******************************************
#
# df = pd.read_csv(
#     "https://raw.githubusercontent.com/DashBookProject/Dash-Plotly/master/Chapter-4/tweets.csv"
# )
# df["name"] = pd.Series(df["name"]).str.lower()
# df["date_time"] = pd.to_datetime(df["date_time"])
# df = (
#     df.groupby([df["date_time"].dt.date, "name"])[
#         ["number_of_likes", "number_of_shares"]
#     ]
#     .mean()
#     .astype(int)
# )
# df = df.reset_index()
#
#
# #  Define components  *******************************************************
#
# dropdown = dcc.Dropdown(
#     id="my-dropdown",
#     multi=True,
#     options=[{"label": x, "value": x} for x in sorted(df["name"].unique())],
#     value=["taylorswift13", "cristiano", "jtimberlake"],
# )
#
# twitter_link = html.A(
#     id="my-link",
#     children="Click here to Visit Twitter",
#     href="https://twitter.com/explore",
#     target="_blank",
# )
#
#
# def make_graph(df_filtered):
#     fig = px.line(
#         data_frame=df_filtered,
#         x="date_time",
#         y="number_of_likes",
#         color="name",
#         log_y=True,
#         labels={"number_of_likes": "Likes", "date_time": "Date", "name": "Celebrity",},
#     )
#     return fig
#
#
# # App Layout **************************************************************
#
# stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
# app = dash.Dash(__name__, external_stylesheets=stylesheets)
#
# app.layout = html.Div(
#     [
#         html.Div(
#             html.H1(
#                 "Twitter Likes Analysis of Famous People", style={"textAlign": "center"}
#             ),
#             className="row",
#         ),
#         html.Div(dcc.Graph(id="line-chart", figure={}), className="row"),
#         html.Div(
#             [
#                 html.Div(dropdown, className="three columns",),
#                 html.Div(twitter_link, className="two columns",),
#             ],
#             className="row",
#         ),
#     ]
# )
#
#
# # Callbacks ***************************************************************
# @app.callback(
#     Output(component_id="line-chart", component_property="figure"),
#     [Input(component_id="my-dropdown", component_property="value")],
# )
# def update_graph(chosen_value):
#     print(f"Values chosen by user: {chosen_value}")
#
#     if len(chosen_value) == 0:
#         raise dash.exceptions.PreventUpdate
#     else:
#         df_filtered = df[df["name"].isin(chosen_value)]
#         return make_graph(df_filtered)
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)

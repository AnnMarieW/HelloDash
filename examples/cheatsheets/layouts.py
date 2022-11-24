side_by_side_html = """```python
sheet=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=sheet)

app.layout = html.Div([
   html.Div([
       html.Div([dcc.Dropdown()], className="three columns"),
       html.Div([dcc.Graph()], className="nine columns")
   ], className="row")
])
```"""

side_by_side_dbc = """```python
import dash_bootstrap_components as dbc
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
   dbc.Row([
       dbc.Col([dcc.Dropdown()], width=3),
       dbc.Col([dcc.Graph()], width=9)
   ])
])
```"""

side_by_side_dmc = """```python
import dash_mantine_components as dmc
app.layout = dmc.Container([
    dmc.Grid([
        dmc.Col(dcc.Dropdown(), span=3),
        dmc.Col(dcc.Graph(), span=8),
    ])
])
```"""

side_by_side = f"""


---
##### Dash Bootstrap

---
{side_by_side_dbc}

---
##### Dash Mantine

---
{side_by_side_dmc}

---
##### HTML and CSS

---
{side_by_side_html}

"""

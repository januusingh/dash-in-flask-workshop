import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd
import plotly.express as px

def init_dashboard(server):
    dash_app = dash.Dash(server=server, url_base_pathname="/dashapp/")

    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Money": [4, 1, 2, 2, 4, 5],
        })

    fig = px.bar(df, x="Fruit", y="Money", labels={"Fruit": "New Fruit Name"})

    dash_app.layout = html.Div(children=[html.H1(children="Hello Dash"),
                                        dcc.Graph(id="example-graph", figure=fig),])
    return dash_app.server

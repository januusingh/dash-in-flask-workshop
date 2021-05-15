import dash
import dash_html_components as html
import dash_core_components as dcc

import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Money": [4, 1, 2, 2, 4, 5],
    })
# Fruit  | Money
# Apples  | 4
# Oranges | 1
# Bananas | 2
# ..

df2 = pd.read_csv("../data/GME_5Y.csv")
# Date         | Close/End | ....
# "01/01/2021" | "$10.32"


# Date         | Close/End | ....
# "01/01/2021" | ["$", "10.32"]

# "$10.32".split("$") --> ["$", "10.32"]

# Date         | Close/End | ....
# "01/01/2021" | "10.32"
def get_value(row):
    return row[1]

df2["Date_dt"] = pd.to_datetime(df2["Date"], format="%m/%d/%Y")
df2["Close_num"] = pd.to_numeric(df2["Close/Last"].str.split("$").apply(get_value))
df2 = df2.sort_values("Date_dt")

fig = px.bar(df, x="Fruit", y="Money", labels={"Fruit": "New Fruit Name"})

fig2 = px.line(df2, x="Date_dt", y="Close_num",
                labels={"Date_dt": "Date", "Close_num": "Closing cost ($)"})

fig3 = px.line(df2, x="Date", y="Close_num")

# This is my app layout
app.layout = html.Div(children=[
        html.H1(children="Hello Dash"),
        html.Div(children=["Dash is cool!", html.H2(children="Another Dash is cool!")],),
        dcc.Graph(id="example-graph", figure=fig),
        dcc.Graph(id="gme-5year", figure=fig2),
        dcc.Graph(id="gme-5year-no_dt", figure=fig3)
    ])

if __name__ == "__main__":
    app.run_server(debug=True)

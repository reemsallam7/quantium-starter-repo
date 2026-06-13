import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "Arial", "padding": "20px"}, children=[

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={"textAlign": "center", "color": "#2c3e50"}
    ),

    html.H3(
        "Filter sales by region",
        style={"textAlign": "center", "color": "#7f8c8d"}
    ),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-graph")
])

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.capitalize()}",
        labels={"date": "Date", "sales": "Sales"}
    )

    fig.update_layout(
        title_x=0.5,
        plot_bgcolor="#f9f9f9"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
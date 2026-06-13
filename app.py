import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = Dash(__name__)

app.layout = html.Div(style={
    "fontFamily": "Arial",
    "backgroundColor": "#f4f6f9",
    "padding": "30px"
}, children=[

    html.Div(style={
        "backgroundColor": "white",
        "padding": "20px",
        "borderRadius": "12px",
        "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
        "marginBottom": "20px",
        "textAlign": "center"
    }, children=[
        html.H1("Soul Foods Sales Dashboard", style={"margin": "0"}),
    ]),

    html.Div(style={
        "backgroundColor": "white",
        "padding": "15px",
        "borderRadius": "12px",
        "marginBottom": "20px",
        "boxShadow": "0 4px 12px rgba(0,0,0,0.05)",
        "textAlign": "center"
    }, children=[

        html.H4("Select Region", style={"marginBottom": "10px"}),

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
            style={"fontSize": "16px"}
        )
    ]),

    html.Div(style={
        "backgroundColor": "white",
        "padding": "10px",
        "borderRadius": "12px",
        "boxShadow": "0 4px 12px rgba(0,0,0,0.05)"
    }, children=[
        dcc.Graph(id="sales-graph")
    ])
])


@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(region):

    if region == "all":
        dff = df
    else:
        dff = df[df["region"] == region]

    fig = px.line(
        dff,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        markers=True
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5,
        font=dict(size=14),
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
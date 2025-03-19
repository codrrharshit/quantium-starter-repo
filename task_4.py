from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv("processed.csv")
df = df.sort_values(by="date")  # Sort by date

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsel Sales DashBoard",
            style={"textAlign": "center", "color": "#ff4d4d", "fontSize": "32px", "marginBottom": "20px"}
        ),
        html.Label(
            "Select Region:",
            style={"fontSize": "18px", "fontWeight": "bold", "display": "block", "marginBottom": "10px"}
        ),
        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            style={
                "display": "flex",
                "gap": "15px",
                "marginBottom": "20px",
                "fontSize": "16px",
            },
        ),
        dcc.Graph(id="Sales-line-chart", style={"width": "100%", "height": "500px"}),
    ],
    style={
        "width": "70%",
        "margin": "auto",
        "padding": "20px",
        "backgroundColor": "#f9f9f9",
        "borderRadius": "10px",
        "boxShadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
    },
)


@callback(
    Output("Sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def Update_chart(selected_region):
    if selected_region == "all":
        df_selected = df
    else:
        df_selected = df[df["region"] == selected_region]

    fig = px.line(df_selected, x="date", y="sales", title=f'Sales Trend - {selected_region.capitalize()} Region')
    fig.update_layout(
        template="plotly_dark",
        title_x=0.5,
        xaxis_title="Date",
        yaxis_title="Sales",
        margin=dict(l=40, r=40, t=40, b=40),
        paper_bgcolor="#2c3e50",
        plot_bgcolor="#34495e",
        font=dict(color="white"),
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)

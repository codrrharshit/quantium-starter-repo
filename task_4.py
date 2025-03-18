from dash import Dash, html,dcc, Input,Output,callback
import plotly.express as px;
import pandas as pd ;


df= pd.read_csv("processed.csv")
#sort according to dates 
df = df.sort_values(by="date")


app = Dash(__name__, external_stylesheets=["style.css"])
app.layout=html.Div([
    html.H1("Pink Morsel Sales DashBoard",className="title"),
    html.Label("select Region :", className="label"),
    dcc.RadioItems(
         id='region-radio',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',
        className="radio-items"
    ),
    dcc.Graph(id="Sales-line-chart",className="chart")
],className="container")


@callback(
    Output("Sales-line-chart","figure"),
    Input("region-radio",'value')
)

def Update_chart(selected_region):
    if selected_region=="all":
        df_selected=df
    else :
        df_selected=df[df["region"]==selected_region]


    fig= px.line(df_selected,x="date",y="sales",title=f'Sales Trend - {selected_region.capitalize()} Region')
    fig.update_layout(
        template="plotly_dark", title_x=0.5,
        xaxis_title="Date", yaxis_title="Sales",
        margin=dict(l=40, r=40, t=40, b=40),
        paper_bgcolor="#2c3e50", plot_bgcolor="#34495e",
        font=dict(color="white")
    )
    return fig


if __name__=='__main__':
    app.run(debug=True)


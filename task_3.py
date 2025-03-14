import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html


# Load the CSV file
df = pd.read_csv("processed.csv")  # Replace with actual filename

# Convert 'date' column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Define the cutoff date for separation
cutoff_date = "2021-01-15"

# Separate data into "Before" and "After" based on the cutoff date
df_before = df[df["date"] < cutoff_date]
df_after = df[df["date"] >= cutoff_date]

df_before_monthly = df_before.groupby(df_before["date"].dt.to_period("M"))["sales"].sum().reset_index()
df_after_monthly = df_after.groupby(df_after["date"].dt.to_period("M"))["sales"].sum().reset_index()

# Convert period to timestamp for proper plotting
df_before_monthly["date"] = df_before_monthly["date"].dt.to_timestamp()
df_after_monthly["date"] = df_after_monthly["date"].dt.to_timestamp()

# Add period column
df_before_monthly["period"] = "Before Price Change"
df_after_monthly["period"] = "After Price Change"

# Combine the two dataframes
df_combined = pd.concat([df_before_monthly, df_after_monthly])

fig = px.bar(df_combined, x="date", y="sales", color="period",
             title="Sales Before & After Price Change",
             labels={"sales": "Total Sales", "date": "Date"},
             barmode="group",
             color_discrete_map={"Before Price Change": "blue", "After Price Change": "orange"})

# Add a vertical reference line for the price change date
fig.add_vline(x=cutoff_date, line_width=2, line_dash="dash", line_color="black")




app = dash.Dash(__name__)

# Define Layout
app.layout = html.Div([
    html.H1("Sales Data Visualizer"),
    dcc.Graph(figure=fig)  # Display the chart
])

# Run Server
if __name__ == "__main__":
    app.run_server(debug=True)

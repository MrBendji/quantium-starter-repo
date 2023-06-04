from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

filtered_data = pd.read_csv('./merged_data.csv')

# Create the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(
    children=[
        html.H1('Sales Visualization'),
        dcc.Graph(
            id='sales-chart',
            figure=px.line(filtered_data, x='Date', y='Sales', title='Sales Data')
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

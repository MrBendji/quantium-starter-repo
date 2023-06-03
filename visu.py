from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

filtered_data = pd.read_csv('merged_data.csv')

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('Sales Visualization'),
        dcc.Graph(
            id='sales-chart',
            figure=px.line(filtered_data, x='Date', y='Sales', title='Sales Data')
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)



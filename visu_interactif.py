from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash

data = pd.read_csv('./merged_data.csv')

# Create the Dash app
app = Dash(__name__)

# Define the app layout with CSS styling
app.layout = html.Div(
    style={'backgroundColor': '#f2f2f2', 'padding': '20px'},
    children=[
        html.H1(
            children='Sales Visualization',
            style={'textAlign': 'center', 'color': '#333333', 'fontFamily': 'Arial', 'marginBottom': '30px'}
        ),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '10px'}
        ),
        dcc.Graph(id='sales-chart')
    ]
)

# Define the callback function to update the chart based on the selected region
@app.callback(
    dash.dependencies.Output('sales-chart', 'figure'),
    [dash.dependencies.Input('region-filter', 'value')]
)
def update_chart(region):
    if region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['Region'] == region]

    fig = px.line(filtered_data, x='Date', y='Sales', title='Sales Data by Region')
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(family='Arial', size=12, color='#333333'),
        xaxis=dict(title='Date'),
        yaxis=dict(title='Sales')
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


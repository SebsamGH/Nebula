import dash 
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Student Progress Dashboard'),
    html.Div([
        html.H2('Academic Performance'),
        # Placeholder for academic performance section
    ]),
    html.Div([
        html.H2('Weekly Attendance'),
        # Placeholder for weekly attendance section
        
    ])
    
])

html.Div([
    html.H2('Academic Performance'),
    dcc.Graph(id='grade-graph')
])

html.Div([
    html.H2('Weekly Attendance'),
    # Placeholder for weekly attendance visualization
])

import plotly.graph_objs as go

sample_data = [
    ('2024-01-01', 85),
    ('2024-02-01', 78),
    ('2024-03-01', 92),
    # Add more data points as needed
]

@app.callback(
    dash.dependencies.Output('grade-graph', 'figure'),
    []
)
def update_grade_graph():
    trace = go.Scatter(
        x=[data[0] for data in sample_data],
        y=[data[1] for data in sample_data],
        mode='lines+markers',
        name='Grades'
    )

    layout = go.Layout(
        title='Grades Over Time',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Grade')
    )

    return {'data': [trace], 'layout': layout}




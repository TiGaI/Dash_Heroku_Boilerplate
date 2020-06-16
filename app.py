# Import required libraries
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/'
)
# Put your Dash code here
app.layout = html.Div(children=[
    dcc.Graph(id="example2"),
    dcc.Slider(id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    ),
    html.Div([html.Button('Button 1', id='btn-1'),
             html.Button('Button 2', id='btn-2'),
             html.Div(id='container', children=[])])
])

@app.callback(
    Output(component_id='example2', component_property='figure'),
    [Input(component_id='year-slider', component_property='value')]
)
def update_h1tag(input_value):
    filtered_df = df[df.year == input_value]

    scatterPlotly = go.Scatter(x=filtered_df['gdpPercap'], 
                y=df['lifeExp'],
                mode='markers')

    fig = go.Figure(data=scatterPlotly)

    fig.update_layout(title="ExampleScatterGraph",
                    xaxis=dict(title='GDP per cap'),
                    yaxis=dict(title='life exp')
                    )
    
    return fig


    # return {
    #     'data': [dict(
    #         x=filtered_df['gdpPercap'],
    #         y=filtered_df['lifeExp'],
    #         mode='markers',
    #         marker={
    #             'size': 15,
    #             'line': {'width': 0.5, 'color': 'white'}
    #         },
    #         type='scatter'
    #     )],
    #     'layout': dict(
    #         xaxis={'type': 'log', 'title': 'GDP Per Capita',
    #                'range':[2.3, 4.8]},
    #         yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
    #         margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
    #         legend={'x': 0, 'y': 1},
    #         hovermode='closest',
    #         transition = {'duration': 500},
    #     )
    # }


@app.callback(
    Output('container', 'children'),
    [Input('btn-1', 'n_clicks'),
    Input('btn-2', 'n_clicks')]
)
def example3(btn1, btn2):
    ctx = dash.callback_context

    if not ctx.triggered:
        button = "No clicks yet"
    else:
        button = ctx.triggered[0]['prop_id']

    return html.Div([
        html.Table([
            html.Tr([html.Th('Button 1'),
                     html.Th('Button 2'),
                     html.Th('Most Recent Click')]),
            html.Tr([html.Td(btn1 or 0),
                     html.Td(btn2 or 0),
                     html.Td(button)])
        ])
    ])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
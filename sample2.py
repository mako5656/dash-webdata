import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#000000',
    'text': '#ffffff'
}

app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'background-color': colors['background']
        }
    ),

    html.Div(
        children='Dash: A web application framework for Python.',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'background-color': colors['background']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [25, 15, 29], 'type': 'log', 'name': 'sample1'},
                {'x': [1, 2, 3], 'y': [20, 27, 15], 'type': 'log', 'name': 'sample2'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font':{
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

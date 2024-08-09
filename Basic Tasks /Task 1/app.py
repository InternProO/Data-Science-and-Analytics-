import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Data Visualization Tool"),
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload Dataset'),
        multiple=False
    ),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='histogram')
])

# Callback to handle file upload
@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('histogram', 'figure')],
    [Input('upload-data', 'contents')]
)
def update_graph(contents):
    if contents is None:
        raise PreventUpdate

    # Read the dataset from the uploaded file
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

    # Generate insights
    scatter_fig = px.scatter(df, x=df.columns[0], y=df.columns[1],
                            title='Scatter Plot of First Two Columns')
    histogram_fig = px.histogram(df, x=df.columns[0], title='Histogram of First Column')

    return scatter_fig, histogram_fig

if __name__ == '__main__':
    app.run_server(debug=True)

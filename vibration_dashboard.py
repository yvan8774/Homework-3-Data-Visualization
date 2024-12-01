# Let's import necessary libraries
import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input,Output
import plotly.express as px

# Let's load the dataset
data = pd.read_csv('C:\\Users\\User\\OneDrive\\Desktop\\Homework-3-Data-Visualization-1\\data\\vibration_data.csv')

# Let's calculate vibration magnitude
data['Magnitude'] = np.sqrt(data['x']**2 + data['y']**2 + data['z']**2)

#Let's create the Dash app
app = Dash(__name__)
app.title = "ACCELEROMETER VIBRATION'S MAGNITUDE (m/s²)"  

# App layout
app.layout = html.Div([
    html.H1("ACCELEROMETER VIBRATION'S MAGNITUDE (m/s²)", style={'textAlign': 'center'}),
    
    # Dropdown to select plot type
    html.Label("Select Plot Type:"),
    dcc.Dropdown(
        id='plot-type',
        options=[
            {'label': 'Line Plot (Magnitude over Index)', 'value': 'line'},
            {'label': 'Histogram (Magnitude Distribution)', 'value': 'histogram'}
        ],
        value='line',
        style={'width': '50%'}
    ),
    
    # Range slider to filter data by sample index
    html.Label("Select Sample Range:"),
    dcc.RangeSlider(
        id='sample-range',
        min=0,
        max=len(data),
        step=1000,
        marks={i: str(i) for i in range(0, len(data)+1, len(data)//5)},
        value=[0, 10000]  # Default range
    ),
    
    # Div for the interactive plot
    dcc.Graph(id='interactive-plot')
])

# Callback to update the plot
@app.callback(
    Output('interactive-plot', 'figure'),
    [Input('plot-type', 'value'),
     Input('sample-range', 'value')]
)
def update_plot(plot_type, sample_range):
    # Filter the data based on the selected sample range
    filtered_data = data.iloc[sample_range[0]:sample_range[1]]

    # Generate the selected plot
    if plot_type == 'line':
        fig = px.line(
            filtered_data,
            y='Magnitude',
            title="Vibration Magnitude Over Sample Index",
            labels={'index': 'Sample Index', 'Magnitude': 'Magnitude (m/s²)'}
        )
    elif plot_type == 'histogram':
        fig = px.histogram(
            filtered_data,
            x='Magnitude',
            nbins=50,
            title="Histogram of Vibration Magnitudes",
            labels={'Magnitude': 'Magnitude (m/s²)', 'count': 'Frequency'}
        )
        # Add mean and std lines
        mean = filtered_data['Magnitude'].mean()
        std = filtered_data['Magnitude'].std()
        fig.add_vline(x=mean, line_dash="dash", line_color="red", annotation_text="Mean")
        fig.add_vline(x=mean + std, line_dash="dash", line_color="orange", annotation_text="+1 Std Dev")
        fig.add_vline(x=mean - std, line_dash="dash", line_color="orange", annotation_text="-1 Std Dev")
    
    return fig

# Now let's run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

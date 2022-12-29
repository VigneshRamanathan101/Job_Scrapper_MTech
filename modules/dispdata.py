import os
import dash
from dash import dcc
from dash import html
import pandas as pd
import webbrowser

# get the current working directory
cwd = os.getcwd()
# construct the full path to the CSV file
csv_path = os.path.join(cwd, 'output', 'test.csv')

# read in the CSV file
df = pd.read_csv(csv_path,index_col=0)
# create a Dash app
app = dash.Dash()

# create a bar chart using the 'job title' and 'seniority level' columns from the dataframe
bar_chart = dcc.Graph(
    id='experience-with-job',
    figure={
        'data': [
            {
                'x': df['Job title'],
                'y': df['Seniority level'],
                'type': 'bar'
            }
        ],
        'layout': {
            'title': 'Experience required for with Various Job Listings'
        }
    }
)

# create a pie chart that displays the number of unique job titles
pie_chart = dcc.Graph(
    id='unique-job-titles',
    figure={
        'data': [
            {
                'labels': df['Job title'].unique(),
                'values': df['Job title'].value_counts(),
                'type': 'pie'
            }
        ],
        'layout': {
            'title': 'Number of Unique Job Titles'
        }
    }
)

# add the charts to the Dash app
app.layout = html.Div(children=[bar_chart, pie_chart])

# run the app
if __name__ == '__main__':
    url='http://127.0.0.1:8050/'
    webbrowser.open(url)
    app.run_server(port=8050, debug=False)
    

# Import
import dash
from dash import html
from dash import dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd



def dispdata():
    app = dash.Dash()


    df=pd.read_csv("output/test.csv")
    df2 = df.drop(df.columns[0],axis=1)
    #print(df['Employment type'].value_counts())
    print(df['City'].value_counts())
    #print(df2.nunique())





    # Finally display the 
    #if __name__ == "__main__":
    #    app.run_server(debug=True)
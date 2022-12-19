import pandas as pd

def edat(op):
    jobdata= pd.read_csv(op)
    print(jobdata.head())

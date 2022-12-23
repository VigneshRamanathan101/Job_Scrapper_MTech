# Import dependancies
import pandas as pd

def edat(op,job,loc):

    df= pd.read_csv(op)
    jobdata = df.drop(df.columns[0],axis=1)
    jobdata["Seniority level"] = jobdata["Seniority level"].replace(['Not Applicable'], 'Freelance/Other')
    print(loc)
    print("here")
    

    tjobs=["Machine Learning Engineer","Data Scientist","Data Analyst"]
    for k in range(len(tjobs)):
        print("Forloop")
        if tjobs[k]== job:
            ojobo=tjobs[k-1]
            ojobt=tjobs[k-2]


    jobdata['Employment type']=jobdata['Employment type'].fillna("Other")
    jobdata['Job function']=jobdata['Job function'].fillna(job)
    jobdata['Industries']=jobdata['Industries'].fillna("IT Services and IT Consulting")
    jobdata['Seniority level']=jobdata['Seniority level'].fillna("Freelance/Other")


    # Clean Data a little bit
    for i in range(len(jobdata.index)):
        a=jobdata.loc[i,'Job title']
        b=job.upper()

        if job in a:
            jobdata.loc[i,'Job title']=job
        elif b in a:
            jobdata.loc[i,'Job title']=job

        if ojobo in a:
            jobdata.loc[i,'Job title']=ojobo
        elif ojobt in a:
            jobdata.loc[i,'Job title']=ojobt

    #Clean location
    for j in range(len(jobdata.index)):
        c=jobdata.loc[i,'City']
        if loc in c:
            jobdata.loc[i,'City']=loc
        else:
            jobdata.loc[i,'City']=loc

    print("Data Cleaning Done")
    print("Displaying Data now")
    jobdata.to_csv('output/test.csv')
    print("Data Cleaning done")
    

# EDA using web Scrapper by Akil Ajith,Ajay Thomas and Vignesh Ramanathan
# Import Files
import os
import pandas as pd
import modules
import glob
from modules import input_user as i
from modules import scrapper as s
from modules import dispdata as dd
import output
from modules import eda as op
from output import *

print("Welcome to AAV's Job Scrapper EDA program")

path='output/output.csv'
cpath='output/choice.txt'
isFile = os.path.isfile(path)
isCFile = os.path.isfile(cpath)

def choose():
      print("""Choose your Job Title
      1.Machine Learning Engineer
      2.Data Scientist
      3.Data Analyst""")

      job=i.get_job()
      print("""Choose your Job Location
            1.Banglore
            2.Chennai
            3.Mumbai""")
      loc=i.get_loc()

      with open('output/choice.txt', 'w') as f:
            f.write(job+","+loc)

      #Scraping Linkedin for Jobs
      print("Web Scrapping Now")
      csvf=s.scrap_job(job,loc)
      print(" Web Scraping Done and Output Saved")

if isFile: 
      print("Previous Output for exists")
      with open('output/choice.txt', 'r') as f:
            lines = f.read()
            splitline=lines.split(',')
            job=splitline[0]
            loc=splitline[1]
      print(f"Previous Choosen Job was: {job}")
      print(f"Previous Choosen Location was: {loc}")
      print("Do You want to use Previous Choice Or New Choice: \
            1.Previous Choice. \
            2.New Choice.")
      nc=i.ponc()
      if nc == 2:
            choose()
else:
      choose()


#Performing Data Cleaning 
csv=open(path,'r')
peda=op.edat(csv,job,loc)
dd.dispdata()




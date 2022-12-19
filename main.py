# EDA using web Scrapper by Akil Ajith,Ajay Thomas and Vignesh Ramanathan
# Import Files
import modules
import glob
from modules import input_user as i
from modules import scrapper as s
import output
from modules import eda as op
from output import *

print("Welcome to AAV's Job Scrapper EDA program")
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

#Scraping Linkedin for Jobs
print("Web Scrapping Now")
csvf=s.scrap_job(job,loc)

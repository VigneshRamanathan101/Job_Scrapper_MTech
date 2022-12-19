# EDA using web Scrapper by Akil Ajith,Ajay Thomas and Vignesh Ramanathan
# Import Files
import input_user as i
import scrapper as s


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

print("Web Scrapping Now")
s.scrap_job(job,loc)
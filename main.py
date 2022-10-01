from asyncio import exceptions
from ssl import Options
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup


job_role = input("Enter Job role: ")
location = input("location [Null]: ")

url = f"https://www.linkedin.com/jobs/search?keywords={job_role}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    
try:
    request = requests.get(url)
except:
    print("couldn't reach the requested webpage :|")

# print response
print(request, "\n\n\n")
  
# print url
print(request.url, "\n\n\n")

try:
    soup = BeautifulSoup(request.content,"lxml")

    #print(soup)
except Exception as e:
    print("!!! \t\t Error Occured \t\t !!!\n\n\n")
    print(e)

jobs = soup.find_all(class_ = "base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")
print(jobs[0].text)

print(len(jobs))

#show-more-less-html__markup

#https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7

#infinite-scroll
from asyncio import exceptions
from ssl import Options
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

#input
job_role = "Data Science" #input("Enter Job role: ")
location = "" #input("location [Null]: ")

url = f"https://www.linkedin.com/jobs/search?keywords={job_role}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

# Web scrapper for infinite scrolling page
options = Options()
options.add_argument('--headless')
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'chromedriver.exe')     
driver.get(url)
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break 

'''   
try:
    request = requests.get(url)
except:
    print("couldn't reach the requested webpage :|")

# print response
print(request, "\n\n\n")
  
# print url
print(request.url, "\n\n\n")
'''

try:
    soup = BeautifulSoup(driver.page_source,"lxml")

    #print(soup)
except Exception as e:
    print("!!! \t\t Error Occured \t\t !!!\n\n\n")
    print(e)

jobs = soup.find_all(class_ = "base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")
print(jobs[0].text)

print(len(jobs))
print(url)
'''
#show-more-less-html__markup

#https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7

#infinite-scroll
'''
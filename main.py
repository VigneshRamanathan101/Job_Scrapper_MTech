from asyncio import exceptions
import queue
from ssl import Options
import time
import logging
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import requests
from bs4 import BeautifulSoup
import pandas as pd

#input
job_role = "Data Science" #input("Enter Job role: ")
location = "" #input("location [Null]: ")

url = f"https://www.linkedin.com/jobs/search?keywords={job_role}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
print(url)

# Web scrapper for infinite scrolling page
options = Options()
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get(url)
time.sleep(1)  # Allow 2 seconds for the web page to open
scroll_pause_time = 3 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
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
    print("Scrolling by Infinite Page")

queue = [0,0,0,0,0]
while True:
    #if 'see more jobs' found
    try:
        See_more_jobs = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[2]/button")
    except:
        break
    if See_more_jobs:
        See_more_jobs.click()
        time.sleep(scroll_pause_time)
    else:
        break
    post = driver.find_elements(By.CSS_SELECTOR,'a.base-card__full-link.absolute.top-0.right-0.bottom-0.left-0.p-0.z-\[2\]')
    queue.append(len(post))
    queue.pop(0)
    if sum(queue)//len(queue) == queue[0]:
        break
    print(len(post))


try:
    soup = BeautifulSoup(driver.page_source,"lxml")
except Exception as e:
    print("!!! \t\t Error Occured \t\t !!!\n\n\n")
    print(e)
    
driver.quit() # close the selenium sessions
jobs = soup.find_all(class_ = "base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")
cols = ['Job title', 'Job link', 'city', 'Seniority level','Employment type', 'Job function', 'Industries']
df = pd.DataFrame(columns= cols )
df_list = []

def detailed_job_post(job_post_link):
    data = {'Seniority level' : 'NA', 'Employment type' : 'NA', 'Job function' : 'NA', 'Industries' : 'NA'}
    try:
        sub_link = requests.get(job_post_link)
    except:
        return data
    sub_link_data = BeautifulSoup(sub_link.text,"lxml")
    list = sub_link_data.find_all( class_ = "description__job-criteria-subheader")                                           # 3
    list_value = sub_link_data.find_all( class_ = "description__job-criteria-text description__job-criteria-text--criteria") # 4
    for i in range(len(list)) :
        data[list[i].text.strip()] = list_value[i].text.strip()
    return data


for job_post in jobs:
    link = job_post.get('href')                      # 1
    title = job_post.text.strip()                    # 2
    value = detailed_job_post(link)
    company = ((job_post.find_next_sibling('div',"base-search-card__info")).find(class_ = "base-search-card__subtitle")).text.strip()
    #company_link = 
    city = (job_post.find_next_sibling('div',"base-search-card__info")).find(class_ = "job-search-card__location").text.strip()
    value['city'] = city
    value['Job link'] = link
    value['Job title'] = title
    print(f'{len(df_list)+1}/{len(jobs)}',value)
    df_list.append([ title, link, city, value['Seniority level'], value['Employment type'], value['Job function'], value['Industries']])

new_df = pd.DataFrame(df_list, columns= cols) 
output = pd.concat([df, new_df],axis = 0).to_csv('output.csv')


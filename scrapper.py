from asyncio import exceptions
import queue
from ssl import Options
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


def scrap_job(job_role,location):
    url = f"https://www.linkedin.com/jobs/search?keywords={job_role}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    print(url)

    # Web scrapper for infinite scrolling page
    options = Options()
    #options.add_argument('--headless')
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    driver = webdriver.Chrome(chrome_options = options, executable_path=r'chromedriver.exe')     
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
        if len(post)>1000:
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
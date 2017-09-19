import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
import lxml

from userAgents import user_agents, randomUserAgents

start = time.time()

url = 'https://play.google.com/store/apps/collection/topselling_free'
head = randomUserAgents()

driver = webdriver.Chrome()
driver.get('{}'.format(url))
time.sleep(2)

for i in range(0,60):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(2)
	try:
		showMore = driver.find_element_by_css_selector('#show-more-button')
		showMore.click()
	except:
		continue

pageSource = driver.page_source
bs = BeautifulSoup(pageSource)
count = 0

#chart = bs.find('div',{'class','id-card-list card-list two-cards'})
#for app in chart.
for apps in bs.findAll('div',{'class',
           'card no-rationale square-cover apps small'}):
    tit = apps.find('a',{'class','title'}).text
    # title = tit[1].strip()
    # rank = tit[0].strip()
    print(tit)
    count += 1
print(count)
driver.close()
print(start - time.time())

from selenium import webdriver
from selenium.webdriver.common.by import By
#Keep Chrome Browser Open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


#Open Chrome Browser
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")


dates_dict = []

event_dates = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_links = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

events = {}

for item in range(len(event_dates)):
 events[item]={
  "time": event_dates[item].text,
  "name": event_links[item].text
 }

print(events)

driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")

events_dict = {i : {"2022-"+event_dates[i].text : event_names[i].text} for i in range(len(event_dates))}
print(events_dict)

driver.quit()
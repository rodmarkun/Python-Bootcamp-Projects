from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
no_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(no_articles.text)

driver.close()

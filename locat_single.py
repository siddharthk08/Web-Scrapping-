from selenium import webdriver
from selenium.webdriver.common.keys import Keys # to import return keys
from selenium.webdriver.common.by import By
import time
query="laptop"
driver = webdriver.Chrome()
driver.get(f"https://www.amazon.in/s?k={query}&crid=3IVMJHJ84VNQX&sprefix=lap%2Caps%2C194&ref=nb_sb_ss_pltr-sample-20_2_3")
elem = driver.find_element(By.CLASS_NAME, "puis-card-container")
#print(elem.text)
print(elem.get_attribute("outerHTML"))
time.sleep(2)
driver.close()
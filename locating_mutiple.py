from selenium import webdriver
from selenium.webdriver.common.keys import Keys # to import return keys
from selenium.webdriver.common.by import By
import time
query="laptop"
driver = webdriver.Chrome()
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=3IVMJHJ84VNQX&sprefix=lap%2Caps%2C194&ref=nb_sb_ss_pltr-sample-20_2_3")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
#print(elem.text)
    print(f"{len(elems)}items found")
    for elem in elems:
        print(elem.text)

time.sleep(2)
driver.close()
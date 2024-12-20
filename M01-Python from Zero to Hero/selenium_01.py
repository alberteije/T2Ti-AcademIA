from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

campo_busca = driver.find_element(By.NAME, "q")
campo_busca.send_keys("T2Ti")
campo_busca.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/webhp?hl=en")

searchFieldElement = driver.find_element(By.NAME, "q")
searchFieldElement = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
searchFieldElement.clear()
searchFieldElement.send_keys("suzuki")
searchFieldElement.send_keys(Keys.ENTER)
time.sleep(5)
imageButton = driver.find_element(By.LINK_TEXT, "Images")
imageButton.click()
time.sleep(1)
firstImage = driver.find_element(By.NAME, "sTFXNd")
driver.close()



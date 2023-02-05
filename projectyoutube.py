
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
driver.get("https://www.youtube.com")
searchFieldElement = driver.find_element(By.NAME, "search_query")
searchFieldElement.clear()
searchFieldElement.send_keys("adele")
searchFieldElement.send_keys(Keys.ENTER)
searchFieldElement.click()
musicButton = driver.find_element(By.CSS_SELECTOR, "#thumbnail > yt-image > img")
musicButton.click()
time.sleep(10)

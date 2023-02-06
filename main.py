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
searchFieldElement = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
searchFieldElement.clear()
searchFieldElement.send_keys("audi")
searchFieldElement.send_keys(Keys.ENTER)
time.sleep(1)
imageButton = driver.find_element(By.LINK_TEXT, "Images")
imageButton.click()
time.sleep(1)
firstImage = driver.find_element(By.XPATH, "(//a[@class='wXeWr islib nfEiy'])[1]")
# firstImage = driver.find_element(By.XPATH, "//div[@data-ved='2ahUKEwj0qri60oH9AhVln_0HHSUbBFUQMygAegUIARDaAQ']")
# firstImage = driver.find_element(By.XPATH, "//img[@alt='Suzuki Auto South Africa Head Office | New Car Deals']")
firstImage.click()
time.sleep(5)
driver.close()




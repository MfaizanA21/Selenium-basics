import os
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#os.environ['PATH'] += r"C:\SeleniumDrivers\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/progressbar/#download")
driver.switch_to.frame(0)
wait = WebDriverWait(driver, 10)
my_element = wait.until(EC.element_to_be_clickable((By.ID, "downloadButton")))
my_element.click()
time.sleep(10)


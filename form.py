import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
wait = WebDriverWait(driver, 1)

firstName = wait.until(ec.visibility_of_element_located((By.NAME, 'firstname')))
firstName.click()
firstName.send_keys("John")

lastName = wait.until(ec.visibility_of_element_located((By.NAME, 'lastname')))
lastName.click()
lastName.send_keys("Doe")

gender = wait.until(ec.visibility_of_element_located((By.ID, 'sex-0')))
gender.click()

experience = wait.until(ec.visibility_of_element_located((By.ID, 'exp-2')))
experience.click()

date = wait.until(ec.visibility_of_element_located((By.ID, 'datepicker')))
date.click()
date.send_keys(str(datetime.date.today()))

profession = wait.until(ec.visibility_of_element_located((By.ID, 'profession-1')))
profession.click()

automation = wait.until(ec.visibility_of_element_located((By.ID, 'tool-2')))
automation.click()

continent = wait.until(ec.visibility_of_element_located((By.ID, 'continents')))
continent.click()
dropdown: WebElement = driver.find_element(By.ID, 'continents')
dropdown.find_element(By.XPATH("//option[. = 'Europe']")).click()

dropdown: WebElement = driver.find_element(By.ID, 'selenium commands')
dropdown.find_element(By.XPATH("//option[. = 'Browser commands']")).click()

submit = wait.until(ec.visibility_of_element_located((By.ID, 'submit')))
submit.click()

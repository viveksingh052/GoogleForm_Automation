from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time


options = Options()
service = Service("C:/Users/vs292/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform?pli=1")
wait = WebDriverWait(driver, 10)


first_name_input = wait.until(Expect.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
first_name_input.send_keys("Vivek")

contact_number_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
contact_number_input.send_keys("8360210146")

email_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
email_input.send_keys("vs292713@gmail.com")

address_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')))
address_input.send_keys("H-1687 Keshavpuram Kalyanpur Kanpur Avas Vikas NO-1")

pincode_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
pincode_input.send_keys("208017")


dob_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
dob_input.clear()
dob_input.send_keys("2003-03-04")

GENDER_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
GENDER_input.send_keys("Male")

TYPE_input = wait.until(Expect.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
TYPE_input.send_keys("GNFPYC")

submit_button_xpath = "//span[contains(text(),'Submit')]"
submit_button = wait.until(Expect.element_to_be_clickable((By.XPATH, submit_button_xpath)))
submit_button.click()


time.sleep(50)
driver.quit()

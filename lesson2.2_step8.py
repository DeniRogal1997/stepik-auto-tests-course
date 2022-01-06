from selenium import webdriver
from selenium.webdriver.common.by import By
import os
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'p.txt')

browser.find_element(By. ID, "file").send_keys(file_path)

required_elements = browser.find_elements(By. CSS_SELECTOR, '.form-group input[required]')
for element in required_elements:
    element.send_keys('required')

browser.find_element(By. CSS_SELECTOR, ".btn.btn-primary").click()
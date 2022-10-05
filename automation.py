from selenium import webdriver
import webbrowser
import time 
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from selenium.webdriver.chrome.options import Options

links = []
with open("link2.txt", "r") as file:
  links = file.read().splitlines()
  

for i in range(len(links)):

  chrome_options = Options()
  chrome_options.add_extension('IDMInterationModule.crx')

  driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
  driver.get(links[i])
  time.sleep(6)
  try:
    driver.find_element_by_id("itfloater_closeev").click()
    time.sleep(3)
    buttons = driver.find_elements_by_css_selector('.btn.btn-success')
    driver.execute_script("arguments[0].click();", buttons[3])
    time.sleep(3)
    try:
      driver.switch_to.window(driver.window_handles[1])
      driver.find_elements_by_css_selector('#sddlbtn')[0].click()
    except:
      driver.switch_to.window(driver.window_handles[0])
      driver.execute_script("arguments[0].click();", buttons[2])
      driver.switch_to.window(driver.window_handles[2])
      driver.find_elements_by_css_selector('#sddlbtn')[0].click()
    print("Video number ", i+1, " started downloading out of total videos ", len(links))
    time.sleep(10)
    driver.quit()
  except:
    continue
  
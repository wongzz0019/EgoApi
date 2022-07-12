import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://t143.5vh.cn/?from_source=&user_openid=&openid=oElvTjqhxQPuUVTBCuw72vpUGQqM#/index')
driver.maximize_window()
driver.find_element(By.CLASS_NAME, 'bt2').click()

time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/img[2]')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('../drivers/chromedriver')


driver.set_page_load_timeout(10)
driver.get('https://www.google.com')
driver.maximize_window()
driver.find_element_by_name('q').send_keys('What is the Weather today?')
# driver.find_element_by_name('q').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_name('btnK').click()
time.sleep(4)
driver.quit()

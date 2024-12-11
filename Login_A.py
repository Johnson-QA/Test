from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Test(unittest.TestCase):

  def test_01_Login_admin(self):
      driver.get('https://aws-dev.welltivity.cn/admin/#/login')
      driver.maximize_window()
      driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/input').send_keys("15221888544")
      driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div/div/input').send_keys("21888544_JS#")
      driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/button').click()
      sleep(5)
      driver.delete_all_cookies()

  def test_02_Login_mall(self):
      driver.get('https://aws-dev.welltivity.cn/mall/#/login')
      driver.maximize_window()
      driver.find_element("xpath", '/html/body/div/div/div/div/form/div[2]/div/div/input').clear()
      driver.find_element("xpath", '/html/body/div/div/div/div/form/div[2]/div/div/input').send_keys("15221888544")
      driver.find_element("xpath", '/html/body/div/div/div/div/form/div[3]/div/div/input').send_keys("21888544_JS#")
      driver.find_element("xpath", '/html/body/div/div/div/div/form/div[4]/div/button').click()
      sleep(5)
      driver.quit()
from selenium import webdriver
from time import sleep
import unittest

opt = webdriver.ChromeOptions()
browser = webdriver.Chrome(options = opt)

class Test(unittest.TestCase):

  def test_01_Login_admin(self):
      browser.get('https://aws-dev.welltivity.cn/admin/#/login')
      browser.maximize_window()
      browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/input').send_keys("15221888544")
      browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div/div/input').send_keys("21888544_JS#")
      browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/button').click()
      sleep(5)
      browser.delete_all_cookies()

  def test_02_Login_mall(self):
      browser.get('https://aws-dev.welltivity.cn/mall/#/login')
      browser.maximize_window()
      browser.find_element("xpath", '/html/body/div/div/div/div/form/div[2]/div/div/input').clear()
      browser.find_element("xpath", '/html/body/div/div/div/div/form/div[2]/div/div/input').send_keys("15221888544")
      browser.find_element("xpath", '/html/body/div/div/div/div/form/div[3]/div/div/input').send_keys("21888544_JS#")
      browser.find_element("xpath", '/html/body/div/div/div/div/form/div[4]/div/button').click()
      sleep(5)
      browser.quit()
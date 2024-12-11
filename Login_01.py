from selenium import webdriver # 匯入 selenium 的 webdriver
from time import sleep         # 匯入內建 time 模組的 sleep() 函式

opt = webdriver.ChromeOptions() # 建立選項物件
browser = webdriver.Chrome(options = opt) # 以 options 參數來建立瀏覽器物件
      
browser.get('https://aws-dev.welltivity.cn/admin/#/login') # 開啟 Chrome 並連到登入頁面
browser.maximize_window() # 將視窗最大化
browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div/input').send_keys("15221888544") # 輸入帳號
browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/div[2]/div/div/div/input').send_keys("21888544_JS#") # 輸入密碼
browser.find_element("xpath", '/html/body/div[1]/div/div[2]/div[2]/form/button').click() # 按下登入按鈕
sleep(5) # 登入後停留在頁面5秒鐘
browser.quit() # 關閉瀏覽器
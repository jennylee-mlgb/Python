# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:00:18 2019

@author: ISSMRZ4
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'above Select package is needed for dropdown'
import time
driver = webdriver.Chrome(executable_path = "C:\\ProgramData\\Anaconda3\\selenium\\chromedriver.exe")    
#driver = webdriver.Chrome(executable_path = "C:\\Users\\issmrz4\\Desktop\\python\\selenium\\chromedriver.exe")


#driver = webdriver.Chrome()
#driver1 = webdriver.Chrome()
#time.sleep(5)
#driver.implicitly_wait(10)

driver.get("https://jpsp.contact.aig.net/AJH/harmony/SitePages/AIG-Harmony_06.aspx")
#driver.get("http://access63.aig.co.jp/ActiveDirectoryLogin/ADLoginForm.aspx")
#assert "AIG Harmony" in driver.title
#driver.get("http://access49.aig.co.jp/msg/YOYAKU/select.ASP")
#driver.get("http://access49.aig.co.jp/msg/YOYAKU/USER_YOYAKU.ASP?SK_CD=10500")

driver.find_element_by_link_text("予約ログインはここをクリック").click()

print(driver.window_handles)

action=webdriver.ActionChains(driver=driver)

if (len(driver.window_handles)==2):
    driver.switch_to.window(window_name=driver.window_handles[-2])
    driver.close()
    driver.switch_to.window(window_name=driver.window_handles[0])
    

obj = Select(driver.find_element_by_name("compDropDownList"))
obj.select_by_visible_text('AIG損害保険株式会社')

username=driver.find_element_by_id("txtUsername")
password=driver.find_element_by_id("txtPassword")

username.send_keys("ISSMRZ4")
password.send_keys("XNNMAN@1990")

driver.find_element_by_name("btnLogin").click()
time.sleep(5)


#driver.find_element_by_link_text("神谷町　MTビル").click()

driver.find_element_by_link_text("神谷町　MTビル").click()
##################################################
time.sleep(5)

window_before=driver.window_handles[0]

tableData=driver.find_elements_by_xpath("/html/body/center/table[2]/tbody/tr")
#print(len(tableData))

# tableData = WebElement, tr = WebElement
for tr in tableData:
    if "17:10 - 17:50" in tr.text or "18:10 - 18:50" in tr.text or "16:10 - 16:50" in tr.text or "15:10 - 15:50" in tr.text or "14:10 - 14:50" in tr.text or "13:10 - 13:50" in tr.text:
#    if "17:10 - 17:50" in tr.text or "16:10 - 16:50" in tr.text:
        print(tr.text)
        tdData = tr.find_elements_by_xpath("td")
        for td in tdData:    
            if "×" not in td.text and len(td.text) == 1:
                
                print("td value: " + td.text)
                driver.switch_to.frame(td.click())
                
                time.sleep(5)
                
                window_after=driver.window_handles[1]
                driver.switch_to.window(window_after) 
                driver.find_element_by_name("SEND").click()
                
                                

    '''
    time.sleep(5)
    if len(driver.window_handles) > 0 : 
        #print(len(driver.window_handles))
        print("cp1: " + driver.current_url)

        window_after=driver.window_handles[1]
        driver.switch_to.window(window_after) 
        print("cp2: " + driver.current_url)
    '''
    
 
    # Requires sleep method
    #driver.find_element_by_name("SEND").click()


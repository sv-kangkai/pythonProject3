import os
import time
from selenium.webdriver.firefox.options import Options as options
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

new_binary_path = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
ops = options()
ops.binary_location = new_binary_path

# firefox_binary = FirefoxBinary(binary)

if __name__ == "__main__":
    var = 1
    while var == 1:
        try:
            print('========================')
            print('启动Tor浏览器，并获取IP地址')
            browser = webdriver.Firefox(options=ops)
            browser.find_element(By.ID, 'connectButton').click()
            time.sleep(10)
            browser.get('http://ipinfo.io/json')
            html = browser.page_source
            soup = BeautifulSoup(html, 'lxml')
            dict_from_json = json.loads(soup.text)
            print('启动成功，网络环境如下：')
            print('当前IP：' + dict_from_json['ip'])
            print('当前城市：' + dict_from_json['city'])
            print('当前地区：' + dict_from_json['region'])
            print('当前国家：' + dict_from_json['country'])
            time.sleep(1)
            site_url = 'https://link-center.net/416534/make-chocolate-cake'
            browser.get(site_url)
            time.sleep(3)
        except:
            continue
        #跳过人机验证，直接访问URL
        try:
            browser.find_element(By.XPATH, '//button[@class=" css-6dzqka"]').click()
        except:
            None

        try:
            browser.execute_script("___grecaptcha_cfg.clients['0'].l.l.callback()")
            #有时候用户协议会出现的比较晚，在真正处理逻辑之前尝试点击一次用户协议，点击正确与否都继续下面的逻辑处理
            try:
                browser.find_element(By.XPATH, '//button[@class=" css-6dzqka"]').click()
            except:
                None
            browser.find_elements(By.XPATH, "//a[@class='lv-button-component new-button-style lv-dark-btn ng-star-inserted']")[0].click()
            time.sleep(0.5)
            browser.find_element(By.XPATH, "//h5[@class='h5-mobile-small display-web-short']").click()
            time.sleep(6)
            close_icon = browser.find_element(By.XPATH, '//div[@id="webModal"]//div[@class="close-icon"]')
            ActionChains(browser).click(close_icon).perform()
            time.sleep(0.5)
            browser.find_element(By.XPATH, "//h5[@class='h5-mobile-small display-notifications-short']").click()
            time.sleep(6)
            close_icon = browser.find_element(By.XPATH, '//div[@id="relatedTopicsModal"]//div[@class="close-icon"]')
            ActionChains(browser).click(close_icon).perform()
            time.sleep(0.5)
            browser.find_element(By.XPATH, "//a[@class='lv-button-component new-button-style lv-dark-btn ng-star-inserted']").click()
            print('结束任务并退出')
            print('========================')
            time.sleep(3)
        except:
            print('*** 任务出错，重试 ***')
        browser.quit()

import os
import time
from selenium.webdriver.firefox.options import Options as options
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

new_binary_path = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
ops = options()
ops.binary_location = new_binary_path

url_list = [
    'https://link-target.net/416534/costa-rica-in-4k',
    'https://direct-link.net/416534/breaking-bad-extras',
    'https://link-center.net/416534/make-chocolate-cake',
    'https://link-target.net/416534/50-facts-in-breaking-bad'
]

if __name__ == "__main__":
    var = 1
    while var == 1:
        try:
            print('========================')
            print('启动Tor浏览器')
            browser = webdriver.Firefox(options=ops)
            browser.find_element(By.ID, 'connectButton').click()
            browser.implicitly_wait(10)
            while var == 1:
                if browser.current_url == 'about:blank':
                    site_url = random.choice(url_list)
                    # site_url = 'https://direct-link.net/416534/breaking-bad-extras'
                    browser.set_page_load_timeout(60)
                    try:
                        browser.get(site_url)
                    except Exception as timeout:
                        browser.quit()
                    break
        except:
            continue
        #跳过人机验证，直接访问URL
        try:
            element = WebDriverWait(browser, 20, 0.5).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@id="qc-cmp2-ui"]//button[@class=" css-6dzqka"]'))
            )
            element.click()
        except:
            None

        try:
            try:
                browser.execute_script("___grecaptcha_cfg.clients['0'].l.l.callback()")
            except:
                None
            #有时候用户协议会出现的比较晚，在真正处理逻辑之前尝试点击一次用户协议，点击正确与否都继续下面的逻辑处理
            # try:
            #     browser.find_element(By.XPATH, '//div[@id="qc-cmp2-ui"]//button[@class=" css-6dzqka"]').click()
            # except:
            #     None
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
        except Exception as ex:
            print('*** 任务出错，重试 ***')
            print(str(ex))
        browser.quit()

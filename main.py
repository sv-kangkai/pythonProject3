import time
from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

if __name__ == '__main__':
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-blink-features")
    chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
    chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
    var = 1
    while var == 1:
        try:
            os.system('brew services restart tor')
            options = {
                'proxy': {
                    'http': 'socks5://127.0.0.1:9050',
                    'https': 'socks5://127.0.0.1:9050',
                    'no_proxy': 'localhost,127.0.0.1'
                }
            }
            chrome = webdriver.Chrome(seleniumwire_options=options)
            # chrome.get('https://ipinfo.io/json')
            chrome.get('https://link-center.net/416534/make-chocolate-cake')
            # chrome.get('https://shrinke.me/WXy72y')
            # element = WebDriverWait(chrome, 20).until(
            #     EC.presence_of_element_located((By.TAG_NAME, "body"))
            # )
            # chrome.switch_to.frame(0)  # 切换到iframe中，页面上唯一的iframe画面
            # chrome.find_element_by_class_name('rc-anchor-content').click()  # 找到iframe页面中的人机识别按钮，点击
            # chrome.switch_to.default_content()  # 切换回主文档
            # time.sleep(10)
            # chrome.find_element_by_id('continue').click()
            # time.sleep(20)
            # chrome.find_element_by_css_selector("a[href='#getlink']").click()
            # time.sleep(0.5)
            # chrome.find_element_by_id('getlink').click()
            # WebDriverWait(chrome, 600).until(
            #     EC.presence_of_element_located((By.TAG_NAME, "body"))
            # )
            # time.sleep(15)
            # WebDriverWait(chrome, 600).until(
            #     EC.presence_of_element_located((By.TAG_NAME, "body"))
            # )
            # chrome.find_element_by_css_selector("a[class='btn btn-success btn-lg get-link']").click()
            time.sleep(999)
            time.sleep(10)
            chrome.quit()
        except:
            print('Oops! Something wrong!')
            time.sleep(1)
            chrome.quit()

import time
from seleniumwire import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
import os

config = {
            'apiKey': 'ffa1ef7c0bd5157f4a52d222dacdc205',
            'defaultTimeout': 120,
            'recaptchaTimeout': 600,
            'pollingInterval': 10,
        }
solver = TwoCaptcha(**config)

if __name__ == '__main__':
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--disable-blink-features")
    chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
    chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
    var = 1
    while var == 1:
        try:
            # os.system('brew services restart tor')
            os.system("open /Applications/Tor\ Browser.app")
            time.sleep(20)
            options = {
                'proxy': {
                    'http': 'socks5://127.0.0.1:9150',
                    'https': 'socks5://127.0.0.1:9150',
                    'no_proxy': 'localhost,127.0.0.1'
                }
            }
            browser = webdriver.Chrome(seleniumwire_options=options)
            time.sleep(3)
            site_url = 'https://direct-link.net/416534/breaking-bad-extras'
            browser.get(site_url)
            # # 如果出现人机验证，破解
            # try:
            #     recaptch_obj = browser.find_element(By.CLASS_NAME, 'g-recaptcha')
            #     google_sitekey = recaptch_obj.get_attribute('data-sitekey')
            #     print(google_sitekey)
            #     print('Beginning solve reCaptcha ... ')
            #     result = solver.recaptcha(sitekey=google_sitekey, url=site_url)
            #     google_captcha_response_input = browser.find_element(
            #         By.ID, 'g-recaptcha-response')
            #
            #     # make input visible
            #     browser.execute_script(
            #         "arguments[0].setAttribute('style','type: text; visibility:visible;');",
            #         google_captcha_response_input)
            #     # input the code received from 2captcha API
            #     google_captcha_response_input.send_keys(result.get('code'))
            #     # hide the captch input
            #     browser.execute_script(
            #         "arguments[0].setAttribute('style', 'display:none;');",
            #         google_captcha_response_input)
            #     balance = solver.balance()
            #     # show 2captcha Balance.
            #     print(f'Your 2captcha balance is ${round(balance, 2)}')
            #     print('Solved.')
            # except:
            #     print('Can not resovle Google reCaptcha object. Error.')
            #
            # # 处理人机验证后的逻辑
            # submit_btn = browser.find_element(By.ID, 'continue')
            # browser.execute_script(
            #     "arguments[0].removeAttribute('disabled');",
            #     submit_btn)
            # # 点击页面会有3个弹出页面，要等待3个弹出页面后，才能进行页面跳转
            # page_title = browser.title
            # while page_title == 'Loan2Host':
            #     time.sleep(1)
            #     submit_btn.click()
            #     windows_handles = browser.window_handles
            #     browser.switch_to.window(windows_handles[0])
            #     page_title = browser.title
            #
            # try:
            #     browser.find_element(By.CSS_SELECTOR, '.fc-button.fc-cta-consent.fc-primary-button').click()
            # except:
            #     print('There is no popup window that you need to click, continue.')
            #
            # time.sleep(15)
            # browser.find_element(By.XPATH, "//a[@href='#getlink']").click()
            # browser.find_element(By.ID, 'getlink').click()
            # time.sleep(15)
            # element = browser.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg get-link']")
            # browser.execute_script('arguments[0].click();', element)
            # # browser.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg get-link']").click()
            # print('Done.')
            time.sleep(10)
            browser.quit()
        except:
            print('Got error!')

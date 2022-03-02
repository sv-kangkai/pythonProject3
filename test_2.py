import os
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

config = {
            'apiKey': 'ffa1ef7c0bd5157f4a52d222dacdc205',
            'defaultTimeout': 120,
            'recaptchaTimeout': 600,
            'pollingInterval': 10,
        }
solver = TwoCaptcha(**config)

# path to the firefox binary inside the Tor package
binary = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

if __name__ == "__main__":
    var = 1
    while var == 1:
        browser = webdriver.Firefox(firefox_binary=binary)
        browser.find_element(By.ID, 'connectButton').click()
        time.sleep(10)
        site_url = 'https://tei.ai/kPPKII'
        browser.get(site_url)
        # 如果出现人机验证，破解
        try:
            recaptch_obj = browser.find_element(By.CLASS_NAME, 'g-recaptcha')
            google_sitekey = recaptch_obj.get_attribute('data-sitekey')
            print(google_sitekey)
            print('Beginning solve reCaptcha ... ')
            result = solver.recaptcha(sitekey=google_sitekey, url=site_url)
            google_captcha_response_input = browser.find_element(
                By.ID, 'g-recaptcha-response')

            # make input visible
            browser.execute_script(
                "arguments[0].setAttribute('style','type: text; visibility:visible;');",
                google_captcha_response_input)
            # input the code received from 2captcha API
            google_captcha_response_input.send_keys(result.get('code'))
            # hide the captch input
            browser.execute_script(
                "arguments[0].setAttribute('style', 'display:none;');",
                google_captcha_response_input)
            balance = solver.balance()
            # show 2captcha Balance.
            print(f'Your 2captcha balance is ${round(balance, 2)}')
            print('Solved.')
        except:
            print('Can not resovle Google reCaptcha object. Error.')
            browser.quit()
            continue

        #处理人机验证后的逻辑
        submit_btn = browser.find_element(By.ID, 'continue')
        browser.execute_script(
            "arguments[0].removeAttribute('disabled');",
            submit_btn)
        # 点击页面会有3个弹出页面，要等待3个弹出页面后，才能进行页面跳转
        page_title = browser.title
        while page_title == 'Loan2Host':
            time.sleep(1)
            submit_btn.click()
            windows_handles = browser.window_handles
            browser.switch_to.window(windows_handles[0])
            page_title = browser.title

        try:
            browser.find_element(By.CSS_SELECTOR, '.fc-button.fc-cta-consent.fc-primary-button').click()
        except:
            print('There is no popup window that you need to click, continue.')

        try:
            time.sleep(15)
            browser.find_element(By.XPATH, "//a[@href='#getlink']").click()
            browser.find_element(By.ID, 'getlink').click()
            time.sleep(15)
            element = browser.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg get-link']")
            browser.execute_script('arguments[0].click();', element)
            # browser.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg get-link']").click()
            print('Done.')
            time.sleep(10)
        except:
            print('Unable to locate element: a href getlink')
            continue
        browser.quit()
    time.sleep(5)

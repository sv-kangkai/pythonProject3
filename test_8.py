from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_extension('~/Downloads/extension_1_6_6_0.crx')
chrome = webdriver.Chrome(options=options)
time.sleep(5)
chrome.get("http://ipinfo.io/json")
time.sleep(120)
chrome.quit()
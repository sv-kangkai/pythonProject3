import os
import time
import aircv as ac
from PIL import Image
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# path to the firefox binary inside the Tor package
binary = '/Applications/Tor Browser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
    raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = None


def get_browser(binary=None):
    global browser
    # only one instance of a browser opens, remove global for multiple instances
    if not browser:
        browser = webdriver.Firefox(firefox_binary=binary)
    return browser


class CompareImage():
    # 可以通过confidencevalue来调节相似程度的阈值，小于阈值不相似
    def matchImg(self, imgsrc, imgobj, phone_x, phone_y, confidencevalue=0):  # imgsrc=原始图像，imgobj=待查找的图片
        imsrc = ac.imread(imgsrc)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj, confidencevalue)
        print(match_result)
        if match_result is not None:
            match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽
            x, y = match_result['result']  # 标准图中小图位置x,y
            shape_x, shape_y = tuple(map(int, match_result['shape']))  # 标准图中x,y
            position_x, position_y = int(phone_x * (x / shape_x)), int(phone_y * (y / shape_y))
        else:
            return None, None, None, None
        # print(match_result)
        # return match_result
        return position_x, position_y, str(match_result['confidence'])[:4], match_result

    def fixed_size(self, width, height, infile, outfile):
        """按照固定尺寸处理图片"""
        im = Image.open(infile)
        out = im.resize((width, height), Image.ANTIALIAS)
        out.save(outfile)

    def get_picture_size(self, imgsrc):
        '''获取图片长，宽'''
        imsrc = ac.imread(imgsrc)
        y, x, z = imsrc.shape
        return x, y


if __name__ == "__main__":
    browser = get_browser(binary=firefox_binary)
    browser.find_element_by_id('connectButton').click()
    WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    browser.get('https://ipinfo.io/json')
    WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    time.sleep(2)
    # browser.get('https://za.uy/d7Y6OLH')
    # browser.get('https://shrinke.me/WXy72y')
    browser.get('https://link-center.net/416534/make-chocolate-cake')
    WebDriverWait(browser, 600).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    browser.get_screenshot_as_file('./res/screen.png')

    result = CompareImage().matchImg("./res/screen.png", "./res/icon.png", 10, 10)
    print('相似度：' + str(result))
    element = browser.find_element_by_id('greendot')
    action = ActionChains(browser)
    # action.move_to_element(element).click().perform()
    # action.move_by_offset(result[3]["rectangle"][0][0], result[3]["rectangle"][0][1]).click().perform() # 鼠标左键点击， 200为x坐标， 100为y坐标
    time.sleep(9999)
    browser.quit()

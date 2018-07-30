from selenium import webdriver
import time

"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
"""


def getHtml(url, loadmore=True, waittime=10):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)
    time.sleep(waittime)
    if loadmore:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                # next_button = browser.find_elements_by_xpath("//*[@id="app"]/div/div[1]/a")
                # next_button = browser.find_element_by_link_text("加载更多")
                next_button.click()
                time.sleep(waittime)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html

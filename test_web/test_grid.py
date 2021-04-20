# coding=utf-8
from selenium import webdriver
import os

chrome_driver = os.path.abspath(r"E:\Python3.6.0\chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chrome_driver
chrome_capabilities = {
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    "webdriver.chrome.driver": chrome_driver
}
browser = webdriver.Remote(command_executor="http://192.168.190.128:5555/wd/hub", desired_capabilities=chrome_capabilities)
browser.get("http://www.baidu.com")
print(browser.title)
browser.quit()

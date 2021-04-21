# coding=utf-8
import pytest
from common.base_page_web import BasePage
from common.log_main import logger
# from selenium import webdriver
# import os
# chrome_driver = os.path.abspath(r"E:\Python3.6.0\chromedriver.exe")
# os.environ["webdriver.chrome.driver"] = chrome_driver
# chrome_capabilities = {
#     "browserName": "chrome",
#     "version": "",
#     "platform": "ANY",
#     "javascriptEnabled": True,
#     "webdriver.chrome.driver": chrome_driver
# }
# browser = webdriver.Remote(command_executor="http://192.168.190.128:5555/wd/hub", desired_capabilities=chrome_capabilities)


class TestWeb:
    def setup_class(self):
        self.driver = BasePage(dcs='hub')

    def setup(self):
        self.driver.get('https://www.baidu.com')

    def teardown(self):
        self.driver.quit()

    def test_web1(self):
        logger.info('test_web1')

    def test_web2(self):
        logger.info('test_web2')

    def test_web3(self):
        logger.info('test_web3')

    def test_web4(self):
        logger.info('test_web4')

if __name__ == '__main__':
    pytest.main(['test_grid.py','-sq','-n','4'])
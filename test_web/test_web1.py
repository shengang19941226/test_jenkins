import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from common.base_page_web import BasePage
from common.log_main import logger

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
    pytest.main(['test_usehadless1.py','-sq','-n','4'])

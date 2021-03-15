import pytest,allure
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from common.log_main import logger
from common.base_page_web import BasePage

@allure.feature('测试2')
class TestDemo:
    def setup_class(self):
        self.driver = BasePage(dcs='hub')

    def setup(self):
        self.driver.get('https://taobao.com')

    def teardown(self):
        self.driver.quit()

    def test_web5(self):
        logger.info('test_web5')

    def test_web6(self):
        logger.info('test_web6')

    def test_web7(self):
        logger.info('test_web7')

    def test_web8(self):
        logger.info('test_web8')

if __name__ == '__main__':
    pytest.main(['test_web2.py','-sq','-n','4'])
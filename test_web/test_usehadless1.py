import configparser

from selenium.webdriver import DesiredCapabilities

from common.base_page_web import BasePage
import pytest,os ,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class TestWeb:

    def setup(self):
        self.driver = BasePage()

    def teardown(self):
        self.driver.quit()

    def test_web1(self):
        self.driver.get('https://www.baidu.com')
        loc = ('xpath','//*[@type="submit"]')
        ele = self.driver.find_element(loc)
        print(f'ele:{ele}')
        print(f'ele_value:{ele.get_attribute("value")}')

if __name__ == '__main__':
    pytest.main(['test_usehadless1.py','-sq'])

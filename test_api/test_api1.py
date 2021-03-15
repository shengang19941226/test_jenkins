import pytest,allure
from common.run_method import Api
from common.log_main import logger

@allure.feature('接口类')
class TestApi:

    def setup(self):
        self.api = Api()
        self.req = {
            "method": "get",
            "url": "data/stocklevel.json",
            "headers": None,
            "json": None,
            "data": None,
            "encoding": "base64"
           }

    @allure.story('用例1')
    def test_api1(self):
        res = self.api.send(self.req).json()
        pytest.assume(res['highStock_moreThan'] == 6)
        logger.info('test_api1')

    @allure.story('用例2')
    def test_api2(self):
        res = self.api.send(self.req).json()
        pytest.assume(res['highStock_moreThan'] == 6)
        logger.info('test_api2')

    @allure.story('用例3')
    def test_api3(self):
        res = self.api.send(self.req).json()
        pytest.assume(res['highStock_moreThan'] == 7)
        logger.info('test_api3')


if __name__ == '__main__':
    pytest.main(['test_api1.py','-sq','-n','3'])


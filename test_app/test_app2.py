import pytest
from common.log_main import logger
from common.app import App
class TestApp:

    def setup(self):
        self.app = App().start(udid='127.0.0.1:62025',port=4725)

    def teardown(self):
        self.app.stop()

    def test_app3(self):
        logger.info('test_app3')

    def test_app4(self):
        logger.info('test_app4')

if __name__ == '__main__':
    pytest.main(['test_app2.py','-sq',])
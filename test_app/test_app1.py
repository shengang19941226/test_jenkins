import pytest
from common.log_main import logger
from common.app import App
class TestApp:

    def setup(self):
        self.app = App().start()

    def teardown(self):
        self.app.stop()

    def test_app1(self):
        logger.info('test_app1')

    def test_app2(self):
        logger.info('test_app2')

if __name__ == '__main__':
    pytest.main(['test_app1.py','-sq',])
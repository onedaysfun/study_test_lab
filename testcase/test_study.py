import time
from loguru import logger
from testcase.common_tools import request_tools
import pytest


class TestCase:
    @classmethod
    def setup_class(cls):
        pass

    def test_01(self):
        url = "https://baike.baidu.com/api/wikihome/homecmsdata"
        method = "get"
        cookies = {}
        resp = request_tools.HttpClient().set_url(url).set_method(method).send_http()
        assert resp.status_code == 200





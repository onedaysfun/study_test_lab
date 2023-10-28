import json
import requests
from loguru import logger
need_req_log = True
need_resp_log = True
need_add_log_in_file = False
# add log in file
if need_add_log_in_file:
    logger.add("logfile/test.log", encoding="utf-8", rotation="500MB",
               enqueue=True, retention="7 days")


class HttpClient:

    def __init__(self):
        self.method: str = "get"
        self.headers: dict = {}
        self.time_out: int = 60
        self.url: str = "None"
        self.data: dict = {}
        self.params: dict = {}
        self.cookies: dict = {}

    def send_http(self):
        method = self.method
        url = self.url
        time_out = self.time_out
        headers = self.headers
        cookies = self.cookies
        data = self.data
        params = self.params
        _req = requests.request(
            method=method,
            headers=headers,
            url=url,
            timeout=time_out,
            cookies=cookies,
            data=data,
            params=params
        )
        if need_req_log:
            json_cookies = {}
            json_headers = {}
            json_params = {}
            if cookies:
                json_cookies = json.dumps(cookies, sort_keys=True, indent=4).__str__()
            if headers:
                json_headers = json.dumps(headers, sort_keys=True, indent=4).__str__()
            if params:
                json_params = json.dumps(params, sort_keys=True, indent=4).__str__()
            _log_req_body = f"<HttpRequest>: [{method.upper()}] {url}\ntime_put:{time_out}\nheaders:{json_headers}\ncookies:{json_cookies}\nparams:{json_params}\n"
            logger.info(_log_req_body)
        if need_resp_log:
            try:
                req_json = _req.json()
                json_body = json.dumps(req_json, sort_keys=True, indent=4).__str__()
                _log_resp_body = f"<HttpResponse> [{method.upper()}] {url}\nstatus_code:{_req.status_code}\ncontent:{json_body}\n"
                logger.info(_log_resp_body)
            except Exception as e:
                logger.warning(e)
        return _req

    def set_method(self, method: str, **kwargs):
        """
        :param method:
        :param kwargs:
        :return:
        """
        kw = "method"
        if method:
            self.method = method
        elif kwargs[kw]:
            self.method = kwargs[kw]
        return self

    def set_url(self, url: str, **kwargs):
        """
        :param url:
        :param kwargs:
        :return:
        """
        kw = "url"
        if url:
            self.url = url
        elif kwargs[kw]:
            self.url = kwargs[kw]
        return self

    def set_cookies(self, cookies: dict, **kwargs):
        """
        :param cookies:
        :param kwargs:
        :return:
        """
        kw = "cookies"
        if cookies:
            self.cookies = cookies
        elif kwargs[kw]:
            self.cookies = kwargs[kw]
        return self

    def set_headers(self, headers: dict, **kwargs):
        """
        :param headers:
        :param kwargs:
        :return:
        """
        kw = "headers"
        if headers:
            self.headers = headers
        elif kwargs[kw]:
            self.headers = kwargs[kw]

    def set_data(self, data: dict, **kwargs):
        """
        :param data:
        :param kwargs:
        :return:
        """
        kw = "data"
        if data:
            self.data = data
        elif kwargs[kw]:
            self.data = kwargs[kw]

    def set_params(self, params: dict, **kwargs):
        """
        :param params:
        :param kwargs:
        :return:
        """
        kw = "params"
        if params:
            self.params = params
        elif kwargs[kw]:
            self.params = kwargs[kw]


if __name__ == '__main__':
    url = "https://baike.baidu.com/api/wikihome/homecmsdata"
    method = "get"
    cookies = {}
    resp = HttpClient().set_url(url).set_method(method).send_http()

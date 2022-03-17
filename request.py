import urllib.parse

from utils import log


class Request():
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.query = {}
        self.body = ''
        self.headers = {}
        self.cookies = {}

    def add_cookies(self):
        cookies = self.headers.get('Cookie', '')
        kvs = cookies.split('; ')
        for kv in kvs:
            if '=' in kv:
                k, v = kv.split('=')
                self.cookies[k] = v

    def add_headers(self, header):
        self.headers = {}
        lines = header
        for line in lines:
            k, v = line.split(': ', 1)
            self.headers[k] = v
        self.cookies = {}
        self.add_cookies()


    def form(self):
        body = urllib.parse.parse_qs(self.body)
        f = {}
        for k, v in body.items():
            f[k] = ''.join(v)
        return f

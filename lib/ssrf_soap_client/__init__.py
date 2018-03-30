#!/usr/bin/python3
import pyphp
from requests.utils import quote

class SsrfSoapClient(pyphp.PhpFunc):
    def config(self):
        self.name = 'ssrf_soap_client'
        self.source = 'ssrf_soap_client/call.php'

    def run(self, target, data, headers=None, user_agent=None):
        if not headers:
            headers = ''
        if not user_agent:
            user_agent = 'SsrfSoapClient'
        return pyphp.php(self.source,
                   target, headers_format(headers),
                    data_format(data), user_agent)


def headers_format(d):
    if isinstance(d, str): return d
    elif isinstance(d, dict):
        new_d = []
        for k, v in d.items():
            new_d.append(k + ': ' + v)
        d = new_d
    return "\r\n".join(d)

def data_format(d):
    if isinstance(d, str): return d
    elif isinstance(d, dict):
        new_d = []
        for k, v in d.items():
            new_d.append(quote(k) + '=' + quote(v))
        d = new_d
    return "&".join(d)

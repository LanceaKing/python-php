#!/usr/bin/python3
from lib import ssrf_soap_client

def main():
    s = ssrf_soap_client.SsrfSoapClient()
    print(s.run('http://127.0.0.1/', {'key1': 'value%/', 'sawq111#': 'asdw)('}))

if __name__ == '__main__':
    main()

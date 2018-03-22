#!/usr/bin/python3
import subprocess
import json
import base64

def php(*args):
    args = ['php'] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = p.stderr.read()
    if err: raise PhpException(err)
    return p.stdout.read()

def libfunc(func, **kwargs):
    params_encode = base64.b64encode(json.dumps(kwargs).encode('utf-8'))
    ret = php('direct.php', func, params_encode)
    return json.loads(base64.b64decode(ret))

class PhpException(Exception):

    def __init__(self, err_msg):
        self.msg = err_msg.decode('utf-8')
        Exception.__init__(self, '\n' + self.msg)

    def getMessage(self):
        return self.msg

def main():
    print(libfunc('ssrf_soap_client', target='127.0.0.1', headers=['Cookies: key=value'], data='a=b&c=d'))

if __name__ == '__main__':
    main()

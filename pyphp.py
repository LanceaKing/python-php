from abc import ABC, abstractmethod
import subprocess

def php(*args):
    args = ['php'] + list(args)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    err = p.stderr.read()
    if err: raise PhpException(err)
    return p.stdout.read()

class PhpFunc(ABC):
    name = None
    __source = None

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, filepath):
        self.__source = 'lib/' + filepath

    def __init__(self):
        self.config()

    @abstractmethod
    def config(self):
        pass

    @abstractmethod
    def run(self):
        pass

class PhpException(Exception):

    def __init__(self, err_msg):
        self.msg = err_msg.decode('utf-8')
        Exception.__init__(self, '\n' + self.msg)

    def getMessage(self):
        return self.msg

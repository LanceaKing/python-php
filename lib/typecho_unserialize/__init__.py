#!/usr/bin/python3
import pyphp

class TypechoUns(pyphp.PhpFunc):
    def config(self):
        self.name = 'typecho_unserialize'
        self.source = 'typecho_unserialize/call.php'

    def run(self, php_cmd):
        return pyphp.php(self.source, php_cmd)

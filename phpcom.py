#!/usr/bin/python3

import socket
import json
import os

class PhpCom(socket.socket):
    def __init__(self, port=31337):
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.__port = int(port)
        self.start()

    def __del__(self):
        self.close()

    def start(self):
        self.bind(('localhost', self.__port))
        self.listen(1)

    def restart(self):
        self.close()
        self.start()

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = int(port)
        self.restart()

    def query(self, func, *args):
        os.system('php director.php %d >> error.log 2>&1 &' % self.__port)
        conn, _ = self.accept()
        with conn:
            conn.recv(3)
            send_data = json.dumps({'func': func, 'args': args})
            conn.sendall(send_data.encode('utf-8'))
            recv_data = conn.recv(1024)
            conn.sendall(b'THX')
        rels = json.loads(recv_data)
        if rels['status']:
            return rels['ret_data']
        else:
            raise PhpComException(rels['ret_data'])

class PhpComException(Exception):
    def __init__(self, err_msg):
        Exception.__init__(self, 'PHP: ' + err_msg)
        self.msg = err_msg

def main():
    pc = PhpCom()
    rel = pc.query('test')
    print(rel)

if __name__ == '__main__':
    main()

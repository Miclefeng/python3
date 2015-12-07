#!/usr/bin/env python
#coding:utf-8

import sys, os, re
import logging
import socket
import urllib.parse as parse
from tornado import iostream, ioloop
from tornado.httpserver import HTTPServer
from tornado import httputil
import base64

PROXY_HOST = "127.0.0.1"
PROXY_PORT = 80
PROXY_USER = "lk"
PROXY_PWD = "2002"

BASE64_USER_PWD = b'Basic' + base64.b64encode(b"lk2002")

logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%d/%b/%Y %H:%M:%S]')

class LocalProxyHandler(object):
    def __init__(self, request):
        self.request = request
        self.connect_remote()
        
    def connect_remote(self):
        scheme, netloc, path, params, query, fragment = parse.urlparse(self.request.uri, 'http')
        try:
            self.remote_host, _, self.remote_port = netloc.rpartition(':')
            self.remote_port = int(self.remote_port)
        except ValueError:
            self.remote_host = netloc
            self.remote_port = 80
        self.remote_path = parse.urlunparse((scheme, self.remote_host + ('' if self.remote_host == 80 else ':%d' % self.remote_port), path, params, query, ''))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.remote_stream = iostream.IOStream(sock)
        #self.remote_stream.connect((self.remote_host, self.remote_port), self._on_connect_remote)
        self.remote_stream.connect((PROXY_HOST, PROXY_PORT), self._on_connect_remote)
        
    def _on_connect_remote(self):
        logging.info('remote addrest (%r, %r) connected.', self.remote_host, self.remote_port)
        data ='%s %s %s\r\n' % (self.request.method, self.remote_path, self.request.version)
        self.request.headers['Proxy-authorization'] = BASE64_USER_PWD
        self.request.headers['Connection'] = 'close'
        self.request.headers['Proxy-Connection'] = 'close'
        data += ''.join('%s: %s\r\n' % (k, v) for k,v in self.request.headers.get_all())
        data += '\r\n'
        if self.request.body:
            data += self.request.body
        self.remote_stream.write(data, self._on_write_remote)
        
    def _on_write_remote(self):
        logging.info('remote addrest (%r, %r) send data end.', self.remote_host, self.remote_port)
        self.remote_stream.read_until('\r\n\r\n', self._on_read_remote_headers)
        
    def _on_read_remote_headers(self, data):
        logging.info('remote addrest (%r, %r) read headers data end.', self.remote_host, self.remote_port)
        eol = data.find('\r\n')
        self.remote_headers = httputil.HTTPHeaders.parse(data[eol:])
        self.request.connection.write(data, self._on_write_local_headers)
        
    def _on_write_local_headers(self):
        logging.info('remote headers, %s', self.remote_headers)
        logging.info('remote addrest (%r, %r) read remote header data end.', self.remote_host, self.remote_port)
        if self.remote_headers.get('connection') == 'close':
            self.remote_stream.read_until_close(self._on_read_remote_body)
        elif 'content-length' in self.remote_headers:
            self.remote_stream.read_bytes(int(self.remote_headers['content-length']), self._on_read_remote_body)
        else:
            self.remote_stream.read_until_close(self._on_read_remote_body)
            
    def _on_read_remote_body(self, data):
        logging.info('remote addrest (%r, %r) read data end.', self.remote_host, self.remote_port)
        self.request.write(data)
        self.request.finish()

def main():
    http_server = HTTPServer(LocalProxyHandler)
    http_server.listen(8080)
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
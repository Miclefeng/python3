#! /usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
# import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello World!")
appliction = tornado.web.Application([(r"/",MainHandler),])
# def handle_request(request):
# 	message = "Hello World from Tornado Http Server"
# 	request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (len(message),message))
# 	request.finish
if __name__ == "__main__":
	appliction.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
	# http_server = tornado.httpserver.HTTPServer(handle_request)
	# http_server.listen(8888)
	# tornado.ioloop.IOLoop.instance().start()
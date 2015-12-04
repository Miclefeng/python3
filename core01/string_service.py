#! /usr/bin/env python
import textwrap
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define,options

define("port",default=8080,help="run on the given port",type=int)

class ReverseHandler(tornado.web.RequestHandler):
	def get(self,input):
		# reverse string
		headers = self.request.headers
		for k,v in headers.items():
			self.write(k+" => "+v+"\n")
		self.write(input+"\n")


class WrapHandler(tornado.web.RequestHandler):
	def post(self):
		text = self.get_argument('text')
		width = self.get_argument('width',40)
		self.write(textwrap.fill(text,int(width))+"\n")
if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application([(r"/reverse/(\w+)",ReverseHandler),(r"/wrap",WrapHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define,options
define("port",default=8000,help="run on given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
	
	def get(self,input):
		self.write(input+"\n")
	def post(self):
		req = self.request.arguments
		self.write(req)
		

if __name__ == "__main__":
	tornado.options.parse_command_line()
	
	app = tornado.web.Application([(r"/",IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
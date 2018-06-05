import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello World!")
appliction = tornado.web.Application([(r"/",MainHandler),])

if __name__ == "__main__":
	appliction.listen(8080)
	tornado.ioloop.IOLoop.instance().start()

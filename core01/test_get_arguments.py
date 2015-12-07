import textwrap  
import tornado.httpserver  
import tornado.ioloop  
import tornado.options  
import tornado.web  
  
from tornado.options import define, options  
define("port", default=8080, help="run on the given port", type=int)  
  
class ReverseHandler(tornado.web.RequestHandler):  
    def get(self, input):  
        self.write(input[::-1] + '\n')  
  
class WrapHandler(tornado.web.RequestHandler):  
    def post(self):  
        text = self.get_argument('text')  
        width = self.get_argument('width', 40)  
        self.write(textwrap.fill(text, int(width)) + '\n')  
          
class FindbrandHandler( tornado.web.RequestHandler ):  
    def get(self, input):  
        input_dcds = input.split('_')  
        input_dcd = u''  
        for elem in input_dcds:  
            if len(elem)>0:  
                input_dcd += unichr(int(elem))  
        print input_dcd.encode('utf-8') 
          
        o_str = 'input: '+input_dcd.encode('utf-8') + '\noutput: getcha\n'  
        self.write(o_str)  
  
if __name__ == "__main__":  
    tornado.options.parse_command_line()  
    app = tornado.web.Application(  
        handlers=[  
            (r"/reverse/(\w+)", ReverseHandler),  
            (r"/wrap", WrapHandler),  
            (r"/brand/(\w+)", FindbrandHandler)  
        ]  
    )  
    http_server = tornado.httpserver.HTTPServer(app)  
    http_server.listen(options.port)  
    tornado.ioloop.IOLoop.instance().start()  
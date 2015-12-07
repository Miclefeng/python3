import tornado.httpclient
import tornado.web
import tornado.ioloop
import tornado.httpserver

# tornado作为web客户端,就收返回的数据l
def Myclient():
	http_client = tornado.httpclient.HTTPClient()
	try:
		response = http_client.fetch("http://www.baidu.com")
		print(response.body)
	except tornado.httpclient.HTTPError as e:
		print("Error: "+str(e))
	except Exception as e:
		print("Error: "+str(e))
	http_client.close()

if __name__ == "__main__":
	Myclient()
	tornado.ioloop.IOLoop.instance().start()

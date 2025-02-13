
from tornado import autoreload
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
ioloop = IOLoop.instance()
autoreload.start(ioloop)
ioloop.start()
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import admin
import db
import os

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        entries = db.getRecentPosts()
        print 'here'
        self.render("home.html")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'templates')
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

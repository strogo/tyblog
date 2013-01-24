import tornado.web
import db
import markdown

class NewPostHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument('title')
        catagory = self.get_argument('catagory')
        tag = self.get_argument('tag')
        markdown = self.get_argument('markdown')
        html = markdown2.markdown(markdown)
        entry = db.Entry()
        entry.title = title
        entry.html = html
        entry.markdown = markdown
        entry.catagory = catagory
        entry.tag = tag
        try:
            db.NewPost(entry)
            self.write("ok")
        except:
            self.write("oh on")


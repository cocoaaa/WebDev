import os
import webapp2
import jinja2
from google.appengine.ext import db

#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class MyDB(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
    def write(self,*a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params ):
        t= jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **params):
        self.response.out.write(self.render_str(template, **params))
        
    def write_front(self, title="", art="", error_title="", error_art=""):
        pass
class MainPage(Handler):
    def get(self):
        pass
        
    def post(self):
        pass

class AnotherHandler(Handler):
    def get(self):
	pass

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/another', AnotherHandler)],
                             debug=True)
    
    

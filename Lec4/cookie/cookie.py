import os
import webapp2
import jinja2
from google.appengine.ext import db

#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)



class Handler(webapp2.RequestHandler):
    def write(self,*a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params ):
        t= jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **params):
        self.response.out.write(self.render_str(template, **params))
        
class MainPage(Handler):
    def get(self):
        self.render("base.html", username="", password="", error="")
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        error=""
        if username and password:
            self.redirect('/welcome?username=%s'%username)
        else:
            error = "Both valid username and password are required."
            self.render("base.html", username=username, password=password, error=error)
            
            

class WelcomeHandler(Handler):
    def get(self):
        username = self.request.get("username")
        visits = self.request.cookies.get('visits', '0')
        visits = int(visits);
        assert(visits>=0)
        self.render("welcome.html", username=username, visits=visits)
        #Update the visits value
        visits += 1
        self.response.set_cookie('visits', str(visits))
        print "visits: ", visits-1
        
    
	   

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/welcome', WelcomeHandler)],
                             debug=True)
    
    

import os
import webapp2
import jinja2
from google.appengine.ext import db
#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def isValid_title(title):
        return (title and len(title)>0)

def isValid_art(art):
        return (art and len(art)>0)

class Art(db.Model):
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
        arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC")
        self.render("front.html", title=title, art=art, arts=arts, error_title=error_title, error_art=error_art )

class MainPage(Handler):
    
        
    def get(self):
        self.write_front()
        
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        if (isValid_title(title) and isValid_art(art)):
            #Store to the db
            a = Art(title = title, art = art)
            a.put()
            #Redirect to the front page
#            print "HI!"
#            print Art.get_by_id(6119881720201216).title
#            bird = db.GqlQuery("SELECT * FROM Art WHERE title='another one'")[0]
#            print bird.art
            self.redirect("/")
            
        else:
            error_title = ""
            error_art = ""

            if not isValid_title(title):
                #Rerender the form with error_title
                error_title = "Give your art a title!"
            if not isValid_art(art):
                #Rerender the form with error_art
                error_art = "Please submit your art!"
            self.write_front(title, art, error_title, error_art)
            
            
class SuccessHandler(Handler):
    def get(self):
        self.write("<h1>Thanks! Your art is submitted!</h1>")
        

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/success', SuccessHandler)],
                             debug=True)
    
    

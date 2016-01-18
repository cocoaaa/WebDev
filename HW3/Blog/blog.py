import os
import webapp2
import jinja2
import cgi

import datetime
from google.appengine.ext import db

#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

def isValid(title, body):
    return (title and body and len(title)>0 and len(body)>0)

class Posts(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


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
        #show the 10 most recent posts
        posts = db.GqlQuery("SELECT * FROM Posts ORDER BY created DESC")[:10]
        self.render("main.html", posts=posts)
        
class NewPostHandler(Handler):
    def get(self):
        self.render("newpost.html", title="", body="", error="")
        
    def post(self):
        title = self.request.get("title")
        body = self.request.get("body")
        if isValid(title, body):
            #Store to the db
            p = Posts(title = title, body = body)
            p.put() #Created an entry to the db
            #Get the key of the object just created
            pid = p.key().id()
            #Redirect to the permalink
            newLink = cgi.escape("/view?pid="+str(pid),quote=True)
            print newLink
            self.redirect(newLink)
            
        else:
            #Rerender the form with the error message
            error = "Give your post both a title and a content!"
            self.render("newpost.html", title=title, body=body, error=error)
#            self.redirect('/')
            
class RedirectHandler(Handler):
    def get(self):
        print "redirecting"
        pid = self.request.get("pid")
        #Load pid's post
        p = Posts.get_by_id(int(pid))
        title = p.title
        body = p.body
        created = "Created at: " + p.created.strftime("%Y-%m-%d %H:%M")
        self.render("confirm.html", title=title, body=body, created=created)
        
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/newpost', NewPostHandler),
                              ('/view', RedirectHandler)],
                             debug=True)
    
#todo:
#    1. new post click -> open up new entry
#    2. submit -> show the blog just created
#    3. css styling
#    4. post on github


    

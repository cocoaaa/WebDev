import webapp2
import jinja2

#class Handler(webapp2.RequestHandler):
    
    
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World!!")
    def post(self):
        pass

app = webapp2.WSGIApplication([('/', MainPage)],
                             debug=True)

        
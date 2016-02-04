import os, json, urllib2, collections
import webapp2 #python webframe
import jinja2 #python template engine
import logging
import time
import tools
from google.appengine.ext import db
#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

#Global Variables
#requestIP = "76.119.233.230"
API_KEY = "AIzaSyC2oZC2Vd5lRnAgPQ_Svv2JTtkXVD6MR4w"
URL_BASE = "https://maps.googleapis.com/maps/api/staticmap?%(markers_str)s&size=%(width)sx%(height)s&key=%(key)s"
CACHE = {}

#Database
class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    location = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)

#def get_top10(update = False):
#    """Returns the result of top ten latest art object created in the datastore"""
#    key = 'top10'
#    if not update and key in CACHE:
#        return CACHE[key]
#    else: 
#        print "!!!!!!!!!"  #debug
#        logging.info("DB Query") #debug
#        arts = Art.gql("ORDER BY created DESC").fetch(10)
#        arts = list(arts)
#        CACHE[key] = arts
#        return arts

#wirte directly to the cache when updating a new art that is just submitted
def get_top10(update = False, newArt=None):
    """Returns the result of top ten latest art object created in the datastore"""
    key = 'top10'
    print "Length of cache: ", len(CACHE.get(key,[]))
    if not update and key in CACHE:
        logging.info("Cache hit")
        return CACHE[key]
    elif key in CACHE: #CACHE needs to be updated
        assert (update and newArt is not None)
        #Remove the oldest
        arts_queue = CACHE[key]
        arts_queue.pop()
        arts_queue.appendleft(newArt)
        
        #Update the cache
        CACHE[key] = arts_queue
        logging.info("Cache updated without entire DB read!")
        return arts_queue
    else: 
        logging.info("Entire DB read. argh") #debug
        arts_queue = collections.deque()
        arts = list(Art.gql("ORDER BY created DESC").fetch(10))
        arts_queue.extend(arts)
        CACHE[key] = arts_queue
        return arts_queue
    
    
class Handler(webapp2.RequestHandler):
    def write(self,*a, **kw):
        self.response.out.write(*a, **kw)
    
    def render_str(self, template, **params ):
        t= jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **params):
        self.response.out.write(self.render_str(template, **params))
        
    def write_front(self, title="", art="", error_title="", error_art=""):
        arts = get_top10()
        print 'number of arts on the front: ', len(arts)
        for a in arts:
            print a.location
        mapURL = None
        if arts:
            locations = filter(None, [a.location for a in arts])
            print locations
            if locations:
                mapURL = tools.getMapURL(locations, API_KEY, URL_BASE)
                logging.info("locations: %s", str(locations))
                print "location url: ", locations
#        if arts: #debug
            print 'total arts submitted: ', len(arts)
            print 'latest submitted: ', arts[0].title
            print 'location: ', arts[0].location
        self.render("front.html", title=title, art=art, error_title=error_title, error_art=error_art, arts=arts,mapURL=mapURL)
    
class MainPage(Handler):
    
    def get(self):
        self.write_front()
        
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
#        requestIP= self.request.remote_addr
        requestIP = tools.getRandomIP() #string type
        logging.info("This is the logging info test")
        logging.info("Printing the request's ip...")
        logging.info("ip: %s", requestIP)
#        print "HEREERERERERERERERER IS THE IP"
#        print requestIP
        if (tools.isValid_title(title) and tools.isValid_art(art)):
            #Get the location of the one who just submitted the artwork
            location = tools.getLocation(requestIP) #string or None
            print "location of the new art: ", location
            
            #Store to the db
            art = Art(title = title, art = art, location=location)
            art.put()
            #clear the cache to prevent the stale cache problem
#            CACHE.clear() #deletes everything in the dictionary  or CACHE['top'] = None
            #To handle cache stampede by multiple concurrent user requests
            print "new art put into database"
#            print "waiting for the update to be valid"
#            time.sleep(1)
            get_top10(update=True, newArt = art)
#            print "Updated the cache based on the new database"
            self.redirect("/success")
            return 
        else:
            error_title = ""
            error_art = ""

            if not tools.isValid_title(title):
                #Rerender the form with error_title
                error_title = "Give your art a title!"
            if not tools.isValid_art(art):
                #Rerender the form with error_art
                error_art = "Please submit your art!"
            self.write_front(title, art, error_title, error_art)
            return
            
            
class SuccessHandler(Handler):
    def get(self):
        self.render('success.html')
        

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/success', SuccessHandler)],
                             debug=True)
    
    

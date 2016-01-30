import os, json, urllib2
import webapp2 #python webframe
import jinja2 #python template engine
import logging
import time
from google.appengine.ext import db
#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def isValid_title(title):
        return (title and len(title)>0)

def isValid_art(art):
        return (art and len(art)>0)
    
def getLocation(requestObj):
    request = urllib2.Request("http://ip-api.com/json")
    response = urllib2.urlopen(request)
    resp_str = response.read()
    resp_json = json.loads(resp_str)
    lat = str(resp_json['lat'])
    lon = str(resp_json['lon'])
    location = lat+","+lon
    return location #str
    
def getMapURL(location, zoom=13, key ="AIzaSyC2oZC2Vd5lRnAgPQ_Svv2JTtkXVD6MR4w"):
    location=str(location); zoom = str(zoom);
    url_base ="https://maps.googleapis.com/maps/api/staticmap?center=%(location)s&size=512x512&zoom=%(zoom)s&key=%(key)s"%{"zoom":zoom, "location": location, "key":key}
    return url_base #str

class Art(db.Model):
    title = db.StringProperty(required=True)
    art = db.TextProperty(required=True)
    mapURL = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)
class Artist(db.Model):
    location = db.StringProperty(required=True)
    mapURL = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    
CACHE = {}
def get_top10(update = False):
    """Returns the result of top ten latest art object created in the datastore"""
    key = 'top10'
    if not update and key in CACHE:
        return CACHE[key]
    else: 
        print "!!!!!!!!!"  #debug
        logging.error("DB Query") #debug
        arts = Art.gql("ORDER BY created DESC").fetch(10)
        arts = list(arts)
        CACHE[key] = arts
        return arts
    
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
#        if arts: #debug
#            print 'total arts submitted: ', len(arts)
#            print 'latest submitted: ', arts[0].title
#            print 'mapURL: ', arts[0].mapURL
        self.render("front.html", title=title, art=art, error_title=error_title,
                                    error_art=error_art, arts=arts,)

class MainPage(Handler):
    def getLocation(self, requestObj):
        request = urllib2.Request("http://ip-api.com/json")
        response = urllib2.urlopen(request)
        resp_str = response.read()
        resp_json = json.loads(resp_str)
        location = None
        lat = str(resp_json.get('lat', None))
        lon = str(resp_json.get('lon',None))
        if lat and lon:
            location = lat+","+lon
        return location #str or None
    
    def get(self):
        self.write_front()
        
    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")
        
        if (isValid_title(title) and isValid_art(art)):
            #Get the location of the one who just submitted the artwork
            location = self.getLocation(self.request)
            mapURL = None
            if location:
                mapURL = getMapURL(location=location)
            #Store to the db
            art = Art(title = title, art = art)
            if mapURL:
                art.mapURL = mapURL
            art.put()
            #clear the cache to prevent the stale cache problem
#            CACHE.clear() #deletes everything in the dictionary  or CACHE['top'] = None
            #To handle cache stampede by multiple concurrent user requests
            print "new art put into database"
            print "waiting for the update to be valid"
            time.sleep(1)
            get_top10(update=True)
            print "Updated the cache based on the new database"
            self.redirect("/success")
            return 
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
            return
            
            
class SuccessHandler(Handler):
    def get(self):
        self.render('success.html')
        

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/success', SuccessHandler)],
                             debug=True)
    
    

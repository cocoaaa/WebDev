import urllib2,json
import random

def isValid_title(title):
        return (title and len(title)>0)

def isValid_art(art):
        return (art and len(art)>0)
    

def getRandomIP():
    ip = ".".join(map(lambda x: str(x), [random.randint(0,255) for i in xrange(4)]))
    return ip
    
def getLocation(requestIP):
    request = urllib2.Request("http://freegeoip.net/json/" + str(requestIP))
    response = urllib2.urlopen(request)
    resp_str = response.read()
    resp_json = json.loads(resp_str)
    location = None
    lat = str(resp_json.get('latitude', '0'))
    lon = str(resp_json.get('longitude', '0'))
    if eval(lat) ==0 and eval(lon) ==0:
        return None
    else:
        location = lat+","+lon
    return location #str or None    

def getMarkers(locations):
    """input: a list of strings in form of 'lat,lon'
    output: a string of "markers=...&markers=:..." to be used 
    in a request to Google Static Map API
    """
    if len(locations) <=0:
        return #todo
    base = "markers="
    for location in locations:
        base += "%s"%location + "%7C"
    return base[:-3]

API_KEY = "AIzaSyC2oZC2Vd5lRnAgPQ_Svv2JTtkXVD6MR4w"
URL_BASE = "https://maps.googleapis.com/maps/api/staticmap?%(markers_str)s&size=%(width)sx%(height)s&key=%(key)s"
def getMapURL(locations, key= API_KEY, url_base = URL_BASE, width="400", height="400"):
    if len(locations) <= 0:
        return None
    markers_str = getMarkers(locations)
    fullURL = URL_BASE%{'markers_str': markers_str,
                       'width': width,
                        'height': height,
                       'key':API_KEY}
    
    return fullURL
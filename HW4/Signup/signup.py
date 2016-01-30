import os,re, string, random, hashlib
import webapp2
import jinja2
from google.appengine.ext import db

#Templates directory: relative to the directory this current python file is in.
template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class User(db.Model):
    username = db.StringProperty(required=True)
    password = db.StringProperty(required=True)
    email = db.StringProperty()
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

class SignupHandler(Handler):
    def give_form(self, username="", password="", email="", 
                        error_u_empty="", error_u_duplicate="",
                        error_p_empty="", error_p_notmatch="", error_email=""):

        self.render("signup.html", 
                   username=username, password=password, email=email, 
                   error_u_empty=error_u_empty, error_u_duplicate=error_u_duplicate,
                   error_p_empty=error_p_empty,
                   error_p_notmatch=error_p_notmatch,
                   error_email=error_email)
        
    def get(self):        
        #response's header to set cookie
        self.response.delete_cookie('username')

        #response's body
        self.give_form();
        return
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        error_u_empty = ""
        error_u_duplicate = ""
        error_p_empty=""
        error_p_notmatch=""
        error_email = ""
        

        if (not username) or len(username)>20:
            error_u_empty="Please choose a valid username."
            self.give_form(error_u_empty=error_u_empty)
            return
        if username:
            isTaken = User.gql("WHERE username='%s'"%username).get()
            if isTaken:
                error_u_duplicate = "Sorry this username is already taken. Try a different one."
                #debug
                print "!!!!!!", error_u_duplicate
                print "created at: ", isTaken.created
                self.give_form( error_u_duplicate=error_u_duplicate)
                return
        if not password:
            error_p_empty="Please choose a password."
            self.give_form(username=username, password=password, error_p_empty=error_p_empty)
            return
        if password != verify:
            error_p_notmatch = "Password not matched!"
            self.give_form(username=username, password=password,                
                            error_p_notmatch=error_p_notmatch)
            return
        if email and not valid_email(email):
            error_email = "Invalid email address!"
            self.give_form(username=username, password=password, email=email, 
                            error_email=error_email)
            return
        #All input data valid
        #Update the database
        hashed_pw = encrypt(username, password)
        user = User(username=username, password=hashed_pw, email=email )
        user.put()
        print 'New userdata created'
        self.response.headers['Content-Type']='text/plain'
        self.response.set_cookie('username', str(username))
        self.redirect("/welcome")
        return
    

class WelcomeHandler(Handler):
    def get(self):
        username = self.request.cookies.get("username")
        if username:
            self.response.write("Welcome, %s!"%username)
            return
        self.error(400) #no cookie named username is set
    
class LoginHandler(Handler):
    def get(self):
        self.render("login.html", username="", password="", error="")
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        error = ""
        print "name: ",  username
        print "pw: ", password
        print "pw_db: ", User.gql("WHERE username='%s'"%username).get().password
        
        #Validate the inputs
        if not valid_login(username, password):
            error = "Username and password don't match!"
            self.render("login.html", username=username, password="", error=error)
            return
        #valid login username, password
        #set cookie to this (validated) username
        print "yay!!! valid login!!!"
        print "username: ", username
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.set_cookie('username', str(username))
        self.redirect("/welcome")
        
class LogoutHandler(Handler):
    def get(self);
        
        #clear up the cookie
        
        #redirect to the signup page 
        self.redirect('/signup')
def valid_email(email):
    pattern = r'(.+)@(.+).(.+)'
    return re.match(pattern, email)

def make_salt():
    return "".join([random.choice(string.letters) for i in xrange(5)])
def make_pw_str(username, password, salt):
    raw_str = str(username) + str(password) + str(salt)
    pw_str = hashlib.sha256(raw_str).hexdigest() + "|" + str(salt)
    return pw_str

def encrypt(username, password):
    salt = make_salt()
    pw_str = make_pw_str(username, password, salt)
    print "salt: ", salt
    print "before: ", username+password+salt
    print "hashed: ", pw_str
    return pw_str
    
def valid_login(username, password):
    username = str(username)
    password = str(password)
    password_db = User.gql("WHERE username='%s'"%username).get().password
    _,salt = password_db.split('|')
    return password_db == make_pw_str(username, password, salt)
        
    
app = webapp2.WSGIApplication([('/signup', SignupHandler),
                               ('/welcome', WelcomeHandler),
                               ('/login', LoginHandler),
                              ],
                             debug=True)
    
    

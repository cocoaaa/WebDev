import webapp2
import re
from cgi import escape
import string

form="""
<form name="signup" method="post">
    <b>Welcome! Please sign up below: </b>
   <br>
   <br>
    <label>
        Username:
        <input type="text" name="username" value="%(username)s">
        <div style="color: red">%(username_error)s</div>
    </label>
    <br>
    <label>
        Password:
        <input type="password" name="password">    
        <div style="color: red">%(password_error)s</div>
    </label>
    <br>
    <label>
        Verify:
        <input type="password" name="verify">
        <div style="color: red">%(verify_error)s</div>
    </label>
    <br>
    <label>
        Email (optional):
        <input type="text" name="email"> 
        <div style="color: red">%(email_error)s</div>
    </label>
    <br>
    <input type="submit">

</form>
"""

welcome="""
<html>
<body>
Welcome <span style="color: blue">%(username)s</span>!!
</body>
</html>
"""
name_pattern = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
pw_pattern = re.compile(r"^.{3,20}$")
email_pattern = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(u_username):
    """
    Input: raw user input into Username field
    Output: u_username if valid, None otherwise
    A username is valid if
        1. 3-20 characters long
        2. uses a-z,A-z,_,-
    """
    res = name_pattern.match(u_username)
    if res is None: #no match, i.e. invalid
        return None
    else: 
        return res.group()
    
def valid_password(u_password):
    """
    Input: raw user input to Password field
    Output: u_password if valid, None otherwise
    A password is valid if it consists of any 3-20 symbols
    """
    res = pw_pattern.match(u_password)
    if res is None:
        return None
    else:
        assert(res.group() == u_password)
        return u_password

def valid_verify(u_verify, u_password):
    """
    Input: raw user input to Verify filed
    Output: u_verify if u_password is valid and it is the same as u_password
    """
    if not(u_verify and u_password):
        return None
        
    if len(u_verify) != len(u_password):
        return None
                
    valid_pw = valid_password(u_password)
    valid_verify = valid_password(u_verify)
    
    if not(valid_pw and valid_verify):
        return None
    elif (valid_pw != valid_verify):
        return None
    else:
        assert(u_verify == valid_verify)
        return u_verify
        
def valid_email(u_email):   
    if u_email == "":
        return u_email
    res = email_pattern.match(u_email)
    if res is None:
        return None
    else:
        assert(u_email == res.group())
        return u_email

def escape_html(s):
    return escape(s, quote=True)
    
class MainPage(webapp2.RequestHandler):
    def write_form(self, 
                   username="",
                   username_error="",
                   password_error="",
                   verify_error="",
                   email_error=""):
                       
        self.response.out.write(form%{"username":escape_html(username),
                                      "username_error":username_error,
                                      "password_error":password_error,
                                      "verify_error":verify_error,
                                      "email_error":email_error})
    
    def get(self):
        self.write_form()
    
    def post(self):
        u_username = self.request.get("username")
        u_password = self.request.get("password")
        u_verify = self.request.get("verify")
        u_email = self.request.get("email")
        
        v_username = valid_username(u_username)
        v_password = valid_password(u_password)
        v_verify = valid_verify(u_verify, u_password)
        v_email = valid_email(u_email)
        
        #Validation success!
        if (v_username and v_password and v_verify):
            
            #redirect
            self.redirect("/welcome")
            
            
        #Validation fails!
        name=u_username
        u_error=""
        p_error=""
        v_error=""
        e_error=""
        if v_username is None:
            u_error = "This username is invalid"
        if v_password is None:
            p_error = "This password is invalid"
        if v_verify is None:
            v_error = "This is invalid or does not match the password"
        if v_email is None:
            e_error = "This email is invalid"
            
            
        self.write_form(username = name,
                        username_error = u_error,
                        password_error = p_error,
                        verify_error = v_error,
                        email_error = e_error)
            
            
            

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username") #todo: empty string is returned here
        self.response.out.write(welcome%{"username":username})


    
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/welcome', WelcomeHandler)
                               ],
                              debug=True)
    


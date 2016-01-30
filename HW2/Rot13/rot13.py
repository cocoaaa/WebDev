import webapp2
import cgi
import string
form = """
<form method="post">
    Welcome! Enter your sentence in the box below:
    <br>
    <br>
    <textarea name="input" rows="10" cols="50">%s</textarea>
    <br>
    <input type="submit">   
</form>
"""


def rotate13(c):
    """
    Input: raw user input (i.e. not escaped ) 
    Output: rotated character or symbols (number, quots, etc)
    """
    if c and c in string.ascii_letters:
        val = ord(c)
        if c in string.ascii_lowercase:
            offset = 97 #ord("a") = 97
        else:
            offset = 65 #ord("A") =65
            
        newVal = ((val-offset+13)%26)+offset
        c = chr(newVal)      
    return c
    
def escape_html(s):
    return cgi.escape(s, quote=True)


class MainPage(webapp2.RequestHandler):
    def write_form(self, user_string=""):
        self.response.out.write(form%user_string)
    
    def get(self):
        self.response.headers['Content-Type'] = 'html'
        self.write_form()
        
    def post(self):
        #rotate13
        user_string = self.request.get("input")
        rotated_string = ""
        for ele in user_string:
            rotated_string += rotate13(ele)
        #equiv
        #rotated_string = "".join(rotate13(ele) for ele in user_string)
    
        #escape
        rotated_string = escape_html(rotated_string)
        
        #update the form and respond 
        self.write_form(user_string=rotated_string)
    
app = webapp2.WSGIApplication([(r'/', MainPage)],
                              debug=True)

          
        
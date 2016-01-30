import webapp2

form="""
<form action="http://www.google.com/search">
    <input name="q">
    <input type="submit">    
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'html';
        self.response.out.write(form);
app = webapp2.WSGIApplication([('/', MainPage), ],
                              debug=True)
def escape_html(s):
    escapeDict = {'<': "&lt;",
                 '>': "&gt;",
                 '"': "&quot;",
                 "&": "&amp;"};
    newS = ""
    for c in s:
        if c in escapeDict:
            newS += escapeDict[c]
        else:
            newS += c
    return newS
            
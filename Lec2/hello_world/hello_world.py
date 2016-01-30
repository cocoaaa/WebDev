import webapp2
import cgi

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    
    <label>
        Year
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit">    
</form>
"""
def valid_month(month):
    """Returns None if month is not a valid month, otherwise return the name of the month 
        with the first letter capitalized.
    """
    months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 
            'September', 'October', 'November', 'December'];
    
    month_abbvs = dict( (m[:3].lower(),m) for m in months)
    if month:
        short_month = month[:3].lower();
        return month_abbvs.get(short_month);
        
def valid_day(day):
    """
    Input: string of a number for a day of a month
    Returns: the day as an Int if the day is a valid day, None otherwise
    """
#    if day.isdigit():
    if day and day.isdigit():
        day = int(day);
        if 1<= day and day <=31:
            return day;

    return None

def valid_year(year):
    """
    Input: User input as a string for the year of DOB
    Return: the year as a number if a valid year, None otherwise"""
    if year and year.isdigit():
        year = int(year)
        if 1900 <= year and year <= 2500:
            return year
    return None

def escape_html(s):
    return cgi.escape(s, quote=True);
    

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""): 
        self.response.out.write(form % {"error": escape_html(error), 
                                        "month": escape_html(month), 
                                        "day": escape_html(day), 
                                        "year": escape_html(year)})
    
    def get(self):
        self.write_form();
        
    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")
        
        month = valid_month(self.request.get("month"))
        day = valid_day(self.request.get("day"))
        year = valid_year(self.request.get("year"))
        
        if (month and day and year):
            #redirect to /thanks
            self.redirect("/thanks");
            
        else:
            self.write_form(error="Invalid birthday.",
                           month=user_month,
                           day=user_day,
                           year=user_year)
                           
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Valid birthday received, thanks!")

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', ThanksHandler)
                               ],
                              debug=True)

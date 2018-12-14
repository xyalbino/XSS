#import webapp2
import urllib2
from google.appengine.ext import webapp as webapp2


page_header = """
<!doctype html>
<html>
  <head>
    <!-- Internal game scripts/styles, mostly boring stuff -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'">
    <script src="static/game-frame.js"></script>
    <link rel="stylesheet" href='static/game-frame-styles.css' />
  </head>

  <body id="level1">
    <img src="static/logos/level1.png">
      <div>
"""

page_footer = """
    </div>
  </body>
</html>
"""

main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""


class MainPage(webapp2.RequestHandler):

    def render_string(self, s):
        self.response.out.write(s)

    def get(self):
        # Disable the reflected XSS filter for demonstration purposes
        #self.response.headers.add_header("X-XSS-Protection", "0")

        if not self.request.get('query'):
            # Show main search page
            self.render_string(page_header + main_page_markup + page_footer)
        else:
            query = self.request.get('query', '[empty]')
            query = urllib2.quote(query, safe='~@#$&()*!+=:;,.?/\'') # use urllib2.quote(), the same as encodeURI() in js
            #print query

            # Our search engine broke, we found no results :-(
            message = "Sorry, no results were found for <b>" + query + "</b>."
            message += " <a href='?'>Try again</a>."

            # Display the results page
            self.render_string(page_header + message + page_footer)

        return


app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)


'''def main():
    from paste import httpserver
    from paste.cascade import Cascade
    from paste.urlparser import StaticURLParser
    static_app = StaticURLParser("")

    # Create a cascade that looks for static files first, then tries the webapp
    app = Cascade([static_app, application])
    httpserver.serve(app, host='127.0.0.1', port='8080')


if __name__ == '__main__':
    main()'''

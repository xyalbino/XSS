import os
import base64
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def render_template(self, filename, context={}):
        path = os.path.join(os.path.dirname(__file__), filename)
        self.response.out.write(template.render(path, context))

    def gen_nonce(self):
        """ Generates a random string of bytes, base64 encoded """
        string = base64.b64encode(os.urandom(16), altchars=b'-_')
        b64len = 66
        return string[0:b64len].decode()

    def get(self):
        # Disable the reflected XSS filter for demonstration purposes
        self.response.headers.add_header("X-XSS-Protection", "0")


        # Route the request to the appropriate template
        if "signup" in self.request.path:

            self.render_template('signup.html',
                                 {'next': self.request.get('next')})
        elif "confirm" in self.request.path:
            self.render_template('confirm.html',
                                 {'next': self.request.get('next', 'welcome')})
        else:
            self.render_template('welcome.html', {})

        return




app = webapp.WSGIApplication([('/', MainPage), ], debug=False)
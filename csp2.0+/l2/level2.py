import webapp2
import os
import base64
from math import floor
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):

    def render_template(self, filename, context={}):
        path = os.path.join(os.path.dirname(__file__), filename)
        self.response.out.write(template.render(path, context))

    def get(self):
        nonce = self.gen_nonce()
        self.render_template('index2.html',{'nonce': nonce})
    def gen_nonce(self):
        """ Generates a random string of bytes, base64 encoded """
        string = base64.b64encode(os.urandom(16), altchars=b'-_')
        b64len = 66
        return string[0:b64len].decode()


app = webapp2.WSGIApplication([('.*', MainPage)], debug=False)

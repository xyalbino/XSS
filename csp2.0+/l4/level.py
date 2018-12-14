import webapp2
import os
import base64
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):

    def render_template(self, filename, context={}):
        path = os.path.join(os.path.dirname(__file__), filename)
        self.response.out.write(template.render(path, context))

    def get(self):
        # Disable the reflected XSS filter for demonstration purposes
        self.response.headers.add_header("X-XSS-Protection", "0")

        if not self.request.get('timer'):
            nonce = self.gen_nonce()
            # Show main timer page
            self.render_template('index.html',{'nonce': nonce})
        else:
            # Show the results page
            timer = self.request.get('timer', 0)
            nonce = self.gen_nonce()

            try:
                timer = float(timer)
            except ValueError:
                timer = float(3)
            self.render_template('timer.html', {'timer': timer,'nonce': nonce})

        return

    def gen_nonce(self):
        """ Generates a random string of bytes, base64 encoded """
        string = base64.b64encode(os.urandom(16), altchars=b'-_')
        b64len = 66
        return string[0:b64len].decode()


app = webapp2.WSGIApplication([('.*', MainPage), ], debug=False)
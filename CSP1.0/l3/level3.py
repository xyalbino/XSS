import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
class MainPage(webapp.RequestHandler):

    def render_template(self, filename, context={}):
        path = os.path.join(os.path.dirname(__file__), filename)
        self.response.out.write(template.render(path, context))

    def get(self):
        self.render_template('index.html')


app = webapp.WSGIApplication([('/', MainPage), ], debug=False)
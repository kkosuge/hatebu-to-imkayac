import urllib
import hashlib
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
  def post(self):
    username = self.request.get("username")
    url = "http://im.kayac.com/api/post/%s"# % user

    data = {}
    data["message"] = "hatena: " + username

    params = urllib.urlencode(data)
    post = urllib.urlopen(url, params)


app = webapp.WSGIApplication(
          [('/',MainPage)],
          debug=True)

def main():
  run_wsgi_app(app)

if __name__=="__main__":
  main()

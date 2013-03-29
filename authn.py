import webapp2
import os
from google.appengine.api import app_identity
from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write("Version %s\n\n" % os.environ['CURRENT_VERSION_ID'])
            self.response.out.write("User Org: %s\n" % os.getenv('USER_ORGANIZATION'))
            self.response.out.write("Nickname: %s\n" % user.nickname())
            self.response.out.write("Email:    %s\n" % user.email())
            self.response.out.write("User ID:  %s\n" % user.user_id())
        else:
            self.redirect(users.create_login_url(self.request.uri))
            


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
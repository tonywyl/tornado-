from tornado.web import RequestHandler


class LoginHandler(RequestHandler):
    def get(self,*args,**kwargs):

        name=self.get_secure_cookie('setcookie')
        self.render('login.html')

    def post(self,*args,**kwargs):
        user=self.get_argument('username')
        pwd=self.get_argument('password')
















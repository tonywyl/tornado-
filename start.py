import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options

from app01 import models

define('port',default=9000,help='run on the given port ',type=int)


user_orm=models.UserManagerORM()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title='user manager v0.1'
        users=user_orm.GetAllUser()
        self.render('template/UserManager.html',title=title,users=users)
    def post(self):
        pass

class AddUserHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        user_info={
            'user_name':self.get_argument('user_name'),
            'user_age':self.get_argument('user_age'),
            'user_sex':self.get_argument('user_sex'),
            'user_score':self.get_argument('user_score'),
            'user_subject':self.get_argument('user_subject')
        }
        user_orm.CreateNewUser(user_info)
        self.redirect('http://127.0.0.1:9000/')

class EditUserHandler(tornado.web.RequestHandler):
    def get(self):
        user_info=user_orm.GetUserByName(self.get_argument('user_name'))
        self.render('template/EditUserInfo.html',user_info=user_info)

    def post(self):
        pass

class UpdateUserInfoHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        user_orm.UpdateUserInfoByName({
            'user_name':self.get_argument('user_name'),
            'user_age':self.get_argument('user_age'),
            'user_sex':self.get_argument('user_sex'),
            'user_score':self.get_argument('user_score'),
            'user_subject':self.get_argument('user_subject')
        })

        self.redirect('http://127.0.0.1:9000')


class DeleteUserHandler(tornado.web.RequestHandler):
    def get(self):
        user_orm.DeleteUserByName(self.get_argument('user_name'))
        print(self.get_argument('user_name'),'===')
        self.redirect('http://127.0.0.1:9000')
    def post(self):
        pass



#路由
settings={
    'static_url_prefix':'/static',
    'static_path':'static',
    'xsrf_cookies':True,

}
def MainProcess():
    tornado.options.parse_command_line()
    application=tornado.web.Application([
        (r'/',MainHandler),
        (r'/AddUser',AddUserHandler),
        (r'/EditUser',EditUserHandler),
        (r'/DeleteUser',DeleteUserHandler),
        (r'/UpdateUserInfo',UpdateUserInfoHandler),
    ],**settings)
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    MainProcess()



















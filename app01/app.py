

import tornado.ioloop
import tornado.web
import tornado
from app01 import models
settings={
    'template_path':'template',
    'static_path':'static',
    'xsrf_cookies':True,
    'cookie_secret':'as',
    'static_url_prefix':'/static/',
    'ui_methods':'md'
    
}
def make_app():
    return tornado.web.Application([
        (r'/login.html',)
    ],**settings)

if __name__ == '__main__':
    app=make_app()
    app.listen(8880)
    tornado.ioloop.IOLoop.current().start()










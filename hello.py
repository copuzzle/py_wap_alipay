# -*- encoding: utf-8 -*-
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if 'Authorization' in self.request.headers:
            self.write("Hello, world!!<br/>%s" % self.request.headers['Authorization'])
        else:
            self.add_header('WWW-Authenticate', 'Basic realm="TCP ss"')
            self.set_status('401', 'Unauthorized')


class Alipay(tornado.web.RedirectHandler):
    from wap_alipay import submit
    pay_url = submit.get_pay_url('123456789', '给我一支烟钱', 1.01)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

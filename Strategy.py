# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Strategy
@time: 2018/6/4 9:15 PM
"""


class Customer:
    info = ""
    name = ""
    phone = ""
    mail = ""
    send_way = ""

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_mail(self, mail):
        self.mail = mail

    def get_mail(self):
        return self.mail

    def get_phone(self):
        return self.phone

    def set_info(self, info):
        self.info = info

    def get_info(self):
        return self.info

    def send_msg(self):
        self.send_way.send(self.info)


class MsgSender:
    dst_code = ""

    def set_code(self, code):
        self.dst_code = code

    def send(self):
        pass


class EmailSender(MsgSender):
    def send(self, info):
        print "Email_address:%s,Email:%s" % (self.dst_code, info)


class TextSender(MsgSender):
    def send(self, info):
        print "Text_number:%s,content:%s" % (self.dst_code, info)

"""
策略模式(Strategy)定义如下：定义一组算法，将每个算法都封装起来，并使他们之间可互换。
示例的实现是不是复杂了，为什么不实现一个sender类，下有若干send方法
"""
if __name__ == '__main__':
    customer_a = Customer()
    customer_a.set_name("123")
    customer_a.set_mail("123@bear2.cn")
    customer_a.set_phone("+86-123")
    customer_a.set_info("hello world")

    text_sender = TextSender()
    text_sender.set_code(customer_a.get_phone())
    text_sender.send(customer_a.get_info())

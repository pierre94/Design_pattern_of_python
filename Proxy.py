# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Proxy
@time: 27/05/2018 4:42 PM
"""


class Server():
    content = ""

    def recv(self, info):
        pass

    def send(self, info):
        pass

    def show(self):
        pass


class InfoServer(Server):
    def recv(self, info):
        self.content = info
        return "recv OK!"

    def show(self):
        print "SHOW:%s" % self.content


class ServerProxy():
    pass


class InfoServerProxy(ServerProxy):
    server = ""

    def __init__(self, server):
        self.server = server

    def recv(self, info):
        return self.server.recv(info)

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info type is not correct"
        addr = info.get("addr", 0)
        if not addr in self.white_list:
            return "your address is invalid"
        else:
            content = info.get("content", "")
            return self.server.recv(content)

    def addwhite(self, addr):
        self.white_list.append(addr)

    def rmWhite(self, addr):
        self.white_list.remove(addr)

    def cleanWhite(self):
        self.white_list = []


"""
代理模式，为其对象提供一个代理，以控制此对象的访问和控制。 
如本示例中，server是proxy的一个属性，proxy的info与server的info完全不同，proxy的server包含addr和server的内容，以达到对server的控制.
proxy在某种程度上会降低处理效率
"""
if __name__ == '__main__':
    info_struct = dict()
    info_struct["addr"] = 10010
    info_struct["content"] = "hello world!"
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print info_server_proxy.recv(info_struct)
    info_server_proxy.show()
    info_server_proxy.addwhite(10010)
    print info_server_proxy.recv(info_struct)
    info_server_proxy.show()

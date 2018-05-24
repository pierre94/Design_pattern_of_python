# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: single
@time: 22/05/2018 8:37 PM
"""
import threading
import time


# 通过__new__实现单实例模式
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class Bus(Singleton):
    lock = threading.Lock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print "sneding Singal Data...", data
        self.lock.release()


class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == "__main__":
    for i in range(3):
        print "Entity %d begin to run..." % i
        my_entity = VisitEntity()
        my_entity.setName("Entity_" + str(i))
        my_entity.start()
        # bus是单实例的，VisitEntity也是单实例的
        print my_entity.my_bus
        print my_entity

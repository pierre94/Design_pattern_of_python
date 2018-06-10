# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: FlyWeight
@time: 30/05/2018 10:34 PM
"""


class Coffee:
    name = ""
    price = 0

    def __init__(self, name):
        self.name = name
        self.price = len(name)  # 价格 = 咖啡名的长度 （扯淡的假设）

    def show(self):
        print "Coffee Name:%s Price: %s" % (self.name, self.price)


class Customer:
    name = ""
    pass


class CoffeeFactory():
    coffee_dict = {}

    def get_coffee(self, name):
        if self.coffee_dict.has_key(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def get_coffee_count(self):
        return len(self.coffee_dict)


class Customer:
    coffee_factory = ""
    name = ""

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print "%s order %s" % (self.name, coffee_name)
        return self.coffee_factory.get_coffee(coffee_name)


"""
享元模式英文：flyweight，使用共享对象支持大量细粒度对象。
如示代码：该模式下三个用户点了两种咖啡，最终的咖啡实例为2，而不是3。

优点：减少重复对象，大大节约系统资源，在适合缓冲池的场景：如进程池和线程池 建议使用这个模式
缺点：系统复杂性提升  需要额外关注线程安全
"""
if __name__ == '__main__':
    coffee_factory = CoffeeFactory()
    custom_1 = Customer("A", coffee_factory)
    custom_2 = Customer("B", coffee_factory)
    custom_3 = Customer("C", coffee_factory)

    custom_1.order("mocha").show()
    custom_2.order("bingxue").show()
    custom_3.order("mocha").show()

    print "3 customers gen coffee's num: %s totally" % coffee_factory.get_coffee_count()

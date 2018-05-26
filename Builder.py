# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Build
@time: 26/05/2018 11:13 PM
"""


# 建造者模式
class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 14.0


class Snack():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class Order():
    burger = ""
    snack = ""

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack

    def show(self):
        print "Burger:%s" % self.burger.getName()
        print "Snack:%s" % self.snack.getName()


class orderBuilder():
    bBurger = ""
    bSnack = ""

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def build(self):
        return Order(self)


"""
建造者模式，核心在于将复杂对象的"构建"和"表示"分离，即将Order和orderBuilder分离
优点：封装性更好，适合目标对象由组件构成的场景
"""
if __name__ == '__main__':
    order_builder = orderBuilder()
    order_builder.addBurger(cheeseBurger())
    order_builder.addSnack(chips())

    order_1 = order_builder.build()
    order_1.show()

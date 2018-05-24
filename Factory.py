# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Factory
@time: 24/05/2018 12:21 AM
"""


class foodFactory():
    type = ""

    def createFood(self, foodClass):
        print self.type, " factory produce a instance"
        foodIns = foodClass()
        return foodIns


class burgerFactory(foodFactory):
    def __init__(self):
        self.type = "burger"


class snackFactory(foodFactory):
    def __init__(self):
        self.type = "snack"


class beverageFactory(foodFactory):
    def __init__(self):
        self.type = "beverage"


class Burger():
    name = ""
    price = ""

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def setPrice(self, price):
        self.price = price


class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 14


if __name__ == '__main__':
    burger_factory = burgerFactory()  # 工厂模式，使用前必须实例化
    cheese_burger = burger_factory.createFood(cheeseBurger)
    print cheese_burger.name, cheese_burger.price

    # cheese_burger_2 = burgerFactory.createFood(cheeseBurger)
    # print cheese_burger_2.name

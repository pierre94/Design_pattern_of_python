# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Bridge
@time: 2018/6/4 8:26 PM
"""


class Pen:
    shape = ""
    type = ""

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass


class Shape:
    name = ""
    param = ""

    def __init__(self, *param):
        pass

    def get_name(self):
        return self.name

    def get_param(self):
        return self.param


class Rectangle(Shape):
    def __init__(self, long, width):
        self.name = "Rectangle"
        self.param = "Long:%s,Width:%s" % (long, width)
        print "create a rectangle"


class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.param = "Radius:%s" % radius
        print "create a circle"


class NormalPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Normal Line"

    def draw(self):
        print "Drawing %s %s --- Params:%s" % (self.type, self.shape.get_name(), self.shape.get_param())


class BrushPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Brush Line"

    def draw(self):
        print "Drawing %s %s --- Params:%s" % (self.type, self.shape.get_name(), self.shape.get_param())

"""
桥梁模式bridge,将抽象与实现（角色关系）解耦，Pen只负责画画，不知道具体图案，所以我们称之为抽象角色。Shape是具体的形状，我们称之为实现化角色。
所谓的桥，就是抽象化角色的抽象类和实现化角色的抽象类之间的引用关系。
优点：
1、抽象角色与实现角色相分离，二者可以独立设计，不受约束；
2、扩展性强：抽象角色和实现角色可以非常灵活地扩展。
不适用场景：
1、不适用继承或者原继承关系中抽象类可能频繁变动的情况
"""
if __name__ == '__main__':
    normal_pen_circle = NormalPen(Circle("15cm"))
    bursh_open_rectangle = BrushPen(Rectangle("17cm", "10cm"))
    normal_pen_circle.draw()
    bursh_open_rectangle.draw()

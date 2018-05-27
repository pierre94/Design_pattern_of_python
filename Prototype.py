# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Prototype
@time: 27/05/2018 3:46 PM
"""
from copy import copy, deepcopy


class simpleLayer():
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackground(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, b):
        self.background = b

    def clone(self):
        return copy(self)

    def deepClone(self):
        return deepcopy(self)


"""
原型模式，使用复制的方式实现同样的一个实例，比内存中直接新建一个对象实例节省不少资源
深拷贝与浅拷贝的区别：
浅拷贝直接对拷贝后对象的属性进行引用，当拷贝后对象发生变化，则原始对象的属性也发生变化
深拷贝是直接复制，后面和原始对象没有直接关系了
"""
if __name__ == '__main__':
    dog_layer = simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print "BackGround:", dog_layer.getBackground()
    print "Painting", dog_layer.getContent()
    another_dog = dog_layer.clone()
    print "BackGround:", another_dog.getBackground()
    print "Painting:", another_dog.getContent()

    another_dog_deep = dog_layer.deepClone()
    print "BackGround:", another_dog_deep.getBackground()
    print "Painting:", another_dog_deep.getContent()

    # 改变浅拷贝的值，原始对象值也变了，深拷贝的值不变
    another_dog.setParent(128)
    print "@@@when copy dog's BackGround change:"
    print "original dog's BackGround:", dog_layer.getBackground()
    print "copy dog's BackGround:", another_dog.getBackground()
    print "deepCopy dog's BackGround:", another_dog_deep.getBackground()
    another_dog.setParent(0)  # 恢复原来的值
    # 改变深拷贝的值，其他对象的值不受影响
    another_dog_deep.setParent(128)
    print "@@@when deepCopy dog's BackGround change:"
    print "original dog's BackGround:", dog_layer.getBackground()
    print "copy dog's BackGround:", another_dog.getBackground()
    print "deepCopy dog's BackGround:", another_dog_deep.getBackground()

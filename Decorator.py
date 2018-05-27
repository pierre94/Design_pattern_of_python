# encoding: utf-8
"""
@version: 1.0
@author: pierrexiong
@file: Decorator
@time: 27/05/2018 7:09 PM
"""
import time


def log(func):
    def wrapper(*args, **kw):
        print "call %s():" % func.__name__
        return func(*args, **kw)

    return wrapper


@log
def now():
    print time.time()

"""
装饰器模式与代理模式有点相近。python天然支持装饰器，没必要再深入实现装饰器了
"""
if __name__ == '__main__':
    now()

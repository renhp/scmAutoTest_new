# __new__()方法

class Dog(object):
    def __init__(self):
        print("init方法")

    def __del__(self):
        print("del方法")

    def __str__(self):
        print("str方法")
        return "这是一个Dog类"

    def __new__(cls):       # 如果有则创建对象时调用这个方法，不写会调用父类的__new__()方法
        print(id(cls))
        print("new方法")
        return object.__new__(cls)      # 调用父类的new方法时会返回一个对象，然后把对象返回给创建对象的变量


print(id(Dog))      # 和上面的new方法中的cls指定是同一个对象
xtq = Dog()
"""
xtq = Dog() 实际操作了三个步骤：
    1.调用__new__方法创建对象，然后找一个变量接收new的返回值，该值是创建的对象的引用；
    2.调用__init__(传的是刚刚创建出来的对象的应用),
    3.返回对象的引用
    new方法只负责创建对象
    init方法只负责初始化
"""


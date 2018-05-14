# 单例:不管创建多少次对象都只有一个对象

class Dog(object):
    __instance = None       # 私有的类属性(instance:实例)
    __init_flag = False
    def __new__(cls, name):     # 参数需与init方法中的一直，不然会报错
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance       # 返回上一次创建对象的引用

    def __init__(self, name):       # 实现只初始化一次
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True

    def __str__(self):
        return self.name


a = Dog("李白")
b = Dog("李红")
print(a, id(a), b, id(b))

print("==", None)


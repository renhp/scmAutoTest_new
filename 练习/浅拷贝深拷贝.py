# 浅拷贝深拷贝
import copy

a = [11, 22, 33]
b = a                   # 浅拷贝:拷贝对象的引用，两个使用的是同一个对象
print(id(a), id(b))
print(b)

c = copy.deepcopy(a)    # 深拷贝:创建一个新对象，新对象的值和老对象的值一样,递归拷贝
print(id(a), id(c))
print(c)

e = copy.copy(a)        # 拷贝:值拷贝第一层，也会创建新对象



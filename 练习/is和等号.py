# is 和 ==

a = -10000
b = -10000
print(id(a))
print(a is b)

a = -10000
c = 10000000000
b = 10000000000
print(id(a))
print(c is b)

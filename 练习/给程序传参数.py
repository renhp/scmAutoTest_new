# 给程序传参
import sys

print(sys.argv)
name = None
if len(sys.argv) > 1:
    name = sys.argv[1]
print("欢迎 %s 的到来!!!" % name)



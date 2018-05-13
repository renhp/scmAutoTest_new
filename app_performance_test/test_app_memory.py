# 测试APP的内存:需要分析虚存和实存

import csv
import os
import time


# 控制类
class Controller(object):

    def __init__(self):
        self.alldata = [("id", "VSS", "RSS")]

    # 分析数据
    def analyzeData(self):
        content = self.readFile()
        i = 0
        for line in content:
            if "com.taobao.taobao" in line:
                print(line)
                line = "#".join(line.split())       # 用"#"替换字符串中的空格
                s = line.split("#")
                vss = s[7].strip("K")       # strip("K"): 去掉字符串"K"
                rss = s[8].strip("K")
                # 将数据存入数组中
                self.alldata.append((i, vss, rss))
                i += 1

    # 数据存储（可以单独封装起来）
    def saveDataToCSV(self):
        csvfile = None
        try:
            csvfile = open("memory.csv", 'w', encoding='utf-8')  # 使用utf-8编码
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)
        finally:
            csvfile.close()
        print(self.alldata)

    # 读取数据文件
    def readFile(self):
        mfile = None
        try:
            mfile = open("meminfo", "r")
            content = mfile.readlines()
        finally:
            mfile.close()
        return content

def main():
    controller = Controller()
    controller.analyzeData()
    controller.saveDataToCSV()


if __name__ == "__main__":
    main()


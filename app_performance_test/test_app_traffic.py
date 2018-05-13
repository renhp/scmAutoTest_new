# 测试APP的流量(traffic)
# 【有问题“testProcess()”方法】

import os
import csv
import string
import time


# 控制类
class Controller(object):
    def __init__(self, count):
        # 定义测试的次数
        self.counter = count
        # 定义收集数据的数组
        self.alldata = [("timestamp", "traffic")]

    # 单次测试
    def testProcess(self, package_name):
        # result = os.popen("adb shell ps | grep 包名")      # linux系统
        results = os.popen("adb shell ps ")
        pid = None
        for line in results:
            result = line.split(" ")[-1]
            if result == package_name:
                pid = line.split(" ")[5]
                break
        # 获取进程ID使用的流量
        traffic = os.popen("adb shell cat /proc/%s/net/dev" % pid)
        receive, transmit, receive2, transmit2 = None, None, None, None
        for line in traffic:
            if "r_rmnet_data0" in line:
                # 将所有空行换成“#”
                line = r"#".join(line.split())
                # 按“#”号拆分，获取收到和发出的流量
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
            elif "r_rmnet_data1" in line:
                # 将所有空行换成“#”
                line = r"#".join(line.split())
                # 按“#”号拆分，获取收到和发出的流量
                receive2 = line.split("#")[1]
                transmit2 = line.split("#")[9]

        # 计算所有流量的之后
        # all_traffic = string.atoi(receive) + string.atoi(transmit) + string.atoi(receive2) + string.atoi(transmit2)
        all_traffic = int(receive) + int(transmit) + int(receive2) + int(transmit2)
        # 按KB计算流量值
        all_traffic = all_traffic/1024
        # 获取当前时间
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, all_traffic))

    # 多次测试过程控制
    def run(self, package_name):
        while self.counter > 0:
            self.testProcess(package_name)
            self.counter -= 1
            # 控制采集频率
            time.sleep(5)

    # 数据存储
    def saveDatoToCSV(self):
        csvfile = None
        try:
            csvfile = open("traffic.csv", "w", encoding="utf-8")  # 使用utf-8编码
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)
        finally:
            csvfile.close()
        print(self.alldata)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime


if __name__ == "__main__":
    controller = Controller(5)
    controller.run('com.taobao.taobao')
    controller.saveDatoToCSV()


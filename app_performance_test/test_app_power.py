# 测试APP的电量：如果有条件用对应的硬件设备测试更准确

import csv
import os
import time


# 控制类
class Contorller(object):

    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "power_Status")]

    # 单次测试过程
    def testProcess(self):
        # 执行获取电量的命令
        cmd = 'adb shell dumpsys battery'
        result = os.popen(cmd)
        # 获取当前电量的level值
        power = None
        for line in result:
            if "level" in line:
                power = line.split(":")[1]

        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, power))

    # 多次测试过程控制
    def run(self):
        cmd = 'adb shell dumpsys battery set status 1'
        os.popen(cmd)       # 先设置为非充电模式
        while self.counter > 0:
            self.testProcess()      # 执行单个测试
            self.counter -= 1
            time.sleep(3)        # 控制检测频率

    # 获取当前的时间
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def saveDataToCSV(self):
        csvfile = None
        try:
            csvfile = open("power.csv", 'w', encoding='utf-8')  # 使用utf-8编码
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)
        finally:
            csvfile.close()
        print(self.alldata)

def main(count):
    """
    :param count: 次数
    :return:
    """
    controller = Contorller(count)
    controller.run()
    controller.saveDataToCSV()

if __name__ == "__main__":
    main(10)





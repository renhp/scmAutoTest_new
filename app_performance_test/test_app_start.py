# APP性能测试:测试启动关闭，进入后台的时间【已通过】
"""
    注测试：
        1，分析的时候需要去除第一个数据，第一个会不太好准确
        2，在生成的CSV文件中算出平均值和生成折线统计图，查看波动情况
        3，其实获启动前和启动后的时间更有价值，后期可以优化
"""
import csv
import os
import time


class App(object):
    def __init__(self):
        self.content = None
        self.startTime = 0

    # 启动APP
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.taobao.taobao/com.taobao.tao.homepage.MainActivity3'
        self.content = os.popen(cmd)       # 在命令行执行命令,并接收返回值

    # 停止APP
    def StopApp(self):
        cmd = 'adb shell am force-stop com.taobao.taobao'
        os.popen(cmd)  # 在命令行执行命令

    # 停止APP:热启动
    def StopHotApp(self):
        cmd = 'adb shell input keyevent 3'
        os.popen(cmd)  # 在命令行执行命令

    # 获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


# 控制类
class Controller(object):

    def __init__(self, count=0):
        self.app = App()
        self.counter = count    # 默认执行次数
        self.alldata = [("timestamp", "elasedtime")]

    # 单次测试过程
    def tetsProcess(self, test_type):
        """
        :param test_type: 为1是冷启动，为2是热启动
        :return:
        """
        if test_type != 1 and test_type != 2:
            raise NameError("请输入1或2: 1为冷启动，2为热启动!!!")
        self.app.LaunchApp()
        time.sleep(5)
        elpasedtime = self.app.GetLaunchedTime()
        if test_type == 1:
            self.app.StopApp()
        else:
            self.app.StopHotApp()
        time.sleep(3)
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime, elpasedtime))

    # 多次执行测试过程
    def run(self, test_type):
        while self.counter > 0:
            print("执行倒数第%d" % (self.counter))
            self.tetsProcess(test_type)
            self.counter -= 1

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def saveDataToCSV(self, fielName):
        csvfile = None
        try:
            csvfile = open(fielName, 'w', encoding='utf-8')      # 使用utf-8编码
            writer = csv.writer(csvfile)
            sum, i = 0, 0
            for num in self.alldata:
                if i < 2:
                    i += 1
                    continue
                i += 1
                time = int(num[1])
                sum += time
            avg = sum / (len(self.alldata) - 2)
            self.alldata.append(("去除首值后平均值", avg))
            writer.writerows(self.alldata)
        finally:
            csvfile.close()
        print(self.alldata)

def main(time, test_type, fileName):
    controller = Controller(time)
    controller.run(test_type)   # 启动
    controller.saveDataToCSV(fileName)


if __name__ == "__main__":
    main(4, 1, 'startTime.csv')         # 冷启动
    time.sleep(2)
    main(4, 2, 'startHotTime.csv')      # 热启动: 目前热启动的退到后台命令有问题



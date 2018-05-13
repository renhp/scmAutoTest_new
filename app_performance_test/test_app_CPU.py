# 测试APP的CPU使用率
import csv
import os
import time


# 控制类
class Contorller(object):

    def __init__(self, count, waiting_time, package_name, activity, file_name):
        self.counter = count
        self.alldata = [("timestamp", "CPU_Status")]
        self.package_name = package_name
        self.waiting_time = waiting_time
        self.file_name = file_name
        cmd = 'adb shell am start -W -n %s/%s' % (package_name, activity)
        self.content = os.popen(cmd)  # 在命令行执行命令,并接收返回值

    # 用于测试完后停止APP
    def StopApp(self):
        cmd = 'adb shell am force-stop %s' % self.package_name
        os.popen(cmd)  # 在命令行执行命令

    # 单次测试过程
    def testprocess(self, package_name):
        """
        :param package_name: 为包名
        :return:
        """
        command = "adb shell dumpsys cpuinfo "
        # if condition is not None:
        #     command += "| grep %s" %package_name      # 适用于Linux系统
        result = os.popen(command)
        for line in result.readlines():
            if package_name in line:
                cpu_value = line.split("%")[0]
                currenttime = self.getCurrentTime()
                self.alldata.append((currenttime, cpu_value))
                break

    # 多次执行测试过程
    def run(self):
        """
        :param waiting_time: 间隔时间
        :param package_name: 包名
        :return:
        """
        while self.counter > 0:
            self.testprocess(self.package_name)      # 执行单个测试
            self.counter -= 1
            time.sleep(self.waiting_time)        # 控制检测频率

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据存储（可以单独封装起来）
    def saveDataToCSV(self):
        csvfile = None
        try:
            csvfile = open(self.file_name, 'w', encoding='utf-8')  # 使用utf-8编码
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)
        finally:
            csvfile.close()
        print(self.alldata)

def main(count, waiting_time, package_name, activity, file_name):
    """
    :param count: 次数
    :param waiting_time:间隔时间
    :param package_name: 包名
    :param activity: 活动名，自动启动APP
    :param file_name: 报告文件名
    :return:
    """
    controller = Contorller(count, waiting_time, package_name, activity, file_name)
    controller.run()
    controller.saveDataToCSV()
    controller.StopApp()        # 测试完后关闭APP


if __name__ == "__main__":
    main(30, 3, "com.taobao.taobao", "com.taobao.tao.homepage.MainActivity3", "CPUUser.csv")




# 管理、执行测试
import unittest
import HTMLTestRunner
import time
from sendEmail import exeTest
from utils.configs import Configs
from utils.logs import Logs


# 准备测试套件
def creatSuitel():
    # 测试用例存放目录
    conf = Configs()                                # 实例化配置对象
    case_dir = conf.getTestCasePath()               # 获取测试用例目录
    log.info('已获取测试用例所在目录')
    # 创建测试套件对象
    testunit = unittest.TestSuite()
    log.info('已创建测试套件')
    # discover方法定义【可以自定义文件开头单词：本案例要修改测试用例文件的开头为“start_”!!!】
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='start_*.py')       # 查找以start开头的.py文件，可以自定义文件开头单词
    # discover = unittest.defaultTestLoader.discover(case_dir + '\\scm_warehousemanage', pattern='start_*.py')
    log.info('已检索到测试用例目录下所有"start_…"用例脚本')
    # discover方法筛选出来的用例，循环添加到测试套件中【一定要修改测试用例文件的开头为“start_”开头!!!】
    log.info('开始添加测试用例到测试套件中')
    i = 1
    # print('====【】', discover)
    for test_suite in discover:         # 【可以自定义文件开头单词：本案例要修改测试用例文件的开头为“start_”!!!】
        # print('====【】', test_suite)
        for test_case in test_suite:    # 【可以自定义文件开头单词：本案例要修改测试用例文件的开头为“start_”!!!】
            print("开始添加第 %d 个测试用例" % i)
            print('====', test_case)
            testunit.addTests(test_case)    # 添加到测试套件中
            log.info('已添加 %d 个测试用例' % i)
            i = i + 1
    print('测试套件已完成：', testunit)  # 输出添加成功的测试用例文件及被测试的方法
    log.info('测试套件已准备添加完成，共有 %d 个测试用例' % (i - 1))
    return testunit

# 调用creatSuitel()方法，获取测试用例套件
log = Logs.getLogger()
log.info('程序启动')
print('程序启动')
log.info('开始生成测试套件')
print('开始生成测试套件')
allTestNames = creatSuitel()

# 获取当前时间，写到报告文件名字中
log.info('准备测试报告')
now_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())     # 获取当前系统时间
# 定义个报告存放路径，
confs = Configs()
report_path = confs.getReportPath()
filename = report_path + r'\result' + '_[' + now_time + '].html'
fp = open(filename, 'wb')
'''所有方式都需要用的下面的'''
print('创建测试报告文件')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'综合测试报告',
    description=u'用例执行情况:')
log.info('测试报告文件已准备好，等待写入内容')
'''所有方式都需要用的下面的运行实例，否则还可以用【unittest.main()】方法'''


# 执行测试用例
if __name__ == "__main__":
    # 执行测试用例
    log.info('开始执行测试用例')
    print('开始执行测试用例')
    runner.run(allTestNames)
    log.info('已执行所有测试用例')
    print('用例执行完毕')

    # 发邮件
    log.info('调用发邮件模块')
    st = exeTest()
    st.sendReportMail()
    log.info('结束程序')








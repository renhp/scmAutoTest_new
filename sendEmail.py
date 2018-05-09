# 发邮件：1、找到测试报告；2、发送邮件
import smtplib
from email.mime.text import MIMEText
import os
from utils.configs import Configs
from utils.logs import Logs



class exeTest():

    # 定义发送邮件方法
    def sentMail(self, file_name):
        self.log.info('准备邮件信息数据')
        # 第三方 SMTP 服务
        mail_host = "smtp.163.com"  # SMTP服务器
        mail_user = "15000478857@163.com"  # 用户名
        mail_pass = "16319950918zyy"  # 授权密码，非登录密码
        sender = '15000478857@163.com'  # 发件人邮箱(最好写全, 不然会失败)
        receivers = ['294043642@qq.com', '1412933450@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        title = '这是新邮件主题'  # 邮件主题        # 邮件主题
        f = open(file_name, 'rb')           # 打开测试报告文件
        content = f.read()                  # 读取邮件内容【HTML格式的】
        f.close()                           # 释放资源
        self.log.info('邮件信息数据已准备好')

        # 创建发邮箱对象，同时添加内容
        message = MIMEText(content, 'html', 'utf-8')  # 内容, 格式, 编码【根据内容选择格式】
        self.log.info('已定义邮件格式')
        message['Subject'] = title  # 添加邮件标题
        message['From'] = "{}".format(sender)  # 添加发件人邮箱
        message['To'] = ",".join(receivers)  # 添加收件人邮箱列表
        self.log.info('已添加标题、发件人、收件人等信息')

        # 发送邮件
        print("开发发送邮件")
        self.log.info('开始发送邮件')
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
            print("邮件发送成功")
            self.log.info('邮件发送成功')
        except smtplib.SMTPException as e:
            print("邮件发送失败!!!")
            self.log.info('邮件发送失败!!!')
            print(e)

    # 定义查找测试报告
    def findReport(self):
        print('寻找最新测试报告')
        self.log.info('寻找最新测试报告')
        # 找文件路径
        conf = Configs()                        # 实例化配置对象
        result_dir = conf.getReportPath()       # 获取报告存放路径
        lists = os.listdir(result_dir)  # 获取目录中的所有文件列表
        lists.sort(key=lambda fn: os.path.getatime(result_dir + "\\" + fn) if not os.path.isdir(result_dir + "\\" + fn) else 0)
        print('最新测试报告为：' + lists[-1])
        self.log.info('已找到最新测试报告')
        # 【os.path.join()】:join()方法用来连接字符串，通过路径与文件名的拼接，我们将得到目录下最新被创建的的文件名的完整路径。
        file_new = os.path.join(result_dir, lists[-1])  # 获取最新文件的完整路径
        self.log.info('已获取最新测试报告文件绝对路径')
        print('最新测试报告路径为：', file_new)
        return file_new

    # 发邮件功能方法
    def sendReportMail(self):
        self.log = Logs.getLogger()
        self.log.info('调用查找测试报告模块')
        file_new = self.findReport()     # 调用查找测试报告
        self.log.info('调用发送邮件')
        self.sentMail(file_new)          # 调用发邮件的方法

if __name__ == "__main__":
    # 实例化

    sd = exeTest()
    # 执行发邮件
    sd.sendReportMail()




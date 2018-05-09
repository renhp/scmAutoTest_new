import logging.handlers
import time
from utils.configs import Configs



class Logs:

    logger = None
    # 日志级别
    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "d"                     # 设置最低日志级别
    log_max_byte = 10 * 1024 * 1024     # 设定日志文件最大内存
    log_backup_count = 5                # 当第一个文件写满后最大备份日志文件数
    conf = Configs()                    # 创建配置对象
    log_path = conf.getLogPath()        # 获取不同环境下的日志路径
    log_file = log_path + r'\scm_test.log'


    @staticmethod
    def getLogger():

        if Logs.logger is not None:
            return Logs.logger

        Logs.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename=Logs.log_file,
                                                           maxBytes=Logs.log_max_byte,
                                                           backupCount=Logs.log_backup_count,
                                                           encoding='UTF-8')
        log_fmt = logging.Formatter("%(asctime)s-【scm测试日志 :--%(levelname)s :--%(message)s :--%(filename)s:%(lineno)d")
        log_handler.setFormatter(log_fmt)
        Logs.logger.addHandler(log_handler)
        Logs.logger.setLevel(Logs.levels.get(Logs.log_level))
        return Logs.logger


if __name__ == "__main__":
    logger = Logs.getLogger()
    logger.debug("this is a debug msg!")    # debug
    logger.info("this is a info msg!")      # info
    logger.warn("this is a warn msg!")      #
    logger.error("this is a error msg!")
    logger.critical("this is a critical msg!")




# -*- coding:utf-8 -*-
"""
    @Author   ：
    @FileName : my_log.py
    @desc     : 描述
"""
import logging


class Logger:
    def __init__(self, log_file=None, level=logging.DEBUG):
        # 创建日志记录器
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        # 创建控制台处理器并设置日志级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # 创建文件处理器并设置日志级别
        if log_file:
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(level)

        # 创建日志格式器并将其附加到处理器上
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        if log_file:
            file_handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        self.logger.addHandler(console_handler)
        if log_file:
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

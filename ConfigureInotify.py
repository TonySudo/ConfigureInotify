#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016 - zengjf <zengjf42@163.com>

import configparser
import threading

# 初始化配置
class ConfigureInotify(threading.Thread):

    __mutex = threading.Lock()
    __configure_file_path = "config.ini"
    config = configparser.ConfigParser()

    # 使用单例模式来生成统一的对象
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "_inst"):

            # 单例对象
            cls._inst = super(ConfigureInotify, cls).__new__(cls)
            cls.config.read(cls.__configure_file_path)

        return cls._inst

    @classmethod
    def parse_config(cls):

        cls.__mutex.acquire()

        # 配置并解析配置文件
        cls.config.read(cls.__configure_file_path)

        cls.__mutex.release()

    @classmethod
    def set_config_file(cls, file_path):

        cls.__configure_file_path = file_path

    @classmethod
    def run(cls):
        print("zengjf")

    @classmethod
    def monitoring_config(cls):
        pass

    @classmethod
    def stop_monitor(cls):
        pass


configures = ConfigureInotify()
configures.set_config_file("config.ini")

if __name__ == '__main__':

    # 输出信息：
    #     < __main__.Configures object at 0x000001F27F04DE48 >
    #     < __main__.Configures object at 0x000001F27F04DE48 >
    #     < __main__.Configures object at 0x000001F27F04DE48 >
    print(ConfigureInotify())
    print(ConfigureInotify())
    print(configures)
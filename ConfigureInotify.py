#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 - zengjf <zengjf42@163.com>

import configparser
import threading
import os
import pyinotify
from pyinotify import WatchManager, Notifier, ProcessEvent

class InotifyEventHandler(ProcessEvent):
    def process_IN_MODIFY(self, event):
        # reparse the configure file
        ConfigureInotify.parse_config()

# 初始化配置
class ConfigureInotify(threading.Thread):

    __mutex = threading.Lock()
    __configure_file_path = "config/config.ini"
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

        print("parse_config")

    @classmethod
    def set_config_file(cls, file_path):

        cls.__configure_file_path = file_path

    @classmethod
    def run(cls):
        wm = WatchManager()
        mask = pyinotify.IN_MODIFY
        notifier = Notifier(wm, InotifyEventHandler())
        wm.add_watch(os.path.dirname(cls.__configure_file_path), mask, auto_add= True, rec=True)

        # print("now starting monitor config directory." )

        while True:
            try:
                notifier.process_events()
                if notifier.check_events():
                    notifier.read_events()
            except KeyboardInterrupt:
                print("keyboard Interrupt.")
                notifier.stop()
                break

configureInotify = ConfigureInotify()

if __name__ == '__main__':

    # 输出信息：
    #     < __main__.Configures object at 0x000001F27F04DE48 >
    #     < __main__.Configures object at 0x000001F27F04DE48 >
    #     < __main__.Configures object at 0x000001F27F04DE48 >
    print(ConfigureInotify())
    print(ConfigureInotify())
    print(configureInotify)

    configureInotify.set_config_file("config/config.ini")
    configureInotify.start()

    while True:
        pass


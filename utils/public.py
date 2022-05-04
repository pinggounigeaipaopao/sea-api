# -*- coding:utf-8 -*-
import os
import configparser
import logging
import logging.config

config = configparser.ConfigParser()

basedir = os.path.split(os.path.realpath(__file__))[0]
os.chdir(basedir)
config_file = basedir + '/../config/config.ini'


def data_dir(data="data", fileName=None):
    '''查找文件的路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), data, fileName)

# 配置日志相关信息
def getConfigValue(section, option):
    config.read(config_file)
    return config.get(section, option)


def setConfigValue(section, option, value):
    config.read(config_file)
    config.set(section, option, value)
    with open(config_file, mode='w') as f:
        config.write(f)


def loggerPath(level):
    print(config_file)
    logging.config.fileConfig(config_file)
    logger_obj = logging.getLogger(level)
    return logger_obj


def getLogger():
    return loggerPath('mytest')


def getLoggerStd():
    return loggerPath('root')

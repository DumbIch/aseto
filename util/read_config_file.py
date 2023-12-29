# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 24.08.2023 13:55
@file: read_config_file.py
@desc:
"""


# For testing
if __name__ == '__main__':
    from configparser import ConfigParser

    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"

    # К сожалению конфигурационные файлы для регистраторов ПАРМА не соответсвуют стандартам ini-файлов для модуля configparser
    # А вот файлы bootce.ini поддерживаются, но проще работать со всеми файлами одинаково
    # config_file = "b2dodrv.ini"
    # config_file = "b1dodrv.ini"
    config_file = "bootce.ini"
    config_file_path = config_path + config_file

    cfg = ConfigParser()
    cfg.read(str(config_file_path), 'utf-8')
    sections = cfg.sections()
    print(sections)



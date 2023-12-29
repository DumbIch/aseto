# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 22.08.2023 13:45
@file: get_startup_timestamp.py
@desc:
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class StartupTimestamp:
    order: str
    timestamp: datetime


def get_startup_timestamp(path, encoding='cp866', title_separator='', message_separator=''):
    file_name = full_path.rsplit('/', 1)[1]
    print(file_name)
    (name, _, extension) = file_name.partition(".")
    if name.find('_') == 2:
        (order, _date, _time) = name.split("_")
        date = [_date[4::], _date[2:4:], _date[:2:]]
        time = [_time[:2:], _time[2:4:], _time[4::]]
        print(f"{order} : {'.'.join(date)} : {'-'.join(time)}")
        return StartupTimestamp(order, )
    else:
        order = name[:2:]

    # else:
    #     with open(path, mode="r", buffering=-1, encoding=str(encoding), errors=None) as f:
    #     title_block = f.read(200)
    #     prepare = title_block.partition(str(title_separator))
    #     prepare_message = prepare[0]
    #     startup_message = prepare_message.partition(str(message_separator))[2]
    #     return repr(startup_message)


# For testing
if __name__ == '__main__':
    dir_startup = "/home/dumdumbich/develop/server/testData/do/"
    file_startup = "b1q6qah4.do"
    # file_startup = "b1q6qzto.do"
    # file_startup = "B1_221001_155643.DO"
    full_path = dir_startup + file_startup
    start_condition = "ДЗ( Напр. АБ ОЩПТ-1:+Uаб отн. земли, 30, 45, 20 ) 'значение ниже нормы'"

    # print(get_startup_timestamp(full_path, 'cp866', "\x00\x00", "\x00Пуск "))

    # file_name = full_path.rsplit('/', 1)[1]
    # print(file_name)
    # (name, _, extension) = file_name.partition(".")
    # if name.find('_') == 2:
    #     (order, _date, _time) = name.split("_")
    #     date = [_date[4::], _date[2:4:], _date[:2:]]
    #     time = [_time[:2:], _time[2:4:], _time[4::]]
    #     print(f"{order} : {'.'.join(date)} : {'-'.join(time)}")

    with open(full_path, mode="r", buffering=-1, encoding='cp866', errors=None) as f:
        title_block = f.read(200)
        (prepare, _, _) = title_block.partition("\x00\x00")
        prepare_message = prepare
        print(prepare_message)
        (_, _, startup_message) = prepare_message.partition("\x00Пуск ")
        print(repr(startup_message))
        (date, time, message) = startup_message.strip().expandtabs(1).split(' ', 2)
        print(f"{str(date).strip()} : {str(time).strip()} : {str(message).strip()}")

# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 22.08.2023 13:14
@file: does_start_condition_match.py
@desc:
"""


def does_start_condition_match(path, encoding, condition):
    with open(path, mode="r", buffering=-1, encoding=str(encoding), errors=None) as f:
        title_block = f.read(200)
        if title_block.rfind(condition) != -1:
            return True
        else:
            return False


# For testing
dir_startup = "/home/dumdumbich/develop/server/testData/do/"
# file_startup = "b1q6qah4.do"
file_startup = "b1q6qzto.do"
full_path = dir_startup + file_startup
start_condition = "ДЗ( Напр. АБ ОЩПТ-1:+Uаб отн. земли, 30, 45, 20 ) 'значение ниже нормы'"

print(does_start_condition_match(full_path, 'cp866', start_condition))

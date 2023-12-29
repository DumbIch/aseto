# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 21.08.2023 12:35
@file: determine_text_file_encoding.py
@desc:
"""

code_pages = ['cp866', 'utf-8', 'cp1251']


def determine_config_file_encoding(path, text) -> str:
    code_page_determinate = False
    file_code_page = ""
    for code_page in code_pages:
        with open(path, mode='rt', buffering=-1, encoding=code_page, errors='ignore') as f:
            for line in f:
                if line.strip().find(str(text)) != -1:
                    code_page_determinate = True
                    file_code_page = str(code_page)
                    break
            if code_page_determinate:
                break
    return file_code_page


# For testing
config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
config_file = "b1dodrv.ini"
# config_file = "b2dodrv.ini"
config_file_path = config_path + config_file

print(str(determine_config_file_encoding(config_file_path, '[Регистратор]')))

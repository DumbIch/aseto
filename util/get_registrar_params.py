# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 22.08.2023 12:51
@file: get_registrar_params.py
@desc:
"""
import os
from os import walk

from util.determine_registrar_type_by_config_file import determine_registrar_type_by_config_file
from util.get_params_dict_from_config_file_section import get_params_dict_from_config_file_section
from util.determine_text_file_encoding import determine_config_file_encoding
from util.get_params_list_from_config_file_section import SECTION_REGISTRAR


def get_config_files_list(target):
    config_files_list = []
    for (root, dirs, files) in walk(str(target)):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            if 'ini' in ext:
                config_file_path = os.path.join(target, root, file)
                print(os.path.normpath(os.path.abspath(config_file_path)))
                config_files_list.append(config_file_path)
    return config_files_list


def get_config_files_encoding_dict(config_files_list: []):
    _config_files_encoding_dict = {}
    for file in config_files_list:
        config_file_encoding = determine_config_file_encoding(file, 'Регистратор')
        if len(str(config_file_encoding)) != 0:
            _config_files_encoding_dict[file] = config_file_encoding
    return _config_files_encoding_dict


# def get_registrar_params_dict(config_files_dict):
def get_registrar_params_dict(target):
    config_files_list = get_config_files_list(target)
    config_files_encoding_dict = get_config_files_encoding_dict(config_files_list)
    _registrar_config_params_dict = {}
    for path, encoding in config_files_encoding_dict.items():
        _registrar_config_params_dict[path] = get_params_dict_from_config_file_section(path, SECTION_REGISTRAR,
                                                                                       encoding)
        _registrar_config_params_dict[path]["Тип"] = determine_registrar_type_by_config_file(path, encoding)
    return _registrar_config_params_dict


# For testing
if __name__ == '__main__':
    import logging

    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
    logging.basicConfig(level='DEBUG', format=fmt)
    log = logging.getLogger('get_registrar_params')

    report_dir = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/log/get-registrar-params/"
    report_file = "Report.txt"
    report_path = report_dir + report_file
    report = open(report_path, mode="w", buffering=-1, encoding='utf-8', errors=None)

    # source_path = "/home/dumdumbich/develop/server/python/data/"
    source_path = "/home/dumdumbich/develop/server/data/dr/"

    # config_list = get_config_files_list(source_path)
    # print(config_list)
    # print(f"Number of config files : {len(config_list)}")
    #
    # config_dict = get_config_files_encoding_dict(config_list)
    #
    # for key, value in config_dict.items():
    #     print(f"{key:<70} : {value:<10}")
    #
    # print(f"length of config_dict is {len(config_dict)}")

    # registrar_config_params_dict = {}
    # for full_path, encoding in config_dict.items():
    #     registrar_config_params_dict[full_path] = get_params_dict_from_config_file_section(full_path, SECTION_REGISTRAR,
    #                                                                                        encoding)
    registrar_config_params_dict = get_registrar_params_dict(source_path)

    print(f"length of registrar_config_params_dict is {len(registrar_config_params_dict)}")
    print(registrar_config_params_dict)

    for full_path, params_dict in registrar_config_params_dict.items():
        print(full_path)
        report.write(full_path + '\n')
        for key, value in params_dict.items():
            report_line = f"{key:<50} : {value:<10}"
            print(report_line)
            report.write(report_line + '\n')
        print()
        report.write('\n')

    report.flush()

    registrar_file = "Registrars.txt"
    registrar_path = report_dir + registrar_file
    registrars = open(registrar_path, mode="w", buffering=-1, encoding='utf-8', errors=None)

    registrars_dict = {}
    for full_path, params_dict in registrar_config_params_dict.items():
        registrar_dict = {}
        setup_number = ""
        for key, value in params_dict.items():
            if 'Установочный номер' == key:
                setup_number = value.lower()
            elif 'Объект' == key:
                registrar_dict[key] = value
            elif 'Название' == key:
                registrar_dict[key] = value
            elif 'Тип' == key:
                registrar_dict[key] = value
        registrars_dict[setup_number] = registrar_dict

    print(registrars_dict)
    numbers = list(registrars_dict.keys())
    numbers.sort()
    for number in numbers:
        params_dict = registrars_dict[number]
        # print(number)
        # registrars.write(number + '\n')
        keys = list(params_dict.keys())
        keys.sort(reverse=True)
        registrar_line = f"{number:<5}"
        for key in keys:
            registrar_line += f"{params_dict[key]:<20}"
            # print(registrar_line)
        registrars.write(registrar_line + '\n')
        print(registrar_line)
        # print()
        # registrars.write('\n')

    registrars.flush()

    report.close()
    registrars.close()

    log.info('App terminate successful')

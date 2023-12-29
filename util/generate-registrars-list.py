# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 21.08.2023 09:23
@file: generate-registrars-list.py
@desc:
"""
import json
from util.determine_text_file_encoding import determine_config_file_encoding
from util.get_params_list_from_config_file_section import get_params_list_from_config_file_section


def convert_config_list_to_dictionary(config_list, separator='='):
    dictionary = {}
    for item in config_list:
        if item.find(separator) != -1:
            (key, _, value) = item.partition(separator)
            dictionary[key.strip()] = value.strip()
    return dictionary


config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
config_file = "b1dodrv.ini"
config_file_path = config_path + config_file

report_dir = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/log/"
report_file = "Report.txt"
report_path = report_dir + report_file
report = open(report_path, mode="w", buffering=-1, encoding='utf-8', errors=None)

print("\n" + config_file_path)
report.write("\n" + config_file_path + "\n")

config_section_name = 'Регистратор'
file_code_page = determine_config_file_encoding(config_file_path, config_section_name)
print(file_code_page)

registrar_description_list = get_params_list_from_config_file_section(config_section_name, config_file_path, file_code_page)
registrar_dictionary = convert_config_list_to_dictionary(registrar_description_list)

# json_str = json.dumps(registrar_dictionary, ensure_ascii=False).encode(encoding="utf-8")
# print(json_str)
# print(json_str.decode())

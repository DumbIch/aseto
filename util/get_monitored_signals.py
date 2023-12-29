# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 25.08.2023 14:28
@file: get_monitored_signals.py
@desc:
"""
from util.get_params_dict_from_config_file_section import get_params_dict_from_config_file_section
from util.get_sections_list_by_config_file import get_sections_list_by_config_file


def get_monitored_signals_list(config, encode):
    print()


# For testing
if __name__ == '__main__':
    import logging

    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
    logging.basicConfig(level='DEBUG', format=fmt)
    log = logging.getLogger('get_registrar_params')

    report_dir = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/get-monitored-signals/sandbox/log/"
    report_file = "Report.txt"
    report_path = report_dir + report_file
    report = open(report_path, mode="w", buffering=-1, encoding='utf-8', errors=None)

    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/get-monitored-signals/sandbox/config/"
    # config_file = "b2dodrv.ini"
    config_file = "b1dodrv.ini"
    config_file_path = config_path + config_file

    monitored_signals_section_list = get_sections_list_by_config_file(config_file_path, 'cp1251', 'ПУ')
    print(monitored_signals_section_list)

    monitored_signals_dict = {}
    for section in monitored_signals_section_list:
        monitored_signals_dict[section] = get_params_dict_from_config_file_section(config_file_path, section, 'cp1251')

    print(monitored_signals_dict)

    report.flush()
    report.close()

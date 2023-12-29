# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 23.08.2023 10:44
@file: get_startup_events_list.py
@desc:
"""
from util.get_params_dict_from_config_file_section import get_params_dict_from_config_file_section
from util.get_params_list_from_config_file_section import SECTION_STARTUP_CONDITION


def get_startup_events_list_by_parma_rp406(config, log, nested_startup=False):
    conditions = get_params_dict_from_config_file_section(config, SECTION_STARTUP_CONDITION, 'cp866')
    startup_events = []
    with open(log, mode="r", buffering=-1, encoding='cp866', errors=None) as f:
        for _line in f:
            line = ' '.join(str(_line).strip().expandtabs(1).split())
            for key, val in conditions.items():
                if str(line).find(val) != -1:
                    if str(line).find('Вл. Пуск') != -1:
                        if not nested_startup:
                            continue
                    startup_events.append(line)
    return startup_events


def get_startup_events_list_by_parma_rp411(config, log, nested_startup=False):
    conditions = get_params_dict_from_config_file_section(config, SECTION_STARTUP_CONDITION, 'cp1251')
    startup_events = []
    with open(log, mode="r", buffering=-1, encoding='cp1251', errors=None) as f:
        for _line in f:
            line = ' '.join(str(_line).strip().expandtabs(1).split())
            for key, val in conditions.items():
                if str(line).find(val) != -1:
                    if str(line).find('Вложенный пуск') != -1:
                        if not nested_startup:
                            continue
                    startup_events.append(line)
    return startup_events


# For testing
if __name__ == '__main__':
    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
    # config_file = "d1dodrv.ini"
    config_file = "b1dodrv.ini"
    config_file_path = config_path + config_file

    dir_log = "/home/dumdumbich/develop/server/testData/log/"
    # file_log = "d1dodrv.log"
    file_log = "B1dodrv.log"
    log_file_path = dir_log + file_log

    # startup_events_list = get_startup_events_list_by_parma_rp406(config_file_path, log_file_path, False)
    startup_events_list = get_startup_events_list_by_parma_rp411(config_file_path, log_file_path, True)

    for event in startup_events_list:
        print(event)

    print(f"Condition match counter = {len(startup_events_list)}")

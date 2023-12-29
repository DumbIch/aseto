# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 22.08.2023 08:24
@file: get_params_list_from_config_file_section.py
@desc:
"""

SECTION_REGISTRAR = '  регистРатор '
SECTION_STARTUP_CONDITION = ' условия пуСка '


def get_params_list_from_config_file_section(config, section, encoding):
    params_list = []
    section_found = False
    section_name = str(section).strip().lower().capitalize()
    with open(str(config), mode="r", buffering=-1, encoding=str(encoding), errors=None) as f:
        for _line in f:
            line = ' '.join(str(_line).strip().expandtabs(1).split())
            if line.startswith(f"[{section_name}]"):
                print(f"Section [{section_name}] was found in the configuration file")
                section_found = True
                continue
            if section_found & line.startswith("["):
                print(f"Processing of the [{section_name}] section is completed")
                break
            if section_found:
                if len(line) != 0:
                    params_list.append(line)
    params_list.sort()
    return params_list


# For testing
if __name__ == '__main__':
    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
    # config_file = "b2dodrv.ini"
    config_file = "b1dodrv.ini"
    config_file_path = config_path + config_file

    # print(get_param_list_from_config_file_section(config_file_path, SECTION_REGISTRAR, 'cp866'))
    print(get_params_list_from_config_file_section(config_file_path, SECTION_STARTUP_CONDITION, 'cp1251'))

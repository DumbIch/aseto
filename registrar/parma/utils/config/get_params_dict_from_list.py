# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 16:12
@file: get_params_dict_from_list.py
@desc:
"""
from registrar.parma.utils.config import get_params_list_from_config_file_section


def get_params_dict_from_list(config, section, encoding):
    params_dict = {}
    for line in get_params_list_from_config_file_section(config, section, encoding):
        if '=' in line:
            (key, value) = line.split('=')
            _key = str(key).strip()
            # if _key.isdigit():
            #     params_key = int(_key)
            # else:
            #     params_key = _key
            params_key = int(_key) if _key.isdigit() else _key
            params_value = str(value).strip()
            params_dict[params_key] = params_value
    return params_dict


if __name__ == '__main__':

    SECTION_REGISTRAR = '  регистРатор '
    SECTION_STARTUP_CONDITION = ' условия пуСка '
    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
    # config_file = "d1dodrv.ini"
    config_file = "b1dodrv.ini"
    config_file_path = config_path + config_file


    def main():
        # startup_conditions_dict = get_params_dict_from_config_file_section(config_file_path, SECTION_STARTUP_CONDITION,'cp866')
        startup_conditions_dict = get_params_dict_from_list(config_file_path,
                                                            SECTION_STARTUP_CONDITION, 'cp1251')
        print(startup_conditions_dict)

        for startup_key, startup_value in startup_conditions_dict.items():
            print(f"{startup_key:<4} : {startup_value:<30}")

        print(f"length of startup_conditions_dict is {len(startup_conditions_dict)}")


    main()

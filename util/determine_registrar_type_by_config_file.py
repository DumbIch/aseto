# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 25.08.2023 11:02
@file: determine_registrar_type_by_config_file.py
@desc:
"""
from util.get_params_dict_from_config_file_section import get_params_dict_from_config_file_section
from util.get_params_list_from_config_file_section import SECTION_REGISTRAR


def determine_registrar_type_by_config_file(config, encoding):
    registrar_params_dict = get_params_dict_from_config_file_section(config, SECTION_REGISTRAR, encoding)
    if "Рабочий каталог" in registrar_params_dict:
        registrar_type = "Парма РП4-06"
        if "Тип" in registrar_params_dict:
            registrar_type = registrar_params_dict["Тип"]
    else:
        registrar_type = "Парма РП4-11"
    return registrar_type.upper()


if __name__ == '__main__':
    import logging

    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
    logging.basicConfig(level='DEBUG', format=fmt)
    log = logging.getLogger('determine_registrar_type_by_config_file')

    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
    # config_file = "b2dodrv.ini"
    config_file = "b1dodrv.ini"
    # config_file = "d4dodrv.ini"
    # config_file = "m1dodrv.ini"
    config_file_path = config_path + config_file

    # print(determine_registrar_type_by_config_file(config_file_path, 'cp866'))
    print(determine_registrar_type_by_config_file(config_file_path, 'cp1251'))

# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 25.08.2023 10:45
@file: get_sections_list_by_config_file.py
@desc:
"""


def get_sections_list_by_config_file(config, encoding, template=''):
    sections_list = []
    with open(str(config), mode="r", buffering=-1, encoding=str(encoding), errors=None) as f:
        for _line in f:
            line = ' '.join(str(_line).strip().expandtabs(1).split())
            if line.startswith(f"[{template}"):
                # print(f"Section {line} was found in the configuration file")
                sections_list.append(line.strip('[]'))
    return sections_list


if __name__ == '__main__':
    import logging

    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
    logging.basicConfig(level='DEBUG', format=fmt)
    log = logging.getLogger('get_sections_list_by_config_file')

    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
    # config_file = "b2dodrv.ini"
    config_file = "b1dodrv.ini"
    config_file_path = config_path + config_file

    # print(get_sections_list_by_config_file(config_file_path, 'cp866'))
    # print(get_sections_list_by_config_file(config_file_path, 'cp1251'))
    print(get_sections_list_by_config_file(config_file_path, 'cp1251', 'ПУ'))

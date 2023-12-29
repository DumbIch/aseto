# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 15:56
@file: get_sections_list_from_config_file.py
@desc:
"""


def get_sections_list_from_config_file(config, encoding, template=''):
    sections_list = []
    with open(str(config), mode="r", buffering=-1, encoding=str(encoding), errors=None) as f:
        for _line in f:
            line = ' '.join(str(_line).strip().expandtabs(1).split())
            if line.startswith(f"[{template}"):
                sections_list.append(line.strip('[]'))
    return sections_list


if __name__ == '__main__':
    config_path = "/home/dumdumbich/Yandex.Disk.Job/Documents/develop/project/ЦРАП/util/generate-registrars-list/sandbox/config/"
    # config_file = "b2dodrv.ini"
    config_file = "b1dodrv.ini"
    config_file_path = config_path + config_file


    def main():
        print(get_sections_list_from_config_file(config_file_path, 'cp1251'))


    main()

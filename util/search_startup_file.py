# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 21.08.2023 11:44
@file: search_startup_file.py
@desc:
"""
from os import walk
import time

from util.get_registrar_params import get_directories_list


# def get_report_message_from_startup_file(path, file_encoding, title_separator, message_separator):
#     global matches_files_in_current_directory  # !!! убрать
#     with open(path, mode="r", buffering=-1, encoding=str(file_encoding), errors=None) as f:  # with open(file_path, mode="r", buffering=-1, encoding='CP866', errors=None) as f:
#         title_block = f.read(200)
#         if title_block.rfind(substring) != -1:
#             matches_files_in_current_directory += 1  # !!! убрать
#             prepare = title_block.partition(str(title_separator))  # prepare = title_block.partition("\x00\x00")
#             prepare_message = prepare[0]
#             startup_message = prepare_message.partition(str(message_separator))[2]  # startup_message = prepare_message.partition("\x00Пуск ")[2]
#             return repr(startup_message) + " : " + file


path_startup = "/home/dumdumbich/develop/server/python/data/"

report_dir = "/home/dumdumbich/develop/server/python/parser/"
report_file = "Report.txt"
report_path = report_dir + report_file
report = open(report_path, mode="w", buffering=-1, encoding='utf-8', errors=None)
substring = "ДЗ( Напр. АБ ОЩПТ-1:+Uаб отн. земли, 30, 45, 20 )"

total_files_number = 0
total_checked_files_number = 0
total_matches_files_number = 0

timestamp_begin = time.perf_counter_ns()

config_directories_list = get_directories_list(path_startup)
total_folders_number = len(config_directories_list)

for directory in config_directories_list:
    directory_message = "\n\n" + directory
    print(directory_message)
    report.write(directory_message + "\n")

    files_list = []
    files_in_current_directory = 0
    checked_files_in_current_directory = 0
    matches_files_in_current_directory = 0

    directory_path = path_startup + directory + "/"
    for (current_dir, unsorted_directories_list, unsorted_files_list) in walk(directory_path):
        if len(unsorted_files_list) != 0:
            files_list.extend(unsorted_files_list)

    files_list.sort(key=str.lower)
    print(files_list)

    files_in_current_directory = len(files_list)
    total_files_number += files_in_current_directory

    for file in files_list:
        (file_name, dot, file_extension) = file.partition(".")
        if file_extension.lower() == "do":
            checked_files_in_current_directory += 1

            file_path = directory_path + file
            print("\n" + file_path)
            report.write("\n" + file_path + "\n")

            with open(file_path, mode="r", buffering=-1, encoding='CP866', errors=None) as f:
                title_block = f.read(200)

                if title_block.rfind(substring) != -1:
                    matches_files_in_current_directory += 1

                    prepare = title_block.partition("\x00\x00")
                    prepare_message = prepare[0]
                    startup_message = prepare_message.partition("\x00Пуск ")[2]
                    report_message = repr(startup_message) + " : " + file
                    print(report_message)
                    report.write(report_message + "\n")

    # report_message = get_report_message_from_startup_file(file_path)
    # report.write(report_message + "\n")

    total_checked_files_number += checked_files_in_current_directory
    total_matches_files_number += matches_files_in_current_directory

    files_in_current_directory_message = "Total of " + str(files_in_current_directory) + " files in current folder"
    print(files_in_current_directory_message)
    report.write(files_in_current_directory_message + "\n")

    checked_files_in_current_directory_message = "Checked " + str(
        checked_files_in_current_directory) + " files in current folder"
    print(checked_files_in_current_directory_message)
    report.write(checked_files_in_current_directory_message + "\n")

    matches_files_in_current_directory_message = "Matches " + str(
        matches_files_in_current_directory) + " files in current folder"
    print(matches_files_in_current_directory_message)
    report.write(matches_files_in_current_directory_message + "\n")

print("\n\n")
report.write("\n\n")

total_folders_number_message = "Total of " + str(total_folders_number) + " folders"
print(total_folders_number_message)
report.write(total_folders_number_message + "\n")

total_files_number_message = "Total of " + str(total_files_number) + " files"
print(total_files_number_message)
report.write(total_files_number_message + "\n")

total_checked_files_number_message = "Total of " + str(total_checked_files_number) + " checked files"
print(total_checked_files_number_message)
report.write(total_checked_files_number_message + "\n")

total_matches_files_number_message = "Total of " + str(total_matches_files_number) + " matches files"
print(total_matches_files_number_message)
report.write(total_matches_files_number_message + "\n")

timestamp_end = time.perf_counter_ns()
elapsed_time = timestamp_end - timestamp_begin

elapsed_time_message = "Elapsed time " + str(elapsed_time) + " ns" + " (" + str(elapsed_time / 1000000) + " ms)"
print(elapsed_time_message)
report.write(elapsed_time_message + "\n")

report.flush()
report.close()

# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 17.08.2023 16:09
@file: parse-log-entry.py
@desc:
"""
from datetime import datetime

from domain.LogEntry import LogEntry

log_entry_line = "25.11.22 09:56:14 Пуск: ОП( 1ВА01А01 яч.8 рабочий ввод: I, 0.14, 40 ) значение выше нормы"

par1, par2, par3 = log_entry_line.split(" ", 2)
print(par1)
print(par2)
print(par3)

log_entry_line_old = "01: 12.01.22 09:14:14	Фильтры ДЗ( ТН 1BZ01F01 ДГ-1GV:Ua, 46, 49, 40 ): Вл. Пуск, значение ниже нормы 5000 ms"
par4, par5, par6, par7 = log_entry_line_old.expandtabs(1).split(" ", 3)
print(par5)
print(par6)
print(par7)

source_file_text = "B1dodrv.log"

timestamp_text = "25.11.22 09:56:14"

timestamp = datetime.strptime(timestamp_text, '%d.%m.%y %H:%M:%S')

body_text = "Пуск: ОП( 1ВА01А01 яч.8 рабочий ввод: I, 0.14, 40 ) значение выше нормы"

log_entry = LogEntry(source_file_text, timestamp, body_text)
print(log_entry)
print(timestamp.date())
print(timestamp.time())

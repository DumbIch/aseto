# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 15:17
@file: parma_registrars.py
@desc:
"""
from enum import Enum


class ParmaRegistrars(Enum):
    UNKNOWN = 0
    RP4_06 = 1
    RP4_06M = 2
    RP4_08 = 3
    RP4_11 = 4
    RP4_12 = 5


parma_registrars_en = [
    "Unknown type",
    "PARMA RP4-06",
    "PARMA RP4-06M",
    "PARMA RP4-08",
    "PARMA RP4-11",
    "PARMA RP4-12",
]

parma_registrars_ru = [
    "Неизвестный тип",
    "ПАРМА РП4-06",
    "ПАРМА РП4-06M",
    "ПАРМА РП4-08",
    "ПАРМА РП4-11",
    "ПАРМА РП4-12",
]

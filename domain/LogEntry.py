# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 17.08.2023 13:51
@file: LogEntry.py
@desc:
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class LogEntry:
    source_file: str
    timestamp: datetime
    body: str

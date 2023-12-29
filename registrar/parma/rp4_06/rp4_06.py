# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 14:12
@file: rp4_06.py
@desc:
"""
from registrar import RegistrarDevice
from registrar.parma import ParmaRegistrars


class ParmaRp406(RegistrarDevice):

    def __init__(self, factory_number):
        self.config = None
        self.placement = None
        self.factory_number = factory_number

    def get_type(self):
        return ParmaRegistrars.RP4_06

    def get_factory_number(self):
        return self.factory_number

    def get_placement(self):
        return self.placement

    def set_placement(self, placement: str):
        self.placement = placement

    def read_config(self, config):
        self.config = config

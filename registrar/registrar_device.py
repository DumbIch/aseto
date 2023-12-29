# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 14:13
@file: registrar_device.py
@desc:
"""
from abc import ABC, abstractmethod


class RegistrarDevice(ABC):

    @abstractmethod
    def get_type(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_factory_number(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_placement(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def set_placement(self, placement: str):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def read_config(self, config_file):
        raise NotImplementedError("Method not implemented")

    # @abstractmethod
    # def load_config(self):
    #     raise NotImplementedError("Method not implemented")

    # @abstractmethod
    # def get_log_entry(self):
    #     raise NotImplementedError("Method not implemented")

    # @abstractmethod
    # def get_startup_entry(self):
    #     raise NotImplementedError("Method not implemented")

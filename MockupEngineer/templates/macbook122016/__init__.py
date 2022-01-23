from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'MacBook 12"'
        self.type = 'pc'
        self.year = 2016
        self.resolution = '{width} x {height}'.format(width=2304, height=1440)

        self.__template_path__ = 'macbook122016'
        self.__colors__ = {"Space Gray": 'spacegray',
                           "Gold": 'gold'}

        self.__portrait_width__ = 1430
        self.__portrait_height__ = 894
        self.__portrait_x__ = 286
        self.__portrait_y__ = 180

        self.__landscape_width__ = 1430
        self.__landscape_height__ = 894
        self.__landscape_x__ = 286
        self.__landscape_y__ = 180

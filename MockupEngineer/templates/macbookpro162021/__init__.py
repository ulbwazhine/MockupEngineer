from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'MacBook Pro 16"'
        self.type = 'pc'
        self.year = 2021
        self.resolution = '{width} x {height}'.format(width=3456, height=2234)

        self.__template_path__ = 'macbookpro162021'
        self.__colors__ = {"Silver": 'silver',
                           "Space Gray": 'spacegray'}

        self.__portrait_width__ = 1502
        self.__portrait_height__ = 963
        self.__portrait_x__ = 499
        self.__portrait_y__ = 261

        self.__landscape_width__ = 1502
        self.__landscape_height__ = 963
        self.__landscape_x__ = 499
        self.__landscape__ = 261

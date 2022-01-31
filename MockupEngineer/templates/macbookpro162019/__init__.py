from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'MacBook Pro 16"'
        self.type = 'pc'
        self.year = 2019
        self.resolution = '{width} x {height}'.format(width=3072, height=1920)

        self.__template_path__ = 'macbookpro162019'
        self.__colors__ = {"Space Gray": 'spacegray'}

        self.__portrait_width__ = 1833
        self.__portrait_height__ = 1147
        self.__portrait_x__ = 340
        self.__portrait_y__ = 224

        self.__landscape_width__ = 1833
        self.__landscape_height__ = 1147
        self.__landscape_x__ = 340
        self.__landscape_y__ = 224

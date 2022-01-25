from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'MacBook Pro 13"'
        self.type = 'pc'
        self.year = 2015
        self.resolution = '{width} x {height}'.format(width=2560, height=1600)

        self.__template_path__ = 'macbookpro132015'
        self.__colors__ = {"Silver": 'silver'}

        self.__portrait_width__ = 1424
        self.__portrait_height__ = 890
        self.__portrait_x__ = 388
        self.__portrait_y__ = 176

        self.__landscape_width__ = 1424
        self.__landscape_height__ = 890
        self.__landscape_x__ = 388
        self.__landscape_y__ = 176

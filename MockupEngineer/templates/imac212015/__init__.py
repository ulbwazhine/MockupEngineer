from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iMac 21"'
        self.type = 'pc'
        self.year = 2015
        self.resolution = '{width} x {height}'.format(width=4096, height=2304)

        self.__template_path__ = 'imac212015'
        self.__colors__ = {"Silver": 'silver'}

        self.__portrait_width__ = 1693
        self.__portrait_height__ = 954
        self.__portrait_x__ = 173
        self.__portrait_y__ = 178

        self.__landscape_width__ = 1693
        self.__landscape_height__ = 954
        self.__landscape_x__ = 173
        self.__landscape_y__ = 178

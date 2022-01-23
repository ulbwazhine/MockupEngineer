from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone 12 Mini'
        self.type = 'phone'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=1080, height=2340)

        self.__template_path__ = 'iphone12mini'
        self.__colors__ = {"Black": 'black',
                           "Blue": 'blue',
                           "Green": 'green',
                           "PRODUCT RED": 'red',
                           "White": 'white'}

        self.__portrait_width__ = 1080
        self.__portrait_height__ = 2340
        self.__portrait_x__ = 160
        self.__portrait_y__ = 160

        self.__landscape_width__ = 2340
        self.__landscape_height__ = 1080
        self.__landscape_x__ = 160
        self.__landscape_y__ = 160

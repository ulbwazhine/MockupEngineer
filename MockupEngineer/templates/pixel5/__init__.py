from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Google'
        self.name = 'Pixel 5'
        self.type = 'phone'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=1080, height=2340)

        self.__template_path__ = 'pixel5'
        self.__colors__ = {"Just Black": 'black',
                           "Sorta Sage": 'sortasage'}

        self.__portrait_width__ = 1080
        self.__portrait_height__ = 2340
        self.__portrait_x__ = 200
        self.__portrait_y__ = 200

        self.__landscape_width__ = 2340
        self.__landscape_height__ = 1080
        self.__landscape_x__ = 200
        self.__landscape_y__ = 200

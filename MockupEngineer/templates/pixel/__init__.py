from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Google'
        self.name = 'Pixel'
        self.type = 'phone'
        self.year = 2016
        self.resolution = '{width} x {height}'.format(width=1080, height=1920)

        self.__template_path__ = 'pixel'
        self.__colors__ = {"Quite Black": 'black',
                           "Really Blue": 'blue',
                           "Very Silver": 'silver'}

        self.__portrait_width__ = 932
        self.__portrait_height__ = 1656
        self.__portrait_x__ = 153
        self.__portrait_y__ = 317

        self.__landscape_width__ = 1656
        self.__landscape_height__ = 932
        self.__landscape_x__ = 346
        self.__landscape_y__ = 149

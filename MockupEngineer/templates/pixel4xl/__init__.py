from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Google'
        self.name = 'Pixel 4 XL'
        self.type = 'phone'
        self.year = 2019
        self.resolution = '{width} x {height}'.format(width=1440, height=3040)

        self.__template_path__ = 'pixel4xl'
        self.__colors__ = {"Just Black": 'black',
                           "Clearly White": 'white',
                           "Oh So Orange": 'orange'}

        self.__portrait_width__ = 1440
        self.__portrait_height__ = 3040
        self.__portrait_x__ = 100
        self.__portrait_y__ = 250

        self.__landscape_width__ = 3040
        self.__landscape_height__ = 1440
        self.__landscape_x__ = 250
        self.__landscape_y__ = 100

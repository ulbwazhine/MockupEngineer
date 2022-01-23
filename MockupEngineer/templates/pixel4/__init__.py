from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Google'
        self.name = 'Pixel 4'
        self.type = 'phone'
        self.year = 2019
        self.resolution = '{width} x {height}'.format(width=1080, height=2280)

        self.__template_path__ = 'pixel4'
        self.__colors__ = {"Just Black": 'black',
                           "Clearly White": 'white',
                           "Oh So Orange": 'orange'}

        self.__portrait_width__ = 1080
        self.__portrait_height__ = 2280
        self.__portrait_x__ = 100
        self.__portrait_y__ = 200

        self.__landscape_width__ = 2280
        self.__landscape_height__ = 1080
        self.__landscape_x__ = 200
        self.__landscape_y__ = 100

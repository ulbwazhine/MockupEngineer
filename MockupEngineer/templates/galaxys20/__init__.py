from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Samsung'
        self.name = 'Galaxy S20'
        self.type = 'phone'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=1440, height=3200)

        self.__template_path__ = 'galaxys20'
        self.__colors__ = {"Cloud Blue": 'blue',
                           "Cosmic Grey": 'grey',
                           "Pink": 'pink'}
        self.__use_mask__ = True

        self.__portrait_width__ = 1440
        self.__portrait_height__ = 3200
        self.__portrait_x__ = 200
        self.__portrait_y__ = 200

        self.__landscape_width__ = 3200
        self.__landscape_height__ = 1440
        self.__landscape_x__ = 200
        self.__landscape_y__ = 200

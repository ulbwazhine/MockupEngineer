from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone SE'
        self.type = 'phone'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=750, height=1334)

        self.__template_path__ = 'iphonese2020'
        self.__colors__ = {"Black": 'black',
                           "PRODUCT RED": 'red',
                           "White": 'white'}

        self.__portrait_width__ = 750
        self.__portrait_height__ = 1334
        self.__portrait_x__ = 150
        self.__portrait_y__ = 300

        self.__landscape_width__ = 1334
        self.__landscape_height__ = 750
        self.__landscape_x__ = 300
        self.__landscape_y__ = 150


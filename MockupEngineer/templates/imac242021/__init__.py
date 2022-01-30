from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iMac 24"'
        self.type = 'pc'
        self.year = 2021
        self.resolution = '{width} x {height}'.format(width=4480, height=2520)

        self.__template_path__ = 'imac242021'
        self.__colors__ = {"Blue": 'blue',
                           "Green": 'green',
                           "Orange": 'orange',
                           "Pink": 'pink',
                           "Purple": 'purple',
                           "Silver": 'silver',
                           "Yellow": 'yellow'}

        self.__portrait_width__ = 4216
        self.__portrait_height__ = 2375
        self.__portrait_x__ = 517
        self.__portrait_y__ = 302

        self.__landscape_width__ = 4216
        self.__landscape_height__ = 2375
        self.__landscape_x__ = 517
        self.__landscape_y__ = 302

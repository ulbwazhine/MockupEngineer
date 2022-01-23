from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPad Air 4'
        self.type = 'tablet'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=2360, height=1640)

        self.__template_path__ = 'ipadair4'
        self.__colors__ = {"Green": 'green',
                           "Rose Gold": 'rosegold',
                           "Silver": 'silver',
                           "Sky Blue": 'skyblue',
                           "Space Gray": 'spacegray'}

        self.__portrait_width__ = 1640
        self.__portrait_height__ = 2360
        self.__portrait_x__ = 150
        self.__portrait_y__ = 150

        self.__landscape_width__ = 2360
        self.__landscape_height__ = 1640
        self.__landscape_x__ = 150
        self.__landscape_y__ = 150

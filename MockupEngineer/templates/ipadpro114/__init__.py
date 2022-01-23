from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPad Pro 4 11"'
        self.type = 'tablet'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=2388, height=1668)

        self.__template_path__ = 'ipadpro114'
        self.__colors__ = {"Silver": 'silver',
                           "Space Gray": 'spacegray'}

        self.__portrait_width__ = 1668
        self.__portrait_height__ = 2388
        self.__portrait_x__ = 200
        self.__portrait_y__ = 200

        self.__landscape_width__ = 2388
        self.__landscape_height__ = 1668
        self.__landscape_x__ = 200
        self.__landscape_y__ = 200

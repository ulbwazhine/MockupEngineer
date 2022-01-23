from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone 12 Pro'
        self.type = 'phone'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=1170, height=2532)

        self.__template_path__ = 'iphone12pro'
        self.__colors__ = {"Gold": 'gold',
                           "Graphite": 'graphite',
                           "Pacific Blue": 'pacificblue',
                           "Silver": 'silver'}

        self.__portrait_width__ = 1170
        self.__portrait_height__ = 2532
        self.__portrait_x__ = 180
        self.__portrait_y__ = 180

        self.__landscape_width__ = 2532
        self.__landscape_height__ = 1170
        self.__landscape_x__ = 180
        self.__landscape_y__ = 180

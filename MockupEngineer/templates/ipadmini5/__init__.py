from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPad Mini 5'
        self.type = 'tablet'
        self.year = 2021
        self.resolution = '{width} x {height}'.format(width=2048, height=1536)

        self.__template_path__ = 'ipadmini5'
        self.__colors__ = {"Gold": 'gold',
                           "Silver": 'silver',
                           "Space Gray": 'spacegray'}

        self.__portrait_width__ = 1536
        self.__portrait_height__ = 2048
        self.__portrait_x__ = 150
        self.__portrait_y__ = 330

        self.__landscape_width__ = 2048
        self.__landscape_height__ = 1536
        self.__landscape_x__ = 330
        self.__landscape_y__ = 150

from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone Xr'
        self.type = 'phone'
        self.year = 2018
        self.resolution = '{width} x {height}'.format(width=828, height=1792)

        self.__template_path__ = 'iphonexr'
        self.__colors__ = {"Blue": 'blue',
                           "Coral": 'coral',
                           "PRODUCT RED": 'red',
                           "Silver": 'silver',
                           "Space Gray": 'spacegray',
                           "Yellow": 'yellow'}

        self.__portrait_width__ = 828
        self.__portrait_height__ = 1792
        self.__portrait_x__ = 110
        self.__portrait_y__ = 110

        self.__landscape_width__ = 1792
        self.__landscape_height__ = 828
        self.__landscape_x__ = 110
        self.__landscape_y__ = 110

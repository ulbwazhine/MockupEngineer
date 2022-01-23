from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'Watch Series 6 44mm'
        self.type = 'wear'
        self.year = 2020
        self.resolution = '{width} x {height}'.format(width=368, height=448)

        self.__template_path__ = 'watchseries644mm'
        self.__colors__ = {"Aluminum Case - Blue": 'blue_aluminum',
                           "Aluminum Case - Gold": 'gold_aluminum',
                           "Aluminum Case - Space Gray": 'spacegray_aluminum',
                           "Aluminum Case - Silver": 'silver_aluminum',
                           "Aluminum Case - PRODUCT RED": 'red_aluminum',
                           "Titanium Case - Light": 'light_titanium',
                           "Titanium Case - Dark": 'dark_titanium',
                           "Stainless Steel Case - Gold": 'gold_steel',
                           "Stainless Steel Case - Graphite": 'graphite_steel',
                           "Stainless Steel Case - Silver": 'silver_steel'}

        self.__portrait_width__ = 368
        self.__portrait_height__ = 448
        self.__portrait_x__ = 129
        self.__portrait_y__ = 241

        self.__landscape_width__ = 448
        self.__landscape_height__ = 368
        self.__landscape_x__ = 241
        self.__landscape_y__ = 129

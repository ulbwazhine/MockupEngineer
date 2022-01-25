from dataclasses import dataclass

from MockupEngineer.templates import Template


@dataclass
class Device(Template):
    def __device_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'MacBook Pro 15"'
        self.type = 'pc'
        self.year = 2015
        self.resolution = '{width} x {height}'.format(width=2880, height=1800)

        self.__template_path__ = 'macbookpro152015'
        self.__colors__ = {"Silver": 'silver'}

        self.__portrait_width__ = 1450
        self.__portrait_height__ = 906
        self.__portrait_x__ = 328
        self.__portrait_y__ = 167

        self.__landscape_width__ = 1450
        self.__landscape_height__ = 906
        self.__landscape_x__ = 328
        self.__landscape_y__ = 167

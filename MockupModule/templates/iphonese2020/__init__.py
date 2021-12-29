from dataclasses import dataclass

from MockupModule.templates import templates_path, TemplateResolution, TemplateColor, Template


@dataclass
class Device(Template):
    def __post_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone SE'
        self.type = 'phone'
        self.year = 2020
        self.example_path = templates_path + '/iphonese2020/example.png'
        self.portrait_resolution = TemplateResolution(width=750, height=1334)
        self.landscape_resolution = TemplateResolution(width=1334, height=750)

        self.colors = [
            TemplateColor(
                color='Black',
                portrait_path=templates_path + '/iphonese2020/black/portrait.png',
                landscape_path=templates_path + '/iphonese2020/black/landscape.png',
            ),
            TemplateColor(
                color='PRODUCT RED',
                portrait_path=templates_path + '/iphonese2020/red/portrait.png',
                landscape_path=templates_path + '/iphonese2020/red/landscape.png',
            ),
            TemplateColor(
                color='White',
                portrait_path=templates_path + '/iphonese2020/white/portrait.png',
                landscape_path=templates_path + '/iphonese2020/white/landscape.png',
            )
        ]

        self.__portrait_width__ = 150
        self.__portrait_height__ = 300
        self.__landscape_width__ = 300
        self.__landscape_height__ = 140


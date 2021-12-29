from dataclasses import dataclass

from MockupModule.templates import templates_path, TemplateResolution, TemplateColor, Template


@dataclass
class Device(Template):
    def __post_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone 12'
        self.type = 'phone'
        self.year = 2020
        self.example_path = templates_path + '/iphone12/example.png'
        self.portrait_resolution = TemplateResolution(width=1170, height=2532)
        self.landscape_resolution = TemplateResolution(width=2532, height=1170)

        self.colors = [
            TemplateColor(
                color='Black',
                portrait_path=templates_path + '/iphone12/black/portrait.png',
                landscape_path=templates_path + '/iphone12/black/landscape.png',
            ),
            TemplateColor(
                color='Blue',
                portrait_path=templates_path + '/iphone12/blue/portrait.png',
                landscape_path=templates_path + '/iphone12/blue/landscape.png',
            ),
            TemplateColor(
                color='Green',
                portrait_path=templates_path + '/iphone12/green/portrait.png',
                landscape_path=templates_path + '/iphone12/green/landscape.png',
            ),
            TemplateColor(
                color='PRODUCT RED',
                portrait_path=templates_path + '/iphone12/red/portrait.png',
                landscape_path=templates_path + '/iphone12/red/landscape.png',
            ),
            TemplateColor(
                color='White',
                portrait_path=templates_path + '/iphone12/white/portrait.png',
                landscape_path=templates_path + '/iphone12/white/landscape.png',
            )
        ]

        self.__portrait_width__ = 180
        self.__portrait_height__ = 180
        self.__landscape_width__ = 180
        self.__landscape_height__ = 180


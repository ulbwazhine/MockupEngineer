from dataclasses import dataclass

from MockupModule.templates import templates_path, TemplateResolution, TemplateColor, Template


@dataclass
class Device(Template):
    def __post_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone 12 Mini'
        self.type = 'phone'
        self.year = 2020
        self.example_path = templates_path + '/iphone12mini/example.png'
        self.portrait_resolution = TemplateResolution(width=1080, height=2340)
        self.landscape_resolution = TemplateResolution(width=2340, height=1080)

        self.colors = [
            TemplateColor(
                color='Black',
                portrait_path=templates_path + '/iphone12mini/black/portrait.png',
                landscape_path=templates_path + '/iphone12mini/black/landscape.png',
            ),
            TemplateColor(
                color='Blue',
                portrait_path=templates_path + '/iphone12mini/blue/portrait.png',
                landscape_path=templates_path + '/iphone12mini/blue/landscape.png',
            ),
            TemplateColor(
                color='Green',
                portrait_path=templates_path + '/iphone12mini/green/portrait.png',
                landscape_path=templates_path + '/iphone12mini/green/landscape.png',
            ),
            TemplateColor(
                color='PRODUCT RED',
                portrait_path=templates_path + '/iphone12mini/red/portrait.png',
                landscape_path=templates_path + '/iphone12mini/red/landscape.png',
            ),
            TemplateColor(
                color='White',
                portrait_path=templates_path + '/iphone12mini/white/portrait.png',
                landscape_path=templates_path + '/iphone12mini/white/landscape.png',
            )
        ]

        self.__portrait_width__ = 160
        self.__portrait_height__ = 160
        self.__landscape_width__ = 180
        self.__landscape_height__ = 180


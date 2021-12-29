from dataclasses import dataclass

from MockupModule.templates import templates_path, TemplateResolution, TemplateColor, Template


@dataclass
class Device(Template):
    def __post_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone 12 Pro'
        self.type = 'phone'
        self.year = 2020
        self.example_path = templates_path + '/iphone12pro/example.png'
        self.portrait_resolution = TemplateResolution(width=1170, height=2532)
        self.landscape_resolution = TemplateResolution(width=2532, height=1170)

        self.colors = [
            TemplateColor(
                color='Gold',
                portrait_path=templates_path + '/iphone12pro/gold/portrait.png',
                landscape_path=templates_path + '/iphone12pro/gold/landscape.png',
            ),
            TemplateColor(
                color='Graphite',
                portrait_path=templates_path + '/iphone12pro/graphite/portrait.png',
                landscape_path=templates_path + '/iphone12pro/graphite/landscape.png',
            ),
            TemplateColor(
                color='Pacific Blue',
                portrait_path=templates_path + '/iphone12pro/pacificblue/portrait.png',
                landscape_path=templates_path + '/iphone12pro/pacificblue/landscape.png',
            ),
            TemplateColor(
                color='Silver',
                portrait_path=templates_path + '/iphone12pro/silver/portrait.png',
                landscape_path=templates_path + '/iphone12pro/silver/landscape.png',
            )
        ]

        self.__portrait_width__ = 180
        self.__portrait_height__ = 180
        self.__landscape_width__ = 180
        self.__landscape_height__ = 180


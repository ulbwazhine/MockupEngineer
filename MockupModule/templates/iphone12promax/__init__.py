from dataclasses import dataclass

from MockupModule.templates import templates_path, TemplateResolution, TemplateColor, Template


@dataclass
class Device(Template):
    def __post_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone 12 Pro Max'
        self.type = 'phone'
        self.year = 2020
        self.example_path = templates_path + '/iphone12promax/example.png'
        self.portrait_resolution = TemplateResolution(width=1284, height=2778)
        self.landscape_resolution = TemplateResolution(width=2778, height=1284)

        self.colors = [
            TemplateColor(
                color='Gold',
                portrait_path=templates_path + '/iphone12promax/gold/portrait.png',
                landscape_path=templates_path + '/iphone12promax/gold/landscape.png',
            ),
            TemplateColor(
                color='Graphite',
                portrait_path=templates_path + '/iphone12promax/graphite/portrait.png',
                landscape_path=templates_path + '/iphone12promax/graphite/landscape.png',
            ),
            TemplateColor(
                color='Pacific Blue',
                portrait_path=templates_path + '/iphone12promax/pacificblue/portrait.png',
                landscape_path=templates_path + '/iphone12promax/pacificblue/landscape.png',
            ),
            TemplateColor(
                color='Silver',
                portrait_path=templates_path + '/iphone12promax/silver/portrait.png',
                landscape_path=templates_path + '/iphone12promax/silver/landscape.png',
            )
        ]

        self.__portrait_width__ = 200
        self.__portrait_height__ = 200
        self.__landscape_width__ = 200
        self.__landscape_height__ = 200


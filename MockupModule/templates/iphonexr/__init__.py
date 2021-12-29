from dataclasses import dataclass

from MockupModule.templates import templates_path, TemplateResolution, TemplateColor, Template


@dataclass
class Device(Template):
    def __post_init__(self):
        self.manufacturer = 'Apple'
        self.name = 'iPhone Xr'
        self.type = 'phone'
        self.year = 2018
        self.example_path = templates_path + '/iphonexr/example.png'
        self.portrait_resolution = TemplateResolution(width=828, height=1792)
        self.landscape_resolution = TemplateResolution(width=1792, height=828)

        self.colors = [
            TemplateColor(
                color='Blue',
                portrait_path=templates_path + '/iphonexr/blue/portrait.png',
                landscape_path=templates_path + '/iphonexr/blue/landscape.png',
            ),
            TemplateColor(
                color='Coral',
                portrait_path=templates_path + '/iphonexr/coral/portrait.png',
                landscape_path=templates_path + '/iphonexr/coral/landscape.png',
            ),
            TemplateColor(
                color='PRODUCT RED',
                portrait_path=templates_path + '/iphonexr/red/portrait.png',
                landscape_path=templates_path + '/iphonexr/red/landscape.png',
            ),
            TemplateColor(
                color='Silver',
                portrait_path=templates_path + '/iphonexr/silver/portrait.png',
                landscape_path=templates_path + '/iphonexr/silver/landscape.png',
            ),
            TemplateColor(
                color='Space Gray',
                portrait_path=templates_path + '/iphonexr/spacegray/portrait.png',
                landscape_path=templates_path + '/iphonexr/spacegray/landscape.png',
            ),
            TemplateColor(
                color='Yellow',
                portrait_path=templates_path + '/iphonexr/yellow/portrait.png',
                landscape_path=templates_path + '/iphonexr/yellow/landscape.png',
            )
        ]

        self.__portrait_width__ = 110
        self.__portrait_height__ = 110
        self.__landscape_width__ = 110
        self.__landscape_height__ = 110


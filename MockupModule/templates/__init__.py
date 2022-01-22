import os

from dataclasses import dataclass, field
from pathlib import Path
from typing import List

templates_path = os.path.join("/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1]), 'templates')


def __list_all_templates():
    all_templates = [x.name for x in Path(templates_path).iterdir()
                     if x.is_dir() and not str(x).startswith('__') and not str(x).endswith('__')]
    return all_templates


ALL_TEMPLATES = sorted(__list_all_templates())
__all__ = ALL_TEMPLATES + ["ALL_TEMPLATES"]


def default_factory_none() -> None:
    return None


def default_factory_false() -> bool:
    return False


@dataclass(frozen=False)
class TemplateColor:
    color: str = ''
    portrait_path: str = field(default_factory=str)
    landscape_path: str = field(default_factory=str)
    
    
@dataclass(frozen=False)
class Template:
    manufacturer: str = field(default_factory=str)
    name: str = field(default_factory=str)
    type: str = field(default_factory=str)
    year: int = field(default_factory=int)
    resolution: str = field(default_factory=str)
    example_path: str = field(default_factory=str)

    colors: List[TemplateColor] = field(default_factory=list)

    __template_path__: str = field(default_factory=str)
    __colors__: dict = field(default_factory=dict)

    __use_mask__: bool = field(default_factory=default_factory_false)

    __portrait_width__: int = field(default_factory=int)
    __portrait_height__: int = field(default_factory=int)
    __portrait_x__: int = field(default_factory=int)
    __portrait_y__: int = field(default_factory=int)
    __portrait_mask__: str = field(default_factory=default_factory_none)

    __landscape_width__: int = field(default_factory=int)
    __landscape_height__: int = field(default_factory=int)
    __landscape_x__: int = field(default_factory=int)
    __landscape_y__: int = field(default_factory=int)
    __landscape_mask__: str = field(default_factory=default_factory_none)

    def __post_init__(self):
        getattr(self, '__device_init__')()

        self.example_path = '{}/{}/example.png'.format(templates_path, self.__template_path__)

        self.colors = [
            TemplateColor(
                color=color,
                portrait_path='{}/{}/{}/portrait.png'.format(templates_path, self.__template_path__, color_path),
                landscape_path='{}/{}/{}/landscape.png'.format(templates_path, self.__template_path__, color_path),
            ) for color, color_path in self.__colors__.items()]

        if self.__use_mask__:
            self.__portrait_mask__ = '{}/{}/portrait-mask.png'.format(templates_path, self.__template_path__)
            self.__landscape_mask__ = '{}/{}/landscape-mask.png'.format(templates_path, self.__template_path__)

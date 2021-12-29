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


@dataclass(frozen=False)
class TemplateResolution:
    width: int = field(default_factory=int)
    height: int = field(default_factory=int)
    

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
    example_path: str = field(default_factory=str)
    portrait_resolution: TemplateResolution = field(default_factory=TemplateResolution)
    landscape_resolution: TemplateResolution = field(default_factory=TemplateResolution)

    colors: List[TemplateColor] = field(default_factory=list)

    __portrait_width__: int = field(default_factory=int)
    __portrait_height__: int = field(default_factory=int)
    __landscape_width__: int = field(default_factory=int)
    __landscape_height__: int = field(default_factory=int)

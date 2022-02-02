import hashlib
import os

from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

templates_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


def __list_all_templates__():
    all_templates = [x.name for x in Path(templates_path).iterdir()
                     if x.is_dir() and not str(x).startswith('__') and not str(x).endswith('__')]
    return all_templates


ALL_TEMPLATES = sorted(__list_all_templates__())
__all__ = ALL_TEMPLATES + ["ALL_TEMPLATES"]


@dataclass(frozen=False)
class DeviceColor:
    color: str
    path: str


@dataclass(frozen=False)
class DeviceImage:
    width: int
    height: int
    x: int
    y: int
    mask: bool
    mask_path: Optional[str]
    rotate: bool


@dataclass(frozen=False)
class Device:
    def __init__(self, path: str):
        config = ConfigParser()
        config.read(os.path.join(templates_path, path, 'config.ini'))

        self.id = hashlib.md5(str({s: dict(config.items(s)) for s in config.sections()}).encode()).hexdigest()
        self.manufacturer: str = str(config.get('info', 'manufacturer'))
        self.name: str = str(config.get('info', 'name'))
        self.type: str = str(config.get('info', 'type'))
        self.year: int = int(config.get('info', 'year'))
        self.width: int = int(config.get('info', 'width'))
        self.height: int = int(config.get('info', 'height'))
        self.resolution: str = '{width} x {height}'.format(
            width=self.width, height=self.height)
        self.preview: str = str(os.path.join(templates_path, path, 'preview.png'))

        self.colors = [DeviceColor(
            color=str(key).title(), path=str(os.path.join(templates_path, path, item))
        ) for key, item in config['colors'].items()]

        self.image = DeviceImage(
            width=int(config.get('image', 'width')),
            height=int(config.get('image', 'height')),
            x=int(config.get('image', 'x')),
            y=int(config.get('image', 'y')),
            mask=config.get('image', 'mask') == 'true',
            mask_path=os.path.join(templates_path, path, 'mask.png') if config.get('image', 'mask') == 'true' else None,
            rotate=config.get('image', 'rotate') == 'true')

    def __str__(self):
        return '<MockupEngineer.templates.Device {} {} {}>'.format(self.manufacturer, self.name, self.year)

    def __post_init__(self):
        self.colors = sorted(self.colors, key=lambda a: a.color)

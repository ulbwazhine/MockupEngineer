import hashlib
import os

from configparser import ConfigParser, NoOptionError, NoSectionError
from pydantic import BaseModel
from pathlib import Path
from typing import Optional, List

from MockupEngineer.utils.about import author, author_url

templates_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


def __list_all_templates__():
    all_templates = [x.name for x in Path(templates_path).iterdir()
                     if x.is_dir() and not str(x).startswith('__') and not str(x).endswith('__')]
    return all_templates


ALL_TEMPLATES = sorted(__list_all_templates__())
__all__ = ALL_TEMPLATES + ["ALL_TEMPLATES"]


class DeviceColor(BaseModel):
    color: str
    path: str


class DeviceImage(BaseModel):
    width: int
    height: int
    x: int
    y: int
    mask: bool
    mask_path: Optional[str]
    rotate: bool


class About(BaseModel):
    author: str
    url: str


class Device(BaseModel):
    id: str
    manufacturer: str
    name: str
    type: str
    year: int
    width: int
    height: int
    resolution: str
    preview: str
    colors: List[DeviceColor]
    image: DeviceImage
    about: About
    __path__: str


def write_config(path: str, config: ConfigParser) -> None:
    with open(os.path.join(templates_path, path, 'config.ini'), 'w', encoding='utf8') as f:
        config.write(f)


def get_author(path: str, config: ConfigParser) -> str:
    try:
        return config.get('about', 'author')
    except (NoOptionError, NoSectionError):
        if 'about' not in config.sections():
            config.add_section('about')
        config['about']['author'] = author()
        write_config(path, config)


def get_url(path, config: ConfigParser) -> str:
    try:
        return config.get('about', 'url')
    except (NoOptionError, NoSectionError):
        if 'about' not in config.sections():
            config.add_section('about')
        config['about']['url'] = author_url()
        write_config(path, config)


def parse_config(path: str) -> Device:
    kwargs = dict(__path__=path)

    config = ConfigParser()
    config.read(os.path.join(templates_path, path, 'config.ini'))

    if int(config.get('info', 'width')) < int(config.get('info', 'height')):
        height = config.get('info', 'width')
        width = config.get('info', 'height')
        config['info']['width'] = width
        config['info']['height'] = height
        write_config(path, config)

    kwargs['id']: str = hashlib.md5(str({s: dict(config.items(s)) for s in config.sections()}).encode()).hexdigest()
    kwargs['manufacturer']: str = str(config.get('info', 'manufacturer'))
    kwargs['name']: str = str(config.get('info', 'name'))
    kwargs['type']: str = str(config.get('info', 'type'))
    kwargs['year']: int = int(config.get('info', 'year'))
    kwargs['width']: int = int(config.get('info', 'width'))
    kwargs['height']: int = int(config.get('info', 'height'))
    kwargs['resolution']: str = '{width} x {height}'.format(
        width=kwargs['width'], height=kwargs['height'])
    kwargs['preview']: str = str(os.path.join(templates_path, path, 'preview.png'))

    kwargs['colors'] = sorted([DeviceColor(
        color=str(key).title(), path=str(os.path.join(templates_path, path, item))
    ) for key, item in config['colors'].items()], key=lambda a: a.color)

    kwargs['image'] = DeviceImage(
        width=int(config.get('image', 'width')),
        height=int(config.get('image', 'height')),
        x=int(config.get('image', 'x')),
        y=int(config.get('image', 'y')),
        mask=config.get('image', 'mask') == 'true',
        mask_path=os.path.join(templates_path, path, 'mask.png') if config.get('image', 'mask') == 'true' else None,
        rotate=config.get('image', 'rotate') == 'true')

    kwargs['about'] = About(
        author=get_author(path, config),
        url=get_url(path, config)
    )

    return Device(**kwargs)

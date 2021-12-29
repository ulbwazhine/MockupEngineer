import logging
import os
from importlib import import_module

from typing import List

from PIL import Image

from MockupModule import templates
from MockupModule.utils import random_string

generated_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generated')
if not os.path.exists(generated_path):
    os.makedirs(generated_path)


class MockupEngineer:
    def __init__(self):
        self.logger = logging.getLogger('MockupEngineer')
        self.templates: List[templates.Template] = []

        for template in templates.ALL_TEMPLATES:
            self.templates.append(getattr(
                import_module(name='MockupModule.templates.' + template,
                              package='MockupModule.templates.' + template + '.Device'), 'Device')())

    def screenshot_resize(self, screenshot: str, width: int, height: int) -> str:
        name = '{}/screenshot{}.png'.format(generated_path, random_string(16))
        img = Image.open(screenshot)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(name)

        return name

    def get_templates(self) -> dict:
        dicted = dict()
        for template in self.templates:
            if template.type in dicted.keys():
                dicted[template.type].append(template)
            else:
                dicted[template.type] = [template]
        return dicted

    def generate(self, template: templates.Template, screenshot: str, color: str = None, orientation: str = None):
        self.logger.info(
            'Generating: {}'.format(
                ', '.join(
                    [': '.join([str(a).upper(), str(b)]) for a, b in template.__dict__.items()])))

        if not orientation:
            img = Image.open(screenshot)
            width, height = img.size
            orientation = 'portrait' if height > width or height == width else 'landscape'

        if orientation == 'portrait':
            screen_width = template.portrait_resolution.width
            screen_height = template.portrait_resolution.height
            width_coordinate = template.__portrait_width__
            height_coordinate = template.__portrait_height__
        else:
            screen_width = template.landscape_resolution.width
            screen_height = template.landscape_resolution.height
            width_coordinate = template.__landscape_width__
            height_coordinate = template.__landscape_height__

        screenshot = self.screenshot_resize(screenshot, screen_width, screen_height)

        for template_color in template.colors:
            if template_color.color == color:
                template_path = template_color.portrait_path \
                    if orientation == 'portrait' else template_color.landscape_path
                break
        else:
            template_path = template.colors[-1].portrait_path \
                if orientation == 'portrait' else template.colors[-1].landscape_path

        name = '{}/mockup{}.png'.format(generated_path, random_string(16))

        template_img = Image.open(template_path)
        mask_img = Image.new('RGBA', template_img.size, (0, 0, 0, 0))
        screenshot_img = Image.open(screenshot)
        mask_img.paste(screenshot_img, (width_coordinate, height_coordinate))
        mask_img.paste(template_img, (0, 0), template_img)

        mask_img.save(name)

        return name

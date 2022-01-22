import logging
import os
from importlib import import_module

from typing import List

from PIL import Image, ImageChops

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
        img = Image.open(screenshot).resize((width, height), Image.ANTIALIAS)
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
        if not orientation:
            img = Image.open(screenshot)
            width, height = img.size
            orientation = 'portrait' if height > width or height == width else 'landscape'

        if orientation == 'portrait':
            screen_width = template.__portrait_width__
            screen_height = template.__portrait_height__
            screen_x = template.__portrait_x__
            screen_y = template.__portrait_y__
            screen_mask = template.__portrait_mask__ if template.__use_mask__ else None
        else:
            screen_width = template.__landscape_width__
            screen_height = template.__landscape_height__
            screen_x = template.__landscape_x__
            screen_y = template.__landscape_y__
            screen_mask = template.__landscape_mask__ if template.__use_mask__ else None

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
        mask_img.paste(screenshot_img, (screen_x, screen_y))
        mask_img.paste(template_img, (0, 0), template_img)

        if screen_mask:
            screen_mask = Image.open(screen_mask).convert('L')
            mask_img.putalpha(screen_mask)
        mask_img.save(name)

        return name

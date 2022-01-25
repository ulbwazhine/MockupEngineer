import logging
import os

from TemporaryStorage import TemporaryStorageInstance
from importlib import import_module
from typing import List
from PIL import Image

from MockupEngineer import templates
from MockupEngineer.utils import random_string

generated_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generated')
if not os.path.exists(generated_path):
    os.makedirs(generated_path)


class MockupEngineerInstance:
    def __init__(self):
        self.logger = logging.getLogger('MockupEngineer')
        self.templates: List[templates.Template] = []
        self.storage = TemporaryStorageInstance()

        for template in templates.ALL_TEMPLATES:
            self.templates.append(getattr(
                import_module(name='MockupEngineer.templates.' + template,
                              package='MockupEngineer.templates.' + template + '.Device'), 'Device')())

    def __create_mockups_list__(self) -> str:
        output = list()
        available_templates = self.get_templates()
        specified_keys = {"pc": 'Computers',
                          'wear': 'Wearable devices'}

        for key, item in available_templates.items():
            output.append(
                '### {}'.format('{}s'.format(key.title()) if key not in specified_keys.keys() else specified_keys[key]))

            for template in item:
                output.append(
                    '* [{manufacturer} {name}](https://raw.githubusercontent.com/'
                    'ulbwazhine/MockupEngineer/main/MockupEngineer/'
                    'templates/{path}/example.png) [{resolution}] ({year})'.format(
                        manufacturer=template.manufacturer, name=template.name,
                        path=template.__template_path__, resolution=template.resolution,
                        year=template.year))

                for color in sorted(template.colors, key=lambda a: a.color):
                    output.append('  * {}'.format(color.color))

                output.append('')

        return '\n'.join(output)

    def __create_examples__(self, example_path: str) -> None:
        for template in self.templates:
            if os.path.isfile(template.example_path):
                os.remove(template.example_path)

            mockup_path = self.generate(template, example_path, orientation='portrait')
            mockup_img = Image.open(mockup_path)
            background_img = Image.new('RGBA', mockup_img.size, (255, 255, 255, 255))
            background_img.paste(mockup_img, (0, 0), mockup_img)

            background_img.save(template.example_path)

            os.remove(mockup_path)

    @staticmethod
    def resize(image: str, width: int, height: int) -> str:
        name = '{}/image{}.png'.format(generated_path, random_string(16))
        img = Image.open(image).resize((width, height), Image.ANTIALIAS)
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

    def generate(self, template: templates.Template,
                 screenshot_path: str, color: str = None,
                 orientation: str = None, external_storage: bool = False) -> str:
        if not orientation:
            img = Image.open(screenshot_path)
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

        resized_screenshot_path = self.resize(screenshot_path, screen_width, screen_height)

        for template_color in template.colors:
            if template_color.color == color:
                template_path = template_color.portrait_path \
                    if orientation == 'portrait' else template_color.landscape_path
                break
        else:
            template_path = template.colors[-1].portrait_path \
                if orientation == 'portrait' else template.colors[-1].landscape_path

        mockup_path = '{}/mockup{}.png'.format(generated_path, random_string(16))

        template_img = Image.open(template_path)
        mask_img = Image.new('RGBA', template_img.size, (0, 0, 0, 0))
        screenshot_img = Image.open(resized_screenshot_path)
        mask_img.paste(screenshot_img, (screen_x, screen_y))
        mask_img.paste(template_img, (0, 0), template_img)

        if screen_mask:
            screen_mask = Image.open(screen_mask).convert('L')
            mask_img.putalpha(screen_mask)
        mask_img.save(mockup_path)

        os.remove(resized_screenshot_path)

        if not external_storage:
            return mockup_path
        else:
            uploaded = self.storage.upload(mockup_path)

            if uploaded and uploaded.url:
                os.remove(mockup_path)
                return uploaded.url
            else:
                return mockup_path

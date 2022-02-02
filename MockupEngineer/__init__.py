import logging
import os

from TemporaryStorage import TemporaryStorageInstance
from typing import List, Optional
from PIL import Image

from MockupEngineer import templates
from MockupEngineer.templates import Device, ALL_TEMPLATES
from MockupEngineer.utils import random_string

generated_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generated')
if not os.path.exists(generated_path):
    os.makedirs(generated_path)


class MockupEngineerInstance:
    def __init__(self):
        self.logger = logging.getLogger('MockupEngineer')
        self.templates: List[Device] = []
        self.storage = TemporaryStorageInstance()

        for template in ALL_TEMPLATES:
            try:
                self.templates.append(Device(template))
            except Exception as e:
                self.logger.warning('Failed to load "{}" module: {}'.format(template, e))

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
                        path=os.path.basename(os.path.dirname(template.preview)),
                        resolution=template.resolution, year=template.year))

                for color in sorted(template.colors, key=lambda a: a.color):
                    output.append('  * {}'.format(color.color))

                output.append('')

        return '\n'.join(output)

    def __create_examples__(self, example_path: str) -> None:
        for template in self.templates:
            if os.path.isfile(template.preview):
                os.remove(template.preview)

            mockup_path = self.generate(template.id, example_path)
            mockup_img = Image.open(mockup_path)
            background_img = Image.new('RGBA', mockup_img.size, (255, 255, 255, 255))
            background_img.paste(mockup_img, (0, 0), mockup_img)

            background_img.save(template.preview)

            os.remove(mockup_path)

    def get_template(self, template_id: str) -> Optional[Device]:
        for template in self.templates:
            if template.id == template_id:
                return template

    def get_templates(self) -> dict:
        dicted = dict()
        for template in self.templates:
            if template.type in dicted.keys():
                dicted[template.type].append(template)
            else:
                dicted[template.type] = [template]
        return dicted

    def generate(self, template_id: str,
                 screenshot_path: str,
                 color: str = None,
                 orientation: str = None,
                 external_storage: bool = False) -> str:
        template = self.get_template(template_id)

        if not template:
            raise ModuleNotFoundError('Module with id {} not found.'.format(template_id))

        for template_color in template.colors:
            if template_color.color == color:
                color = template_color
                break
        else:
            color = template.colors[0]

        template_image = Image.open(color.path).convert("RGBA")
        screenshot_image = Image.open(screenshot_path).convert("RGBA")
        placeholder_image = Image.new('RGBA', template_image.size, (0, 0, 0, 0))

        screenshot_orientation = (
            'portrait' if screenshot_image.size[0] <= screenshot_image.size[1] else 'landscape'
        ) if not orientation else orientation

        template_orientation = (
            'portrait' if template.image.width <= template.image.height else 'landscape'
        )

        if screenshot_orientation != template_orientation and template.image.rotate:
            screenshot_image = screenshot_image.rotate(-90, expand=True)

        screenshot_image = screenshot_image.resize((template.image.width, template.image.height), Image.ANTIALIAS)

        placeholder_image.paste(screenshot_image, (template.image.x, template.image.y))
        placeholder_image.paste(template_image, (0, 0), template_image)

        if template.image.mask:
            mask_image = Image.open(template.image.mask_path).convert('L')
            placeholder_image.putalpha(mask_image)

        if screenshot_orientation != template_orientation and template.image.rotate:
            placeholder_image = placeholder_image.rotate(90, expand=True)

        mockup_path = os.path.join(generated_path, 'mockup-{}.png'.format(random_string(16)))
        placeholder_image.save(mockup_path)

        if not external_storage:
            return mockup_path
        else:
            uploaded = self.storage.upload(mockup_path)

            if uploaded and uploaded.url:
                os.remove(mockup_path)
                return uploaded.url
            else:
                return mockup_path

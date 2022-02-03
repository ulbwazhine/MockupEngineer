import datetime
import os
import shutil

from FluentGenerator import FluentImage
from PIL import Image
from jinja2 import Template

from MockupEngineer import MockupEngineerInstance, generated_path


def create_examples():
    mockup = MockupEngineerInstance()

    max_size = 1000

    for template in mockup.templates:
        screenshot_path = FluentImage(
            colors=10, width=template.image.width, height=template.image.height, background='white').generate()
        mockup_path = mockup.generate(template_id=template.id, screenshot_path=screenshot_path)
        os.remove(screenshot_path)
        shutil.move(mockup_path, template.preview)

        mockup_img = Image.open(template.preview)
        background_img = Image.new('RGBA', mockup_img.size, (255, 255, 255, 255))
        background_img.paste(mockup_img, (0, 0), mockup_img)

        if background_img.size[0] > max_size or background_img.size[1] > max_size:
            if background_img.size[0] > background_img.size[1]:
                width = max_size
                height = int(background_img.size[1] * (max_size / background_img.size[0]))
            else:
                width = int(background_img.size[0] * (max_size / background_img.size[1]))
                height = max_size

            background_img = background_img.resize((width, height), Image.ANTIALIAS)
        background_img.save(template.preview)

    shutil.rmtree(generated_path)


def create_readme():
    mockup = MockupEngineerInstance()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'readme-template.md'), 'r') as f:
        data = Template(f.read()).render(templates=mockup.get_templates(), os=os,
                                         specified_keys={"pc": 'Computers',
                                                         'wear': 'Wearable devices'})

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'readme.md'), 'w') as f:
        f.write(data)


def bump_version():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup.py'), 'r') as f:
        data = f.read()

        setup_version = data.split('version=\'')[1].split('\',')[0]
        setup_date = datetime.datetime.strptime(".".join(setup_version.split('.')[:-1]), '%Y.%m.%d')
        setup_variant = int(setup_version.split('.')[-1])
        current_date = datetime.datetime.utcnow()
        setup_variant = 1 if (current_date.day > setup_date.day or
                              current_date.month > setup_date.month or
                              current_date.year > setup_date.year) else setup_variant + 1
        setup_date = current_date.strftime('%Y.%m.%d')
        bumped = data.replace(setup_version, '{}.{}'.format(setup_date, setup_variant))

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup.py'), 'w') as f:
        f.write(bumped)


def run_pypi():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system("python3 setup.py sdist")
    os.system("twine upload dist/*")
    os.system("rm -rf \"dist\"")
    os.system("rm -rf \"MockupEngineer.egg-info\"")


if __name__ == '__main__':
    create_readme()
    create_examples()
    bump_version()
    run_pypi()

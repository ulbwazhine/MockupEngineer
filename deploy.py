import datetime
import os
import shutil

from FluentGenerator import FluentImage
from jinja2 import Template

from MockupEngineer import MockupEngineerInstance, generated_path


def create_examples():
    mockup = MockupEngineerInstance()

    for template in mockup.templates:
        screenshot = FluentImage(
            colors=10, width=template.image.width, height=template.image.height, background='white').generate()
        mockuped = mockup.generate(template_id=template.id, screenshot_path=screenshot)
        os.remove(screenshot)
        shutil.move(mockuped, template.preview)

    os.removedirs(generated_path)


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

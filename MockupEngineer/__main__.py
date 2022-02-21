import os
import webbrowser

from MockupEngineer import MockupEngineerInstance, Device


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Main:
    def __init__(self):
        print('Loading modules...')
        self.mockup = MockupEngineerInstance()
        cls()
        self.select_category()

    def exit(self):
        cls()
        exit()

    def input(self, placeholder: str, func, args=()):
        cls()
        return func(input(placeholder), *args)

    def menu(self, **variants):
        variants = {a.replace('var', ''): b for a, b in variants.items()}
        for a, (b, _, _) in variants.items():
            print('    [{}] {}'.format(a, b))
        val = input('Enter value: ')
        if val not in variants:
            cls()
            print('Invalid value, try again:')
            return self.menu(**variants)
        else:
            variants[val][1](*variants[val][2])

    def select_category(self):
        cls()
        print('Select device category:')
        self.menu(**{str(num + 1): (a['title'], self.select_template, (b,)) for num, (b, a) in
                     enumerate(self.mockup.get_templates().items())},
                  var0=('Exit', self.exit, ()))

    def select_template(self, category: str):
        cls()
        print('Choose a device:')
        self.menu(**{str(num + 1): (
            '{} {} ({}) [{}]'.format(a.manufacturer, a.name, a.resolution, a.year), self.select_color, (a.id,)) for
            num, a
            in enumerate(self.mockup.get_templates()[category]['templates'])},
                  var0=('Back', self.select_category, ()))

    def select_color(self, template_id):
        cls()
        print('Choose color:')
        template = self.mockup.get_template(template_id)
        self.menu(
            **{str(num + 1): (a.color, self.enter_path, (a.color, template)) for num, a in enumerate(template.colors)},
            var0=('Back', self.select_template, (template.type,)))

    def enter_path(self, color: str, template: Device):
        self.input('Enter the path to the screenshot: ', self.generate, (color, template))

    def generate(self, path: str, color: str, template: Device):
        if not os.path.isfile(path):
            return self.input('File does not exist, try again: ', self.generate, (color, template))
        if not (path.lower().endswith('.png') or path.lower().endswith('.jpg') or path.lower().endswith('.jpeg')):
            return self.input('MockupEngineer supports .png and .jpeg screenshots, try again: ', self.generate,
                              (color, template))
        cls()
        print('Generating...')
        url = self.mockup.generate(screenshot_path=path, template_id=template.id, color=color, external_storage=True)
        cls()
        print('Success: {}'.format(url))
        webbrowser.open(url)
        self.menu(var1=('Back', self.select_category, ()),
                  var0=('Exit', self.exit, ()))


if __name__ == '__main__':
    Main()

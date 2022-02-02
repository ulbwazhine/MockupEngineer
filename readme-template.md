<div align="center">
  <h1>MockupEngineer</h1>
  <p>
    <img src="https://img.shields.io/pypi/dm/MockupEngineer">
    <img src="https://img.shields.io/pypi/v/MockupEngineer?label=version">
    <img src="https://img.shields.io/pypi/l/MockupEngineer">
    <img src="https://img.shields.io/github/repo-size/ulbwazhine/MockupEngineer">
  </p>
  <p>A simple library for creating beautiful screenshots.</p>
</div>

## Navigation
* [Example](https://github.com/ulbwazhine/MockupEngineer#example)
* [Install](https://github.com/ulbwazhine/MockupEngineer#install)
  * [Update](https://github.com/ulbwazhine/MockupEngineer#update)
* [Usage](https://github.com/ulbwazhine/MockupEngineer#usage)
  * [As a standalone application](https://github.com/ulbwazhine/MockupEngineer#as-a-standalone-application)
  * [In Python console](https://github.com/ulbwazhine/MockupEngineer#in-python-console)
  * [MockupEngineerInstance.generate parameters](https://github.com/ulbwazhine/MockupEngineer#mockupengineerinstancegenerate-parameters)
* [List of supported mockups](https://github.com/ulbwazhine/MockupEngineer#list-of-supported-mockups)
  * [Phones](https://github.com/ulbwazhine/MockupEngineer#phones)
  * [Tablets](https://github.com/ulbwazhine/MockupEngineer#tablets)
  * [Computers](https://github.com/ulbwazhine/MockupEngineer#computers)
  * [Wearable devices](https://github.com/ulbwazhine/MockupEngineer#wearable-devices)
* [Links](https://github.com/ulbwazhine/MockupEngineer#links)

## Example

<div align="center">
  <img width="375px" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12promax/example.png" alt="Apple iPhone 12 Pro Max Mockup">
  <p>Apple iPhone 12 Pro Max Mockup</p>
</div>

## Install
```console
$ python3 -m pip install MockupEngineer
```

### Update
```console
$ python3 -m pip install MockupEngineer --upgrade
```

## Usage

#### As a standalone application:
```console
$ python3 -m MockupEngineer
```

<div align="center">
  <img width="70%" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/console_example.jpeg" alt="">
</div>

#### In Python console:

```python
from MockupEngineer import MockupEngineerInstance

mockup = MockupEngineerInstance()

mockup.generate(template=mockup.templates[0],
                screenshot_path='/path/to/screenshot',
                color=mockup.templates[0].colors[0].color)
```

```console
>>> /path/to/mockup
```

#### `MockupEngineerInstance.generate` parameters:
   * `template`: *Template* — Device template model, must be passed from *MockupEngineerInstance.templates* or *MockupEngineerInstance.get_templates()*.
   * `screenshot_path`: *str* — Absolute path to the image in **JPG, PNG format**.
   * `color`: *Optional[str]* — Optional parameter, force device color. Must be passed according to *Template.colors[**n**].color*
   * `orientation`: *str* — Optional parameter, force device orientation. Must be *landscape* or *portrait*.
   * `external_storage`: *Optional[bool]* — Optional parameter, true if you need to upload mockup on [TemporaryStorage](https://github.com/ulbwazhine/TemporaryStorage) (0x0.st etc)

## List of supported mockups

Full list of all currently supported mockups
{% for a, b in templates.items() %}
### {{'{}s'.format(a.title()) if a not in specified_keys.keys() else specified_keys[a]}}
{% for c in b %}
* [{{c.manufacturer}} {{c.name}}](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/{{os.path.basename(os.path.dirname(c.preview))}}/preview.png) ({{c.year}}) [{{c.resolution}}] 
{% for d in c.colors %}  * *{{d.color}}*
{% endfor %}{% endfor %}{% endfor %}
You can help the project by adding support for new mockups by contributing on [GitHub](https://github.com/ulbwazhine/MockupEngineer).

## Links
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/author.svg" height="30"/>](https://ulbwa.github.io)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/github.svg" height="30"/>](https://github.com/ulbwazhine/MockupEngineer)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/pypi.svg" height="30"/>](https://pypi.org/project/MockupEngineer)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/donate.svg" height="30"/>](https://ulbwa.github.io/go?to=donate)
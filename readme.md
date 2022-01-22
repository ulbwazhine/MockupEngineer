<div align="center">
  <h1>MockupEngineer</h1>
  <p>An simple library for creating beautiful screenshots.</p>
</div>

## Example

<img align="center" width="350" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12promax/example.png" alt="Apple iPhone 12 Pro Max">


## Install
```
$ python -m pip install MockupEngineer
```

## Usage

In Python console:
```python
from MockupModule import MockupEngineer

mockup = MockupEngineer()

mockup.generate(template=mockup.templates[0], 
                screenshot_path='/path/to/screenshot',
                color=mockup.templates[0].colors[0].color)
```

```
>>> /path/to/mockup
```

As a standalone application:
```
$ python -m MockupModule
```

## Links
* [Author](https://t.me/ulbwa)
* [GitHub](https://github.com/ulbwazhine/MockupEngineer)
* [PyPI](https://pypi.org/project/MockupEngineer/)


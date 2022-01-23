<div align="center">
  <h1>MockupEngineer</h1>
  <p>
    <img src="https://img.shields.io/pypi/dm/MockupEngineer">
    <img src="https://img.shields.io/pypi/v/MockupEngineer?label=version">
    <img src="https://img.shields.io/pypi/l/MockupEngineer">
    <img src="https://img.shields.io/github/repo-size/ulbwazhine/MockupEngineer">
  </p>
  <p>An simple library for creating beautiful screenshots.</p>
</div>

## Navigation
* [Example](https://github.com/ulbwazhine/MockupEngineer#example)
* [Install](https://github.com/ulbwazhine/MockupEngineer#install)
* [Usage](https://github.com/ulbwazhine/MockupEngineer#usage)
  * [In Python console](https://github.com/ulbwazhine/MockupEngineer#in-python-console)
  * [As a standalone application](https://github.com/ulbwazhine/MockupEngineer#as-a-standalone-application)
* [List of supported mockups](https://github.com/ulbwazhine/MockupEngineer#list-of-supported-mockups)
  * [Phones](https://github.com/ulbwazhine/MockupEngineer#phones)
  * [Tablets](https://github.com/ulbwazhine/MockupEngineer#tablets)
  * [Computers](https://github.com/ulbwazhine/MockupEngineer#computers)
  * [Wearable devices](https://github.com/ulbwazhine/MockupEngineer#wearable-devices)
* [Links](https://github.com/ulbwazhine/MockupEngineer#links)

## Example

<div align="center">
  <img align="center" width="350" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12promax/example.png" alt="Apple iPhone 12 Pro Max Mockup">
  <p>Apple iPhone 12 Pro Max Mockup</p>
</div>

## Install
```
$ python -m pip install MockupEngineer
```

## Usage

#### In Python console:
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

#### As a standalone application:
```
$ python -m MockupModule
```

## List of supported mockups

Full list of all currently supported mockups

### Phones
* [Samsung Galaxy S20](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/galaxys20/example.png) [1440 x 3200] (2020)
  * Cloud Blue
  * Cosmic Grey
  * Pink

* [Samsung Galaxy S20 Ultra](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/galaxys20/example.png) [1440 x 3200] (2020)
  * Cosmic Black
  * Cosmic Grey

* [Apple iPhone 12](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12/example.png) [1170 x 2532] (2020)
  * Black
  * Blue
  * Green
  * PRODUCT RED
  * White

* [Apple iPhone 12 Mini](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12mini/example.png) [1080 x 2340] (2020)
  * Black
  * Blue
  * Green
  * PRODUCT RED
  * White

* [Apple iPhone 12 Pro](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12pro/example.png) [1170 x 2532] (2020)
  * Gold
  * Graphite
  * Pacific Blue
  * Silver

* [Apple iPhone 12 Pro Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12promax/example.png) [1284 x 2778] (2020)
  * Gold
  * Graphite
  * Pacific Blue
  * Silver

* [Apple iPhone SE](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphonese2020/example.png) [750 x 1334] (2020)
  * Black
  * PRODUCT RED
  * White

* [Apple iPhone Xr](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphonexr/example.png) [828 x 1792] (2018)
  * Blue
  * Coral
  * PRODUCT RED
  * Silver
  * Space Gray
  * Yellow

* [Google Pixel](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/pixel/example.png) [1080 x 1920] (2016)
  * Quite Black
  * Really Blue
  * Very Silver

* [Google Pixel 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/pixel4/example.png) [1080 x 2280] (2019)
  * Clearly White
  * Just Black
  * Oh So Orange

* [Google Pixel 4 XL](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/pixel4xl/example.png) [1440 x 3040] (2019)
  * Clearly White
  * Just Black
  * Oh So Orange

* [Google Pixel 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/pixel5/example.png) [1080 x 2340] (2020)
  * Just Black
  * Sorta Sage

### Tablets
* [Apple iPad 9](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/ipad9/example.png) [2160 x 1620] (2021)
  * Gold
  * Silver
  * Space Gray

* [Apple iPad Air 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/ipadair4/example.png) [2360 x 1640] (2020)
  * Green
  * Rose Gold
  * Silver
  * Sky Blue
  * Space Gray

* [Apple iPad Mini 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/ipadmini5/example.png) [2048 x 1536] (2021)
  * Gold
  * Silver
  * Space Gray

* [Apple iPad Pro 4 11"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/ipadpro114/example.png) [2388 x 1668] (2020)
  * Silver
  * Space Gray

* [Apple iPad Pro 4 12.9"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/ipadpro134/example.png) [2732 x 2048] (2020)
  * Silver
  * Space Gray

### Computers
* [Apple MacBook 12"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/macbook122016/example.png) [2304 x 1440] (2016)
  * Gold
  * Space Gray

### Wearable devices
* [Apple Watch Series 6 44mm](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/watchseries644mm/example.png) [368 x 448] (2020)
  * Aluminum Case - Blue
  * Aluminum Case - Gold
  * Aluminum Case - PRODUCT RED
  * Aluminum Case - Silver
  * Aluminum Case - Space Gray
  * Stainless Steel Case - Gold
  * Stainless Steel Case - Graphite
  * Stainless Steel Case - Silver
  * Titanium Case - Dark
  * Titanium Case - Light

You can help the project by adding support for new mockups by contributing on [GitHub](https://github.com/ulbwazhine/MockupEngineer).

## Links
* [Author](https://ulbwa.github.io)
* [GitHub](https://github.com/ulbwazhine/MockupEngineer)
* [PyPI](https://pypi.org/project/MockupEngineer/)
* [Donate](https://ulbwa.github.io/go?to=donate)


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

### Phones

* [Samsung Galaxy S20](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/galaxys20/preview.png) (2020) [1440 x 3200] 
  * *Cloud Blue*
  * *Cosmic Grey*
  * *Pink*

* [Samsung Galaxy S20 Ultra](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/galaxys20ultra/preview.png) (2020) [1440 x 3200] 
  * *Cosmic Black*
  * *Cosmic Grey*

* [Apple iPhone 12](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12/preview.png) (2020) [1170 x 2532] 
  * *Black*
  * *Blue*
  * *Green*
  * *Product Red*
  * *White*

* [Apple iPhone 12 Mini](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12mini/preview.png) (2020) [1080 x 2340] 
  * *Black*
  * *Blue*
  * *Green*
  * *Product Red*
  * *White*

* [Apple iPhone 12 Pro](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12pro/preview.png) (2020) [1170 x 2532] 
  * *Gold*
  * *Graphite*
  * *Pacific Blue*
  * *Silver*

* [Apple iPhone 12 Pro Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12promax/preview.png) (2020) [1284 x 2778] 
  * *Gold*
  * *Graphite*
  * *Pacific Blue*
  * *Silver*

* [Apple iPhone SE](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonese2020/preview.png) (2020) [750 x 1334] 
  * *Black*
  * *Product Red*
  * *White*

* [Apple iPhone Xr](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexr/preview.png) (2018) [828 x 1792] 
  * *Blue*
  * *Coral*
  * *Product Red*
  * *Silver*
  * *Space Gray*
  * *Yellow*

* [Apple iPhone Xs](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexs/preview.png) (2019) [1125 x 2436] 
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Apple iPhone Xs Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexsmax/preview.png) (2019) [1242 x 2688] 
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Google Pixel](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel/preview.png) (2016) [1080 x 1920] 
  * *Quite Black*
  * *Really Blue*
  * *Very Silver*

* [Google Pixel 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel4/preview.png) (2019) [1080 x 2280] 
  * *Just Black*
  * *Clearly White*
  * *Oh So Orange*

* [Google Pixel 4 XL](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel4xl/preview.png) (2019) [1440 x 3040] 
  * *Just Black*
  * *Clearly White*
  * *Oh So Orange*

* [Google Pixel 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel5/preview.png) (2020) [1080 x 2340] 
  * *Just Black*
  * *Sorta Sage*

### Computers

* [Apple iMac 21"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/imac212015/preview.png) (2015) [4096 x 2304] 
  * *Silver*

* [Apple MacBook 12"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbook122016/preview.png) (2016) [2304 x 1440] 
  * *Space Gray*
  * *Gold*

* [Apple MacBook Pro 13"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro132015/preview.png) (2015) [2560 x 1600] 
  * *Silver*

* [Apple MacBook Pro 15"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro152015/preview.png) (2015) [2880 x 1800] 
  * *Silver*

* [Apple MacBook Pro 16"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro162019/preview.png) (2019) [3072 x 1920] 
  * *Space Gray*

* [Apple MacBook Pro 16"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro162021/preview.png) (2021) [3456 x 2234] 
  * *Silver*
  * *Space Gray*

* [Google Pixelbook Go](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixelbookgo/preview.png) (2019) [1920 x 1080] 
  * *Just Black*

* [Apple Pro Display XDR](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/prodisplayxdr/preview.png) (2019) [6016 x 3384] 
  * *Silver*

### Tablets

* [Apple iPad 9](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipad9/preview.png) (2021) [2160 x 1620] 
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Apple iPad Air 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadair4/preview.png) (2020) [2360 x 1640] 
  * *Green*
  * *Rose Gold*
  * *Silver*
  * *Sky Blue*
  * *Space Gray*

* [Apple iPad Mini 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadmini5/preview.png) (2021) [2048 x 1536] 
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Apple iPad Pro 4 11"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadpro114/preview.png) (2020) [2388 x 1668] 
  * *Silver*
  * *Space Gray*

* [Apple iPad Pro 4 12.9"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadpro134/preview.png) (2020) [2732 x 2048] 
  * *Silver*
  * *Space Gray*

### Wearable devices

* [Apple Watch Series 6 44mm](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/watchseries644mm/preview.png) (2020) [368 x 448] 
  * *Aluminum Case - Blue*
  * *Aluminum Case - Gold*
  * *Aluminum Case - Space Gray*
  * *Aluminum Case - Silver*
  * *Aluminum Case - Product Red*
  * *Titanium Case - Light*
  * *Titanium Case - Dark*
  * *Stainless Steel Case - Gold*
  * *Stainless Steel Case - Graphite*
  * *Stainless Steel Case - Silver*

You can help the project by adding support for new mockups by contributing on [GitHub](https://github.com/ulbwazhine/MockupEngineer).

## Links
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/author.svg" height="30"/>](https://ulbwa.github.io)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/github.svg" height="30"/>](https://github.com/ulbwazhine/MockupEngineer)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/pypi.svg" height="30"/>](https://pypi.org/project/MockupEngineer)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/donate.svg" height="30"/>](https://ulbwa.github.io/go?to=donate)
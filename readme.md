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
  <img width="375px" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12promax/preview.png" alt="Apple iPhone 12 Pro Max Mockup">
  <p>Apple iPhone 12 Pro Max Mockup</p>
</div>

### Notice
The quality of all examples is much worse than real mockups, this is due to the project size limit on PyPI.

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
  <img width="70%" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/console_example.png" alt="Usage as a standalone application">
</div>

#### In Python console:

```python
from MockupEngineer import MockupEngineerInstance

mockup = MockupEngineerInstance()

mockup.generate(template_id=mockup.templates[0].id,
                screenshot_path='/path/to/screenshot',
                color=mockup.templates[0].colors[0].color)
```

```console
>>> /path/to/mockup
```

#### `MockupEngineerInstance.generate` parameters:
   * `template_id`: *int* — Device template id, must be passed from *MockupEngineerInstance.templates* or *MockupEngineerInstance.get_templates()*.
   * `screenshot_path`: *str* — Absolute path to the image in **JPG, PNG format**.
   * `color`: *Optional[str]* — Optional parameter, force device color. Must be passed according to *Template.colors[**n**].color*.
   * `orientation`: *str* — Optional parameter, force device orientation. Must be *landscape* or *portrait*.
   * `external_storage`: *Optional[bool]* — Optional parameter, true if you need to upload mockup on [TemporaryStorage](https://github.com/ulbwazhine/TemporaryStorage) (0x0.st etc)

## List of supported mockups

Full list of all currently supported mockups

### Phones

* [Samsung Galaxy S20](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/galaxys20/preview.png) (2020) [1440 x 3200]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `84b30848f1af25c9a3bff6583bbbe75a`
  * Colors:
  * * *Cloud Blue*
  * * *Cosmic Grey*
  * * *Pink*

* [Samsung Galaxy S20 Ultra](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/galaxys20ultra/preview.png) (2020) [1440 x 3200]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `c4168e005483c3579bef74898a4b0384`
  * Colors:
  * * *Cosmic Black*
  * * *Cosmic Grey*

* [Apple iPhone 12](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12/preview.png) (2020) [1170 x 2532]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `1648990cfee89db1d6cb744c998e783a`
  * Colors:
  * * *Black*
  * * *Blue*
  * * *Green*
  * * *Product Red*
  * * *White*

* [Apple iPhone 12 Mini](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12mini/preview.png) (2020) [1080 x 2340]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `aea792f252c0ba0847741c0a4a6dd3ca`
  * Colors:
  * * *Black*
  * * *Blue*
  * * *Green*
  * * *Product Red*
  * * *White*

* [Apple iPhone 12 Pro](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12pro/preview.png) (2020) [1170 x 2532]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `b25e4e76e2083e389761d3495a347e58`
  * Colors:
  * * *Gold*
  * * *Graphite*
  * * *Pacific Blue*
  * * *Silver*

* [Apple iPhone 12 Pro Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12promax/preview.png) (2020) [1284 x 2778]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `658c22b16917a70e5e1703f300ef98fe`
  * Colors:
  * * *Gold*
  * * *Graphite*
  * * *Pacific Blue*
  * * *Silver*

* [Apple iPhone 13](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13/preview.png) (2021) [1170 x 2532]   
  * Author: [@ulbwa](https://ulbwa.xyz) [19.02.2022]
  * ID: `e03132ca8b4b0483e9d8f4a1ec1be1f5`
  * Colors:
  * * *Blue*
  * * *Midnight*
  * * *Pink*
  * * *Product Red*
  * * *Starlight*

* [Apple iPhone 13 Mini](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13mini/preview.png) (2021) [1080 x 2340]   
  * Author: [@ulbwa](https://ulbwa.xyz) [19.02.2022]
  * ID: `d0346fb29c4c3de9ff70953a7ae3bfee`
  * Colors:
  * * *Blue*
  * * *Midnight*
  * * *Pink*
  * * *Product Red*
  * * *Starlight*

* [Apple iPhone 13 Pro](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13pro/preview.png) (2021) [1170 x 2532]   
  * Author: [@ulbwa](https://ulbwa.xyz) [19.02.2022]
  * ID: `1c6f40f0490c7e0cf35de1c96af5c720`
  * Colors:
  * * *Gold*
  * * *Graphite*
  * * *Sierra Blue*
  * * *Silver*

* [Apple iPhone 13 Pro Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13promax/preview.png) (2021) [1284 x 2778]   
  * Author: [@ulbwa](https://ulbwa.xyz) [19.02.2022]
  * ID: `edc57edf104fdba42fdf935986b09ab8`
  * Colors:
  * * *Gold*
  * * *Graphite*
  * * *Sierra Blue*
  * * *Silver*

* [Apple iPhone SE](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonese2020/preview.png) (2020) [750 x 1334]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `7ed0bde8cf28335afb6bf7e8fc90806b`
  * Colors:
  * * *Black*
  * * *Product Red*
  * * *White*

* [Apple iPhone Xr](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexr/preview.png) (2018) [828 x 1792]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `5213bfd57a03c81ad4dc702952810ee6`
  * Colors:
  * * *Blue*
  * * *Coral*
  * * *Product Red*
  * * *Silver*
  * * *Space Gray*
  * * *Yellow*

* [Apple iPhone Xs](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexs/preview.png) (2019) [1125 x 2436]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `4b17c9428565db596f647b448656b744`
  * Colors:
  * * *Gold*
  * * *Silver*
  * * *Space Gray*

* [Apple iPhone Xs Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexsmax/preview.png) (2019) [1242 x 2688]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `2c9c1c6b8c0b598fe1c1aca4c1f334f8`
  * Colors:
  * * *Gold*
  * * *Silver*
  * * *Space Gray*

* [Google Pixel](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel/preview.png) (2016) [1080 x 1920]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `ede34489f377fcc7852a326dd79c2550`
  * Colors:
  * * *Quite Black*
  * * *Really Blue*
  * * *Very Silver*

* [Google Pixel 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel4/preview.png) (2019) [1080 x 2280]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `673398cd2adaadd60506fb0140b83ab9`
  * Colors:
  * * *Just Black*
  * * *Clearly White*
  * * *Oh So Orange*

* [Google Pixel 4 XL](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel4xl/preview.png) (2019) [1440 x 3040]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `c55e7641f3ba76d7b777281b0ba4aa87`
  * Colors:
  * * *Just Black*
  * * *Clearly White*
  * * *Oh So Orange*

* [Google Pixel 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel5/preview.png) (2020) [1080 x 2340]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `870266635f047a49c2eae83f7d46e26e`
  * Colors:
  * * *Just Black*
  * * *Sorta Sage*

### Computers

* [Apple iMac 21"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/imac212015/preview.png) (2015) [4096 x 2304]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `385eb0911d0edb6821c18a2193bdadaf`
  * Colors:
  * * *Silver*

* [Apple iMac 24"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/imac242021/preview.png) (2021) [4480 x 2520]   
  * Author: [@ulbwa](https://ulbwa.xyz) [03.02.2022]
  * ID: `40a349f85ca132c2d6c1444db0be9561`
  * Colors:
  * * *Green*
  * * *Yellow*
  * * *Orange*
  * * *Pink*
  * * *Purple*
  * * *Blue*
  * * *Silver*

* [Apple MacBook 12"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbook122016/preview.png) (2016) [2304 x 1440]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `f74ec99f02ed5fafbe1cb1767763ed91`
  * Colors:
  * * *Space Gray*
  * * *Gold*

* [Apple MacBook Air (M1)](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookair2020/preview.png) (2020) [2560 x 1600]   
  * Author: [@ulbwa](https://ulbwa.xyz) [03.02.2022]
  * ID: `1f3fe3fec5b92861b7958bc75f40fe95`
  * Colors:
  * * *Silver*

* [Apple MacBook Pro 13"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro132015/preview.png) (2015) [2560 x 1600]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `2f15fb3eb0dde3b76771f3090c6ddbb6`
  * Colors:
  * * *Silver*

* [Apple MacBook Pro 15"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro152015/preview.png) (2015) [2880 x 1800]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `ba492b242a78b7f49caa41f61b5b3418`
  * Colors:
  * * *Silver*

* [Apple MacBook Pro 16"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro162019/preview.png) (2019) [3072 x 1920]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `0bfe5c7d2a8a4e5398090c3027791ed1`
  * Colors:
  * * *Space Gray*

* [Apple MacBook Pro 16"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro162021/preview.png) (2021) [3456 x 2234]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `80467845e71272f0d8d2bd13490a73f3`
  * Colors:
  * * *Silver*
  * * *Space Gray*

* [Google Pixelbook Go](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixelbookgo/preview.png) (2019) [1920 x 1080]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `6911ed9934b1c877a0b01c3750c2b79e`
  * Colors:
  * * *Just Black*

* [Apple Pro Display XDR](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/prodisplayxdr/preview.png) (2019) [6016 x 3384]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `8b728f1faab0389874db4bb0ae6244e5`
  * Colors:
  * * *Silver*

### Tablets

* [Apple iPad 9](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipad9/preview.png) (2021) [2160 x 1620]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `9c1f043b21ef803bd467135b83105f0b`
  * Colors:
  * * *Gold*
  * * *Silver*
  * * *Space Gray*

* [Apple iPad Air 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadair4/preview.png) (2020) [2360 x 1640]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `569262bc590b30cfb296471c3c8a4af8`
  * Colors:
  * * *Green*
  * * *Rose Gold*
  * * *Silver*
  * * *Sky Blue*
  * * *Space Gray*

* [Apple iPad Mini 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadmini5/preview.png) (2021) [2048 x 1536]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `7a8b3c603fe34817d9233e5b6afed174`
  * Colors:
  * * *Gold*
  * * *Silver*
  * * *Space Gray*

* [Apple iPad Pro 4 11"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadpro114/preview.png) (2020) [2388 x 1668]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `e47f6e3bb880a034866f59f97f612abe`
  * Colors:
  * * *Silver*
  * * *Space Gray*

* [Apple iPad Pro 4 12.9"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadpro134/preview.png) (2020) [2732 x 2048]   
  * Author: [@ulbwa](https://ulbwa.xyz) [31.01.2022]
  * ID: `9a85db6aeb1d45c896daff67af785936`
  * Colors:
  * * *Silver*
  * * *Space Gray*

### Wearable devices

* [Apple Watch Series 6 44mm](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/watchseries644mm/preview.png) (2020) [368 x 448]   
  * Author: [@ulbwa](https://ulbwa.xyz) [01.02.2022]
  * ID: `e055638cf7325a856ed0369dc8d0dcb1`
  * Colors:
  * * *Aluminum Case - Blue*
  * * *Aluminum Case - Gold*
  * * *Aluminum Case - Space Gray*
  * * *Aluminum Case - Silver*
  * * *Aluminum Case - Product Red*
  * * *Titanium Case - Light*
  * * *Titanium Case - Dark*
  * * *Stainless Steel Case - Gold*
  * * *Stainless Steel Case - Graphite*
  * * *Stainless Steel Case - Silver*

You can help the project by adding support for new mockups by contributing on [GitHub](https://github.com/ulbwazhine/MockupEngineer).

## Links
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/author.svg" height="30"/>](https://ulbwa.github.io)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/github.svg" height="30"/>](https://github.com/ulbwazhine/MockupEngineer)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/pypi.svg" height="30"/>](https://pypi.org/project/MockupEngineer)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/donate.svg" height="30"/>](https://ulbwa.github.io/go?to=donate)
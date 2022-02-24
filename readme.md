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

* [Samsung Galaxy S20](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/galaxys20/preview.png) (2020) [3200 x 1440] - `8080d01d4bdd37843088986938af2ae0`
  * *Cloud Blue*
  * *Cosmic Grey*
  * *Pink*

* [Samsung Galaxy S20 Ultra](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/galaxys20ultra/preview.png) (2020) [3200 x 1440] - `86fa8df7653bb8559cfc49b8670b16bc`
  * *Cosmic Black*
  * *Cosmic Grey*

* [Apple iPhone 12](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12/preview.png) (2020) [2532 x 1170] - `3596ecc24abae25279feddb34dd72a0e`
  * *Black*
  * *Blue*
  * *Green*
  * *Product Red*
  * *White*

* [Apple iPhone 12 Mini](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12mini/preview.png) (2020) [2340 x 1080] - `692048fda2b0b645f705066d522c12b8`
  * *Black*
  * *Blue*
  * *Green*
  * *Product Red*
  * *White*

* [Apple iPhone 12 Pro](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12pro/preview.png) (2020) [2532 x 1170] - `753cf086117da37d8c2e44e974880a94`
  * *Gold*
  * *Graphite*
  * *Pacific Blue*
  * *Silver*

* [Apple iPhone 12 Pro Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone12promax/preview.png) (2020) [2778 x 1284] - `5509eab3ac4c47315753b2e50faeb633`
  * *Gold*
  * *Graphite*
  * *Pacific Blue*
  * *Silver*

* [Apple iPhone 13](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13/preview.png) (2021) [2532 x 1170] - `33f683bda9f3beb5d0ce8ae5ef9e7fc4`
  * *Blue*
  * *Midnight*
  * *Pink*
  * *Product Red*
  * *Starlight*

* [Apple iPhone 13 Mini](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13mini/preview.png) (2021) [2340 x 1080] - `09340db4628d41418a4ed472db07c60e`
  * *Blue*
  * *Midnight*
  * *Pink*
  * *Product Red*
  * *Starlight*

* [Apple iPhone 13 Pro](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13pro/preview.png) (2021) [2532 x 1170] - `f0247d613f7d390cfb3362fd7242e515`
  * *Gold*
  * *Graphite*
  * *Sierra Blue*
  * *Silver*

* [Apple iPhone 13 Pro Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphone13promax/preview.png) (2021) [2778 x 1284] - `d95345535d98fcc6f4030e1d3ca62052`
  * *Gold*
  * *Graphite*
  * *Sierra Blue*
  * *Silver*

* [Apple iPhone SE](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonese2020/preview.png) (2020) [1334 x 750] - `553673b4367e8ebf59067d764b45e9fd`
  * *Black*
  * *Product Red*
  * *White*

* [Apple iPhone Xr](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexr/preview.png) (2018) [1792 x 828] - `6ccede90e5879fd87f85cfb2039247b3`
  * *Blue*
  * *Coral*
  * *Product Red*
  * *Silver*
  * *Space Gray*
  * *Yellow*

* [Apple iPhone Xs](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexs/preview.png) (2019) [2436 x 1125] - `f4128697b9cb1963cc4d14727872fa44`
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Apple iPhone Xs Max](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/iphonexsmax/preview.png) (2019) [2688 x 1242] - `16ebf01c894fb468c05a1b7c3e395d47`
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Google Pixel](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel/preview.png) (2016) [1920 x 1080] - `c7076ff96733f11e2cd8179fc2d5e7a4`
  * *Quite Black*
  * *Really Blue*
  * *Very Silver*

* [Google Pixel 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel4/preview.png) (2019) [2280 x 1080] - `3bfff2be23c2c354403f5a622a804f64`
  * *Just Black*
  * *Clearly White*
  * *Oh So Orange*

* [Google Pixel 4 XL](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel4xl/preview.png) (2019) [3040 x 1440] - `7b0762b034f6c29f2c77a66bb388f59e`
  * *Just Black*
  * *Clearly White*
  * *Oh So Orange*

* [Google Pixel 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixel5/preview.png) (2020) [2340 x 1080] - `2707894cc5d336d0ba276e6306e9f001`
  * *Just Black*
  * *Sorta Sage*

### Computers

* [Apple iMac 21"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/imac212015/preview.png) (2015) [4096 x 2304] - `71165ffd80a5db69ecd26e2e05ee1355`
  * *Silver*

* [Apple iMac 24"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/imac242021/preview.png) (2021) [4480 x 2520] - `808f7bc509565fb4bdaab7c7b5485a68`
  * *Green*
  * *Yellow*
  * *Orange*
  * *Pink*
  * *Purple*
  * *Blue*
  * *Silver*

* [Apple MacBook 12"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbook122016/preview.png) (2016) [2304 x 1440] - `4724b1349442f7fdaa60216d31cbd6a8`
  * *Space Gray*
  * *Gold*

* [Apple MacBook Air (M1)](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookair2020/preview.png) (2020) [2560 x 1600] - `d930de4882bee944ff19da75a4b6ee9f`
  * *Silver*

* [Apple MacBook Pro 13"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro132015/preview.png) (2015) [2560 x 1600] - `670487e7eaab6353af7f151f1da8622e`
  * *Silver*

* [Apple MacBook Pro 15"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro152015/preview.png) (2015) [2880 x 1800] - `4b33ac1e5b863a6b67f684d3e73a9796`
  * *Silver*

* [Apple MacBook Pro 16"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro162019/preview.png) (2019) [3072 x 1920] - `ce29763748dd896d6db09f94c626ca4d`
  * *Space Gray*

* [Apple MacBook Pro 16"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/macbookpro162021/preview.png) (2021) [3456 x 2234] - `75da9011a54ecd48e3da2c20e2c8afd0`
  * *Silver*
  * *Space Gray*

* [Google Pixelbook Go](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/pixelbookgo/preview.png) (2019) [1920 x 1080] - `c6ef98219e013c1dca8480b3dba14caa`
  * *Just Black*

* [Apple Pro Display XDR](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/prodisplayxdr/preview.png) (2019) [6016 x 3384] - `148a8f19517b4359cfe9db9092bb85a1`
  * *Silver*

* [Microsoft Surface Book](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/surfacebook/preview.png) (2015) [3000 x 2000] - `08816799dd7ebd63a9fe2e5a46f8b69c`
  * *Platinum*

### Tablets

* [Apple iPad 9](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipad9/preview.png) (2021) [2160 x 1620] - `347347da85ed8817ecd8eefd8fe22a0e`
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Apple iPad Air 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadair4/preview.png) (2020) [2360 x 1640] - `9a644764f99ccbe46753de8516e053fe`
  * *Green*
  * *Rose Gold*
  * *Silver*
  * *Sky Blue*
  * *Space Gray*

* [Apple iPad Mini 5](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadmini5/preview.png) (2021) [2048 x 1536] - `d8e92692708b63e444300f3b6dfacc6f`
  * *Gold*
  * *Silver*
  * *Space Gray*

* [Apple iPad Pro 4 11"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadpro114/preview.png) (2020) [2388 x 1668] - `a80a78a3f7492bb5d460c59de173bc88`
  * *Silver*
  * *Space Gray*

* [Apple iPad Pro 4 12.9"](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/ipadpro134/preview.png) (2020) [2732 x 2048] - `198018d62640d23de5ae4e3e6cbc5fd0`
  * *Silver*
  * *Space Gray*

* [Microsoft Surface Pro 3](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/surfacepro3/preview.png) (2014) [2160 x 1440] - `d250f0d3f84dd0b972c152ee592fbc3a`
  * *Platinum*

* [Microsoft Surface Pro 4](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/surfacepro4/preview.png) (2015) [2736 x 1824] - `604015046fcf51f1a264bb0333269f80`
  * *Platinum*

### Wearable devices

* [Apple Watch Series 6 44mm](https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupEngineer/templates/watchseries644mm/preview.png) (2020) [448 x 368] - `085a3fafbdec1f728aed9882adc2c5b0`
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
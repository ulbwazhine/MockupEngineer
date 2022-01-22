.. role:: raw-html-m2r(raw)
   :format: html



.. raw:: html

   <div align="center">
     <h1>MockupEngineer</h1>
     <p>An simple library for creating beautiful screenshots.</p>
   </div>


Example
-------

:raw-html-m2r:`<img align="center" width="350" src="https://raw.githubusercontent.com/ulbwazhine/MockupEngineer/main/MockupModule/templates/iphone12promax/example.png" alt="Apple iPhone 12 Pro Max">`

Usage
-----

In Python console:

.. code-block:: python

   from MockupModule import MockupEngineer

   mockup = MockupEngineer()

   mockup.generate(template=mockup.templates[0], 
                   screenshot_path='/path/to/screenshot',
                   color=mockup.templates[0].colors[0].color)

.. code-block::

   >>> /path/to/mockup

As a standalone application:

.. code-block::

   $ python -m MockupModule

Links
-----


* `Author <https://t.me/ulbwa>`_
* `GitHub <https://github.com/ulbwazhine/MockupEngineer>`_

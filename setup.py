from setuptools import setup

try:
    from pypandoc import convert

    read_md = lambda f: convert(f, 'rst')
except ImportError:
    read_md = lambda f: open(f, 'r').read()

setup(
    name='MockupEngineer',
    version='2022.22.01.3',
    packages=['MockupModule', 'MockupModule.templates'],
    url='https://github.com/ulbwazhine/MockupEngineer',
    license='MIT',
    author='Ulbwazhine',
    author_email='ulbwa@icloud.com',
    description='An simple library for creating beautiful screenshots.',
    install_requires=open('./requirements.txt', 'r').readlines(),
    long_description=read_md('README.md')
)

import os

from setuptools import setup

path = os.path.dirname(os.path.abspath(__file__))


setup(
    name='MockupEngineer',
    version='2022.22.01.6',
    packages=['MockupModule', 'MockupModule.templates'],
    url='https://github.com/ulbwazhine/MockupEngineer',
    license='MIT',
    author='Ulbwazhine',
    author_email='ulbwa@icloud.com',
    description='An simple library for creating beautiful screenshots.',
    install_requires=open('{}/requirements.txt'.format(path), 'r').readlines(),
    long_description=open('{}/readme.md'.format(path), 'r').read(),
    long_description_content_type='text/markdown'
)

from setuptools import setup


setup(
    name='MockupEngineer',
    version='2022.22.01.4',
    packages=['MockupModule', 'MockupModule.templates'],
    url='https://github.com/ulbwazhine/MockupEngineer',
    license='MIT',
    author='Ulbwazhine',
    author_email='ulbwa@icloud.com',
    description='An simple library for creating beautiful screenshots.',
    install_requires=open('./requirements.txt', 'r').readlines(),
    long_description=open('./readme.md', 'r').read(),
    long_description_content_type='text/markdown'
)

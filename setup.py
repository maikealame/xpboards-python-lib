from setuptools import setup, find_packages
from os import path

# Reads documentation from README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xpboards',
    packages=find_packages(include=['xpboards']),
    version='0.1.2',
    description='A python util for xpboards',
    author='Douglas Eloy',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown'
)   


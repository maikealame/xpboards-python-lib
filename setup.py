from setuptools import setup, find_packages

setup(
    name='xpboards',
    packages=find_packages(include=['xpboards']),
    version='0.1.0',
    description='A python util for xpboards',
    author='Douglas Eloy',
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    license='MIT'
)   


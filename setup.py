# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "0.0.1"

setup(
    name='vlc-random-videoclip',
    version=version,
    description='Play a random videoclip in vlc',
    author='Nikolai Nowaczyk',
    author_email='mail@nikno.de',
    license='MIT',
    packages=find_packages(),
    install_requires=['python-vlc']
)

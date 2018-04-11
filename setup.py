#!/usr/bin/env python3

from distutils.core import setup
from m3helper.version import __version__, __appname__

setup(
    name=__appname__,
    version=__version__,
    author='Talv',
    url='https://github.com/Talv/m3helper',
    packages=['m3helper'],
    entry_points={
        'console_scripts': [
            'm3helper=m3helper.main:main',
        ]
    },
    install_requires=[
        'toml'
    ],
)

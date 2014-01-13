# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cookiecutter-project
version = cookiecutter-project.__version__

setup(
    name='cookiecutter-project',
    version=version,
    author='',
    author_email='will@django.nu',
    packages=[
        'cookiecutter-project',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['cookiecutter-project/manage.py'],
)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages


requirements = [
]

test_requirements = [
]

setup(
    name='simulations',
    version='0.1.0',
    packages=find_packages('src', exclude=["*.tests''", "*.tests.*", "tests.*", "tests"]),
    package_dir={'':'src'},
    include_package_data=False,
    install_requires=requirements,

    author='Jerry Kiely',
    author_email='jerry@cowboysmall.com',
    description='Simulations',
    keywords='simulations',
    url='https://github.com/cowboysmall/simulations',

    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
    ],

    test_suite='tests',
    tests_require=test_requirements
)
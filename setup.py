#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='mockwebserver',
    version='0.2.0',
    description='A simple web server for unit testing purposes. Acts as context manager for teardown.',
    author='Virtualstock',
    author_email='dev.admin@virtualstock.com',
    url='https://github.com/Virtualstock/mockwebserver',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['attrs'],
    tests_require=['requests'],
)

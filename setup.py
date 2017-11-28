#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='mockwebserver',
    version='0.3.0',
    description='A simple web server for unit testing purposes. Acts as context manager for teardown.',
    author='Ronan Klyne',
    author_email='ronan.klyne@virtualstock.co.uk',
    url='http://pypi.v-source.co.uk/',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'attrs',
        'wsgi-intercept==1.5.1',
    ],
    tests_require=['requests'],
)

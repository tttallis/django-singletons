#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-singletons',
    version='0.1.6',
    description='Reusable singleton models for Django',
    author='Thomas Ashelford',
    author_email='thomas@ether.com.au',
    url='http://github.com/tttallis/django-singletons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
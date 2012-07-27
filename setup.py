#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-admin-jqueryui',
    version='1.8.22',
    author='Piotr Kilczuk -- Hint',
    author_email='piotr@hint.pl',
    url='https://github.com/hint/django-admin-jqueryui',
    description='Simply adds a jquery ui to the admin panel',
    #packages = ['inline_ordering',],
    packages=find_packages(),
    provides=['admin_jqueryui', ],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

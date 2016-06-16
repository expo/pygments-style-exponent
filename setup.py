#!/usr/bin/python

from setuptools import setup

setup(
    name = 'pygments-style-exponent',
    version = '0.1',
    description = 'Pygments style for Exponent (getexponent.com)',
    license = 'BSD',

    author = 'Brent Vatne',
    author_email = 'brentvatne@gmail.com',

    url = 'https://github.com/exponentjs/pygments-style-exponent',

    packages = ['pygments_style_exponent'],
    install_requires = ['pygments >= 1.4'],

    entry_points = '''[pygments.styles]
                      exponent = pygments_style_exponent:ExponentStyle''',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

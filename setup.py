#!/usr/bin/env python

import os
import sys

import scapegoat

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = scapegoat.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='scapegoat',
    version=version,
    description="""Simple task management""",
    long_description=readme + '\n\n' + history,
    author='Alexander Herrmann',
    author_email='darignac@gmail.com',
    url='https://github.com/dArignac/scapegoat',
    packages=[
        'scapegoat',
    ],
    include_package_data=True,
    install_requires=[
        'Django'
    ],
    license='MIT',
    zip_safe=False,
    keywords='scapegoat',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)

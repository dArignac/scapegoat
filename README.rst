=========
scapegoat
=========

.. image:: https://travis-ci.org/dArignac/scapegoat.png?branch=master
    :target: https://travis-ci.org/dArignac/scapegoat

.. image:: http://codecov.io/github/dArignac/scapegoat/coverage.svg?branch=master
    :target: http://codecov.io/github/dArignac/scapegoat?branch=master

.. image:: https://readthedocs.org/projects/scapegoat/badge/?version=latest
    :target: https://readthedocs.org/projects/scapegoat/?badge=latest
    :alt: Documentation Status

Simple task management

Documentation
-------------

The full documentation is at https://scapegoat.readthedocs.org.

Quickstart
----------

Install scapegoat::

    pip install scapegoat

To use it, add the scapegoat url and navigate to there. Scapegoat is standalone.::

    urlpatterns = [
        ...
        url(r'^', include('scapegoat.urls')),
        ...
    ]

Features
--------

* TODO

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage

================================
python-anyconfig-cbor-backend
================================

.. image:: https://img.shields.io/pypi/v/anyconfig-cbor-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-cbor-backend/
   :alt: [Latest Version]

.. image:: https://github.com/ssato/python-anyconfig-cbor-backend/workflows/Tests/badge.svg
   :target: https://github.com/ssato/python-anyconfig-cbor-backend/actions?query=workflow%3ATests
   :alt: [Github Actions: Test status]

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-cbor-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-cbor-backend
   :alt: Coverage Status

.. image:: https://scrutinizer-ci.com/g/ssato/python-anyconfig-cbor-backend/badges/quality-score.png
   :target: https://scrutinizer-ci.com/g/ssato/python-anyconfig-cbor-backend
   :alt: [Code Quality by Scrutinizer]

.. landscape looks stopped their service.
.. .. image:: https://landscape.io/github/ssato/python-anyconfig-cbor-backend/master/landscape.png
   :target: https://landscape.io/github/ssato/python-anyconfig-cbor-backend/master
   :alt: Code Health

This is a backend module for python-anyconfig to support to load and dump CBOR
files with using cbor.

- Author: Satoru SATOH <ssato@redhat.com>
- License: MIT

SEE ALSO:

- python-anyconfig: https://pypi.python.org/pypi/anyconfig
- cbor: https://pypi.python.org/pypi/cbor
- CBOR spec: http://cbor.io

Build & Install
================

If you're Fedora or Red Hat Enterprise Linux user, try::

  $ python setup.py srpm && mock dist/<package>-<ver_dist>.src.rpm
  
or::

  $ python setup.py rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:

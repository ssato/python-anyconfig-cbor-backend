#
# Copyright (C) 2018 Satoru SATOH <satoru.satoh @ gmail.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name
from __future__ import absolute_import, print_function

import os.path
import os
import unittest

import anyconfig

from tests.common import _bytes, dicts_equal


_CURDIR = os.path.dirname(__file__)


class Test(unittest.TestCase):

    conf_path = os.path.join(_CURDIR, "0.cbor")

    def test_20_load(self):
        try:
            cnf = anyconfig.load(self.conf_path)
        except anyconfig.UnknownFileTypeError:
            print("all types=%r" % anyconfig.list_types())
            raise

        ref = {_bytes('a'): 0,
               _bytes('b'): _bytes('bbb'),
               _bytes('c'): 5,
               _bytes('sect0'): {_bytes('d'): [_bytes('x'), _bytes('y'),
                                               _bytes('z')]}}
        self.assertTrue(dicts_equal(cnf, ref))

# vim:sw=4:ts=4:et:

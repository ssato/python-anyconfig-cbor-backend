#
# Copyright (C) 2018 Satoru SATOH <satoru.satoh @ gmail.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name
from __future__ import absolute_import

import os.path
import os
import unittest

import anyconfig


_CURDIR = os.path.dirname(__file__)


class Test(unittest.TestCase):

    conf_path = os.path.join(_CURDIR, "0.cbor")

    def test_20_load(self):
        conf = anyconfig.load(self.conf_path)
        self.assertEqual(conf['b'], "bbb", conf)

# vim:sw=4:ts=4:et:

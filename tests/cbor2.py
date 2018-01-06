#
# Copyright (C) 2018 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
from __future__ import absolute_import

import anyconfig_cbor_backend.cbor2 as TT
import tests.common as TBC


class HasParserTrait(TBC.HasParserTrait):

    psr = TT.Parser()
    cnf = dict(a=0, b="bbb", c=5, sect0=dict(d=["x", "y", "z"]))
    cnf_s = TT.cbor2.dumps(cnf)


class Test_10(TBC.Test_10_dumps_and_loads, HasParserTrait):

    dump_options = dict(datetime_as_timestamp=True, value_sharing=True)


class Test_20(TBC.Test_20_dump_and_load, HasParserTrait):

    pass

# vim:sw=4:ts=4:et:

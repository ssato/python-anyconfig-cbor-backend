#
# Copyright (C) 2018 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
# pylint: disable=too-many-ancestors
r"""CBOR backend:

- Format to support: CBOR, http://cbor.io, https://tools.ietf.org/html/rfc7049
- Requirements: cbor, https://pypi.python.org/pypi/cbor2
- Development Status :: 4 - Beta
- Limitations: None obvious
- Special options:

  - All options of cbor.load{s,} and cbor.dump{s,} should work.
  - See also: https://github.com/agronholm/cbor2/blob/master/cbor2/

Changelog:

    .. versionadded:: 0.8.4
"""
from __future__ import absolute_import
import anyconfig.backend.base
import cbor2


class Parser(anyconfig.backend.base.StringStreamFnParser,
             anyconfig.backend.base.BinaryFilesMixin):
    """Parser for CBOR files.
    """
    _type = "cbor"
    _extensions = ["cbor"]
    _loads_opts = ["tag_hook", "object_hook"]
    _dump_opts = ["datetime_as_timestamp", "timezone", "value_sharing",
                  "default"]

    _load_from_string_fn = anyconfig.backend.base.to_method(cbor2.loads)
    _load_from_stream_fn = anyconfig.backend.base.to_method(cbor2.load)
    _dump_to_string_fn = anyconfig.backend.base.to_method(cbor2.dumps)
    _dump_to_stream_fn = anyconfig.backend.base.to_method(cbor2.dump)

# vim:sw=4:ts=4:et:

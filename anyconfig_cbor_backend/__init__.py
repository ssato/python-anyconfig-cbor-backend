"""anyconfig backend to support Java properties files.
"""
from __future__ import absolute_import
from .cbor import Parser as CBORParser
from .cbor2 import Parser as CBOR2Parser

__all__ = ["CBORParser", "CBOR2Parser"]

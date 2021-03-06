# Stubs for fastecdsa.encoding.asn1 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..curve import Curve
from ..point import Point
from .util import int_bytelen, int_to_bytes
from typing import Any, Tuple

INTEGER: bytes
BIT_STRING: bytes
OCTET_STRING: bytes
OBJECT_IDENTIFIER: bytes
SEQUENCE: bytes
PARAMETERS: bytes
PUBLIC_KEY: bytes


def asn1_structure(data_type: bytes, data: bytes) -> bytes:
    ...


def asn1_private_key(d: int, curve: Curve) -> bytes:
    ...


def asn1_ecversion(version: Any = ...) -> bytes:
    ...


def asn1_ecpublickey() -> bytes:
    ...


def asn1_oid(curve: Curve) -> bytes:
    ...


def asn1_public_key(Q: Point) -> bytes:
    ...


def parse_asn1_length(data: bytes) -> Tuple[int, bytes, bytes]:
    ...

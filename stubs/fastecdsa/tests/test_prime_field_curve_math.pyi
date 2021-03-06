# Stubs for fastecdsa.tests.test_prime_field_curve_math (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..curve import P192, P224, P256, P384, P521, secp256k1
from ..point import Point
from unittest import TestCase

class TestPrimeFieldCurve(TestCase):
    def test_P192_arith(self) -> None: ...
    def test_P224_arith(self) -> None: ...
    def test_P256_arith(self) -> None: ...
    def test_P384_arith(self) -> None: ...
    def test_P521_arith(self) -> None: ...
    def test_secp256k1_arith(self) -> None: ...
    def test_arbitrary_arithmetic(self) -> None: ...
    def test_point_at_infinity_arithmetic(self) -> None: ...

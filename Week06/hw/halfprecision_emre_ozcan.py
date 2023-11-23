# Based on IEEE Standard for Floating-Point Arithmetic (IEEE 754)
# IEEE Std 754-2008 (Revision of IEEE Std 754-1985), 29 August 2008

import math
from dataclasses import dataclass
from decimal import Decimal
from numbers import Complex


@dataclass(frozen=True)
class IEEE754BinaryFormat:
    """Represents a Binary interchange floating-point format"""

    s: int
    """'sign bit' parameter"""

    w: int
    """'exponent field width in bits' parameter"""

    t: int
    """'trailing significant field width in bits' parameter, (p - 1)"""

    @staticmethod
    def binary_k(k: int) -> "IEEE754BinaryFormat":
        """
        Construct a binary interchange floating-point format from total
        storage bits

        The rest of the parameters are calculated using Table 3.5 of the IEEE
        754 standard.

        :param k: 'storage with bits' parameter of the format
        :return: a binary interchange floating-point format
        """

        # Table 3.5 -- Binary interchange format parameters
        if not k >= 128:
            raise ValueError("k must be greater than or equal to 128")
        if k % 32 != 0:
            raise ValueError("k must be a multiple of 32")

        w = round(4 * math.log2(k)) - 13
        return IEEE754BinaryFormat(
            s=1,
            w=w,
            t=k - w - 1
        )

    @staticmethod
    def binary16() -> "IEEE754BinaryFormat":
        """Construct a half-precision floating-point format"""
        return IEEE754BinaryFormat(1, 5, 10)

    @staticmethod
    def binary32() -> "IEEE754BinaryFormat":
        """Construct a single-precision floating-point format"""
        return IEEE754BinaryFormat(1, 8, 23)

    @staticmethod
    def binary64() -> "IEEE754BinaryFormat":
        """Construct a double-precision floating-point format"""
        return IEEE754BinaryFormat(1, 11, 52)

    @staticmethod
    def binary128() -> "IEEE754BinaryFormat":
        """Construct a quadruple-precision floating-point format

        See the method `binary_k` if you want more bits.
        """
        return IEEE754BinaryFormat(1, 15, 112)

    def __post_init__(self):
        if self.s != 1:
            raise ValueError("s must be 1")

    def __str__(self):
        return f"<binary{self.k()} {self.s}, {self.w}, {self.t}>"

    def p(self) -> int:
        """'the number of digits in the significand (precision)' parameter

        This parameter is bound to t by the relation `p = t + 1` because the
        most significant bit of the trailing significand field is implicit.
        """
        return self.t + 1

    def emax(self) -> int:
        """'the maximum exponent e' parameter"""

        # Table 3.5 -- Binary interchange format parameters
        # emax = 2^(k – p - 1) – 1
        # p - 1 = t, therefore, p = t + 1
        # emax = 2^(k – t - 2) – 1
        # since k = 1 + w + t, emax = 2^(w – 1) – 1
        return 2 ** (self.w - 1) - 1

    bias = emax
    """constant chosen to make the exponent field unsigned
    
    Note that this constant is always equal to emax.
    (See Table 3.5.)
    """

    def emin(self) -> int:
        """'the minimum exponent e' parameter"""

        # 3.3 Sets of floating-point data
        # emin shall be 1 − emax for all formats.
        # emin = 1 - emax
        #      = 1 - (2^(w – 1) – 1)
        #      = 1 - 2^(w - 1) + 1
        #      = -2^(w - 1) + 2
        return -2 ** (self.w - 1) + 2

    def k(self) -> int:
        """'storage width in bits' parameter"""

        # Table 3.5 -- Binary interchange format parameters
        return 1 + self.w + self.t

    def _s_field_for(self, _number: float | str | Decimal, /) -> str:
        if _number < 0:
            return self.s * "1"
        return self.s * "0"

    @staticmethod
    def _int2binary(_number: Decimal | int, /, *, width: int = 1) -> str:
        """convert an integer to binary (e.g., `13` -> `1101`)"""
        if _number == 0:
            return "0".rjust(width, "0")
        result = ""
        if _number > 0:
            while _number > 0:
                result = str(_number % 2) + result
                _number //= 2
            return result.rjust(width, "0")
        else:
            while len(result) < width:
                result = str(_number % 2) + result
                _number //= 2
            return result.rjust(width, "1")

    @staticmethod
    def _binary2int(_number: str, /) -> Decimal:
        """convert a binary number to an integer (e.g., `1101` -> `13`)"""
        result = 0
        for index, digit in enumerate(_number[::-1]):
            result += int(digit) * 2 ** index
        return Decimal(result)

    @staticmethod
    def _normalized2binary(_number: Decimal, /, *, width: int) -> str:
        """
        convert the fractional part of a float smaller than 1 to binary
        (e.g., `0.375` -> `011`)
        """
        if _number >= 1:
            raise ValueError("number must be smaller than 1")

        result = ""
        while _number > 0 and len(result) < width:
            _number *= 2
            if _number >= 1:
                result += "1"
                _number -= 1
            else:
                result += "0"
        return result.ljust(width, "0")

    def _combine_parts(self, s_field: str, e_field: str, t_field: str) -> str:
        assert len(s_field) == self.s
        assert len(e_field) == self.w
        assert len(t_field) == self.t
        return s_field + e_field + t_field

    def represent(self, _number: int | float | Decimal, /) -> str:
        """Represent a number in this binary interchange format

        :param _number: the number to represent
        :return: the representation of the number in this interchange format
        """

        if not isinstance(_number, (int, float, Decimal)):
            raise TypeError("number must be a int, float or Decimal")
        if isinstance(_number, Complex) and _number.imag != 0:
            raise TypeError("number must not be a complex")
        if _number is True or _number is False:
            raise TypeError("number must not be a bool")

        _number = Decimal(_number)

        # 3.4 Binary interchange format encodings
        # The representation r of the floating-point datum, and value v of the
        # floating-point datum represented, are inferred from the constituent
        # fields as follows:

        # a) If E = 2^w − 1 and T != 0, then [...] v is NaN regardless of S.
        if math.isnan(_number):  # This step encodes the NaNs.
            return self._combine_parts(
                s_field="0" * self.s,
                e_field="1" * self.w,
                t_field="1" * self.t
            )

        # b) If E = 2^w − 1 and T = 0, then [...] v = (-1)^S * (+inf).
        if math.isinf(_number):  # This step encodes the infinities.
            return self._combine_parts(
                s_field=self._s_field_for(_number),
                e_field="1" * self.w,
                t_field="0" * self.t,
            )

        # e) If E=0 and T=0 and S=1, then r is (1, emin, 0)
        #    and v = (-1)^S * (+0) (signed zero).
        if _number == 0:  # This step encodes the zeros.
            sign = math.copysign(1, _number)
            return self._combine_parts(
                s_field=self._s_field_for(sign),
                e_field="0" * self.w,
                t_field="0" * self.t,
            )

        # 3.4 Binary interchange format encodings
        exponent = Decimal(math.floor(math.log2(abs(_number))))

        if exponent > self.emax():
            return self.represent(_number * Decimal("inf"))

        # After this process is done, if e = emin and 0 < m < 1, the
        # floating-point number is subnormal. Subnormal numbers (and zero) are
        # encoded with a reserved biased exponent value.
        emin = self.emin()
        if exponent < emin:
            # Assume exponent to be emin and encode as subnormal.
            exponent = Decimal(emin)
            mantissa = abs(_number) / 2 ** exponent

            if 0 < mantissa < 1:
                # d) If E=0 and T!=0, then r is (S, emin, (0 + 2^(1-p) * T))
                #    [...] v = (-1)^S * 2^emin * (0 + 2^(1-p) * T).
                return self._combine_parts(
                    s_field=self._s_field_for(_number),
                    e_field="0" * self.w,
                    t_field=self._normalized2binary(mantissa, width=self.t),
                )

            return self.represent(_number * Decimal("inf"))

        # c) If 1 <= E <= 2^w − 2, then r is (S, (E-bias), (1+2^(1-p)*T))
        #    [...] v = (-1)^S * 2^(E − bias) * (1 + 2^(1-p) * T).
        mantissa = abs(_number) / 2 ** exponent
        return self._combine_parts(
            s_field=self._s_field_for(_number),
            e_field=self._int2binary(exponent + self.bias(), width=self.w),
            t_field=self._normalized2binary(mantissa - 1, width=self.t),
        )

    __call__ = represent

    def parse(self, _number: str, /) -> Decimal:
        """Parse a number represented in this binary interchange format

        :param _number: The number represented in binary
        :return: The parsed number
        """
        if not isinstance(_number, str):
            raise TypeError("number must be a string")
        if len(_number) != self.k():
            raise ValueError("number must be a string of length k")
        for c in _number:
            if c not in ["0", "1"]:
                raise ValueError("number must be a string of 0s and 1s")

        s_field_bits = _number[:self.s]
        e_field_bits = _number[self.s:self.s + self.w]
        t_field_bits = _number[self.s + self.w:]

        s_field = self._binary2int(s_field_bits)
        e_field = self._binary2int(e_field_bits)
        t_field = self._binary2int(t_field_bits)

        sign = Decimal("-1") if s_field == 1 else Decimal("1")

        # The representation r of the floating-point datum, and value v of the
        # floating-point datum represented, are inferred from the constituent
        # fields as follows:

        # a) If E = 2^w − 1 and T != 0, then r is qNaN or sNaN and v is NaN
        #    regardless of S (see 6.2.1).
        if e_field == 2 ** self.w - 1 and t_field != 0:
            return Decimal("nan")

        # b) If E = 2^w − 1 and T = 0, then r and v = (−1)^S * (+inf).
        if e_field == 2 ** self.w - 1 and t_field == 0:
            return sign * Decimal("inf")

        # 1 - p = 1 - (t + 1)
        #       = 1 - t - 1
        #       = -t
        mantissa = Decimal(2 ** (-self.t)) * t_field

        # c) If 1 <= E <= 2^w − 2, then r is (S, (E−bias), (1 + 2^(1 − p) * T));
        if 1 <= e_field <= 2 ** self.w - 2:
            # the value of the corresponding floating-point number is
            # v = (−1)^S * 2^(E−bias) * (1 + 2^(1 − p) * T)
            return sign * 2 ** (e_field - self.bias()) * (1 + mantissa)

        # d) If E=0 and T!=0, then r is (S, emin, (0 + 2^(1-p) * T))
        if e_field == 0 and t_field != 0:
            # the value of the corresponding floating-point number is
            # v = (−1)^S * 2^emin * (0 + 2^(1-p) * T).
            return sign * 2 ** Decimal(self.emin()) * (0 + mantissa)

        # e) If E=0 and T=0, then r is (S, emin, 0) and v = (−1)^S * (+0).
        if e_field == 0 and t_field == 0:
            return sign * Decimal("0")

    def is_representation_subnormal(self, _number: str, /) -> bool:
        """
        Check if a number represented in this binary interchange format is
        a subnormal number

        :param _number: The number represented in binary
        :return: Whether the specified number is a subnormal number
        """
        if not isinstance(_number, str):
            raise TypeError("number must be a string")
        if len(_number) != self.k():
            raise ValueError("number must be a string of length k")
        for c in _number:
            if c not in ["0", "1"]:
                raise ValueError("number must be a string of 0s and 1s")

        e_field_bits = _number[self.s:self.s + self.w]
        t_field_bits = _number[self.s + self.w:]

        for bit in e_field_bits:
            if bit != "0":
                return False

        # e_field is all zeros

        for bit in t_field_bits:
            if bit != "0":
                return True

        return False


# Table 3.5 -- Binary interchange format parameters
HalfPrecision = IEEE754BinaryFormat.binary16()
# SinglePrecision = IEEE754BinaryFormat.binary32()
# DoublePrecision = IEEE754BinaryFormat.binary64()
# QuadruplePrecision = IEEE754BinaryFormat.binary_k(128)

if __name__ == "__main__":
    import itertools
    for i in itertools.product("01", repeat=16):
        bits = "".join(i)
        parsed = HalfPrecision.parse(bits)
        re_represented = HalfPrecision.represent(parsed)
        assert bits == re_represented or math.isnan(parsed), \
               f"{bits!r}, {re_represented!r}"
        print(bits, re_represented, parsed, sep="\t")

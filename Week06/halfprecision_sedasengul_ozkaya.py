import math

class HalfPrecision:
    def __init__(self, number):
        if type(number) is not float:
            raise TypeError("Input must be a float")
        self.number = number

    def __str__(self):
        x = self.number
        sign = "1" if math.copysign(1.0, x) < 0 else "0"
        x = abs(x)

        if x == 0.0:
            return sign + "00000" + "0000000000"

        if math.isinf(x):
            return sign + "11111" + "0000000000"

        m, e = math.frexp(x)
        e -= 1
        m *= 2
        bias = 15
        exp = e + bias

        # Normalized
        if exp > 0:
            if exp >= 31:
                return sign + "11111" + "0000000000"

            frac = m - 1
            mant = int(frac * 1024 + 0.5)

            if mant == 1024:
                mant = 0
                exp += 1
                if exp >= 31:
                    return sign + "11111" + "0000000000"

            return sign + format(exp, "05b") + format(mant, "010b")

        # Denormal
        mant = int(x / (2 ** -14) * 1024 + 0.5)
        mant = min(mant, 1023)

        return sign + "00000" + format(mant, "010b")

import numpy as np


class IEEE754:
    def __init__(self, x: float, precision: int = 2,
                 force_length: int = None,
                 force_exponent: int = None,
                 force_mantissa: int = None,
                 force_bias: int = None):
        self.precision = precision
        length_list = [16, 32, 64, 128, 256]
        exponent_list = [5, 8, 11, 15, 19]
        mantissa_list = [10, 23, 52, 112, 236]
        bias_list = [15, 127, 1023, 16383, 262143]
        self.__length = force_length if force_length is not None else length_list[precision]
        self.__exponent = force_exponent if force_exponent is not None else exponent_list[precision]
        self.__mantissa = force_mantissa if force_mantissa is not None else mantissa_list[precision]
        self.__bias = force_bias if force_bias is not None else bias_list[precision]
        self.s = 0 if x >= 0 else 1
        x = abs(x)
        self.x = x
        self.i = self.integer2binary(int(x))
        self.d = self.decimal2binary(x - int(x))
        self.e = self.integer2binary((self.i.size - 1) + self.__bias)
        self.m = np.append(self.i[1::], self.d)
        self.h = ''

    def __str__(self):
        r = np.zeros(self.__length, dtype=int)
        i_d = np.append(self.i[1::], self.d)
        r[0] = self.s
        r[1 + (self.__exponent - self.e.size):(self.__exponent + 1):] = self.e
        r[(1 + self.__exponent):(1 + self.__exponent + i_d.size):] = i_d[0:self.__mantissa]
        s = np.array2string(r, separator='')
        return s[1:-1].replace("\n", "").replace(" ", "")

    @staticmethod
    def integer2binary(x: int) -> np.ndarray:
        b = np.empty((0,), dtype=int)
        while x > 1:
            b = np.append(b, np.array([x % 2]))
            x = int(x / 2)
        b = np.append(b, np.array([x]))
        b = b[::-1]
        return b

    def decimal2binary(self, x: float) -> np.ndarray:
        b = np.empty((0,), dtype=int)
        i = 0
        while x > 0 and i < self.__mantissa:
            x *= 2
            b = np.append(b, np.array([int(x)]))
            x -= int(x)
            i += 1
        return b

    def str2hex(self) -> str:
        s = str(self)
        for i in range(0, len(s), 4):
            ss = s[i:i + 4]
            si = 0
            for j in range(4):
                si += int(ss[j]) * (2 ** (3 - j))
            sh = hex(si)
            self.h += sh[2]
        return self.h.capitalize()


if __name__ == '__main__':
    # with default options (Double Precision)
    number = 13.375
    a = IEEE754(number)
    # you should call the instance as a string
    print(str(a))
    print(f"{a}")
    # you can get the hexadecimal presentation like this
    print(a.str2hex())
    # or you can specify a precision and
    for p in range(5):
        a = IEEE754(number, p)
        print("x = %f | b = %s | h = %s" % (13.375, a, a.str2hex()))
    # or you can use your own custom precision
    a = IEEE754(number,
                force_length=19,
                force_exponent=6,
                force_mantissa=12,
                force_bias=31)
    print(f"{a}")



class HalfPrecision:

    __BIAS = 15

    def __init__(self, number: float):
        if type(number)!=float:
            raise TypeError("Please enter a float")
        if number > 65504:
            self.string_representation = "0111110000000000"
            return
        if number == float('inf'):
            self.string_representation = "0111110000000000"
            return
        elif number == float('-inf'):
            self.string_representation = "1111110000000000"
            return
        binary_representation = str(BinaryRepresentation(number))
        sign_bit = '1' if binary_representation[0] == '-' else '0'
        abs_binary = binary_representation.replace("-", "")
        dot_index = abs_binary.index('.')
        exponent: int
        if abs_binary.startswith('1'):
            exponent = dot_index - 1
        else:
            decimal = abs_binary.partition('.')[2]
            if decimal.find('1') == -1:
                self.string_representation = "0000000000000000" \
                    if sign_bit == '0' else "1000000000000000"
                return
            else:
                exponent = -(decimal.index('1') + 1)
        biased = float(exponent + HalfPrecision.__BIAS)
        exponent_bits = BinaryRepresentation(biased).integer2binary()
        while len(exponent_bits) < 5:
            exponent_bits = '0' + exponent_bits
        ind_1 = abs_binary.index('1')
        ment = abs_binary[ind_1 + 1:]
        ment = ment.replace('.', '')
        length = len(ment)
        if length < 10:
            while len(ment) < 10:
                ment += '0'
        elif length > 10:
            ment = ment[:10]
        self.string_representation = sign_bit + exponent_bits + ment


    def __str__(self):
        return self.string_representation




class BinaryRepresentation:

    def __init__(self, number: float):
        if not isinstance(number, float):
            raise TypeError('number is not a float')
        self.negative = True if str(number)[0] == '-' else False
        self.number = abs(number)

    def integer2binary(self):
        num_int = int(self.number)
        if num_int == 0:
            return "0"
        arr = []
        while num_int > 0:
            arr.append(num_int % 2)
            num_int = num_int // 2
        arr.reverse()
        return self.int_array_to_string(arr)

    def decimal2binary(self):
        num_dec = self.number - int(self.number)
        arr = []
        loop_count = 1
        while loop_count < 25:
            if num_dec == 0:
                break
            num_dec *= 2
            int_part = int(num_dec)
            arr.append(int_part)
            if int_part == 1:
                num_dec -= int_part
            loop_count += 1
        return self.int_array_to_string(arr)

    def __str__(self):
        prefix = "-" if self.negative else ""
        return prefix + self.integer2binary() + "." + self.decimal2binary()

    @staticmethod
    def int_array_to_string(arr) -> str:
        result = ''
        for i in arr:
            result += str(i)
        return result


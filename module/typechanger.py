class Type:
    @staticmethod
    def Decimal_to_Binary(number):
        number = int(number)
        binary = []
        while number != 0:
            binary.append(number % 2)
            number = number // 2
        binary.reverse()
        return binary

    @staticmethod
    def Binary_to_Decimal(binary):
        binary.reverse()
        i = decimal = 0
        for bit in binary:
            decimal += bit * (2 ** i)
            i += 1
        return decimal

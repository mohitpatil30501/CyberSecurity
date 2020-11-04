class Type:
    @staticmethod
    def Decimal_to_Binary(ip_part):
        binary = []
        for number in ip_part:
            try:
                number = int(number)
            except ValueError:
                return None
            temp_binary = []
            while number != 0:
                temp_binary.append(number % 2)
                number = number // 2
            if len(temp_binary) < 8:
                for i in range(0, 8 - len(temp_binary)):
                    temp_binary.append(0)
            temp_binary.reverse()
            binary.extend(temp_binary)
        return binary

    @staticmethod
    def Binary_to_Decimal(binary):
        length = len(binary)
        decimal = binary_lists = []
        binary.reverse()
        binary_lists.append(binary[: length // 4])
        binary_lists.append(binary[length // 4: length // 2])
        binary_lists.append(binary[length // 2: (length * 3) // 4])
        binary_lists.append(binary[(length * 3) // 4:])
        for binary_element in binary_lists:
            print(len(binary_element))
            i = decimal_element = 0
            for bit in binary_element:
                decimal_element += bit * (2 ** i)
                i += 1
            decimal.append(str(decimal_element))
        return decimal

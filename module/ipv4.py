from module.typechanger import Type


class IPv4:
    def __init__(self):
        self.ip = str(input("Format: 127.0.0.1\nEnter IP Address: "))
        self.ip_part = self.data = self.mask = None

    def Validation_of_ip(self):
        self.ip_part = self.ip.split('.', 4)
        if len(self.ip_part) != 4:
            return False
        for i in self.ip_part:
            if 255 < int(i) or int(i) < 0:
                return False
        return True

    def Check_class(self):
        if self.Validation_of_ip():
            ip_first = int(self.ip_part[0])
            if 0 <= ip_first <= 127:
                Class = "A"
                Application = "Unicast"
            elif 128 <= ip_first <= 191:
                Class = "B"
                Application = "Unicast"
            elif 192 <= ip_first <= 223:
                Class = "C"
                Application = "Unicast"
            elif 224 <= ip_first <= 239:
                Class = "D"
                Application = "Multicast"
            elif 240 <= ip_first <= 255:
                Class = "E"
                Application = "Reserved"
            else:
                return False
            self.data = {
                'ip': self.ip,
                'class': Class,
                'application': Application
            }
            return self.data
        return False

    def Subnet_mask(self):
        data = self.Check_class()
        if not data:
            return False
        if data['class'] == "A":
            subnet = "255.0.0.0"
        elif data['class'] == "B":
            subnet = "255.255.0.0"
        elif data['class'] == "C":
            subnet = "255.255.255.0"
        elif data['class'] == "D" or data['class'] == "E":
            subnet = "255.255.255.255"
        else:
            return False
        self.data['subnet'] = subnet
        return self.data

    def Mask(self):
        data = self.Subnet_mask()
        self.mask = data['mask'] = int(input("Enter mask: /"))
        if self.mask < 0 or self.mask > 32:
            return False
        last_bits = 32 - self.mask

        ip_binary_first = Type.Decimal_to_Binary(self.ip_part)
        ip_binary_last = Type.Decimal_to_Binary(self.ip_part)
        number_of_ip_list = []
        ip_binary_first.reverse()
        ip_binary_last.reverse()

        for i in range(0, last_bits):
            ip_binary_first[i] = 0
            ip_binary_last[i] = 1
            number_of_ip_list.append(1)

        ip_binary_first.reverse()
        ip_binary_last.reverse()

        ip_binary_first = Type.Binary_to_Decimal(ip_binary_first)
        ip_binary_last = Type.Binary_to_Decimal(ip_binary_last)
        self.data['first_ip_address'] = ip_binary_first[0] + '.' + ip_binary_first[1] + '.' + ip_binary_first[2] + '.' + ip_binary_first[3]
        self.data['last_ip_address'] = ip_binary_last[0] + '.' + ip_binary_last[1] + '.' + ip_binary_last[2] + '.' + ip_binary_last[3]
        self.data['number_of_ip_addresses'] = Type.Binary_to_Decimal_int(number_of_ip_list) + 1
        return self.data

    def print_ipv4(self):
        if self.Mask() is None:
            return False
        print("\n\tData Retrived:\nGiven IP:", self.data['ip'])
        print("Class:", self.data['class'], "\nApplication:", self.data['application'])
        print("Subnet Mask:", self.data['subnet'], "\nMask:", self.data['mask'])
        print("First IP of Network or Default Gateway:", self.data['first_ip_address'])
        print("Last IP of Network:", self.data['last_ip_address'])
        print("Total IPs in Network:", self.data['number_of_ip_addresses'])


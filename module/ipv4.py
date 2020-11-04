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


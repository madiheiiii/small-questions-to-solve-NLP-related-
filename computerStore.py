import re
class ComputerStore:
    def __init__(self, GHz, diskSpace, price):
        self.GHz = ""
        self.diskSpace = ""
        self.price = ""
        self.add_GHz(GHz)
        self.add_diskSpace(diskSpace)
        self.add_price(price)


    def add_GHz (self, GHz):
        pattern = r"\b[6-9]([0-9]*)(\.[0-9]+)? *(GHz|[Gg]iga[Hh]ertz)"
        if re.match(pattern, str(GHz)):
            self.GHz + GHz
        else:
            raise ValueError("GHz must be 6 GHz or more")
        
    def add_diskSpace(self, diskSpace):
        pattern = r"\b[5-9]([00]|[0-9]+)(\.[0-9]+)? *(GB|[Gg]igabyte)"
        if re.match(pattern, str(diskSpace)):
            self.diskSpace + diskSpace
        """else:
            raise ValueError("Disk space must be greater than 500 GB")"""

    def add_price (self, price):
        pattern = r"(^/W)$[0-9]{1, 3}(\.[0-9][0-9])?\b"
        if re.match(pattern, str(price)):
            self.price + price
        """else:
            raise ValueError("Price must be something like $444.34 or $45")"""
        

        
my_computer = ComputerStore("6.5 GHz", "1000 GB", "1200.00")
print(f"Computer Specs: {my_computer.GHz}, {my_computer.diskSpace}, ${my_computer.price}")
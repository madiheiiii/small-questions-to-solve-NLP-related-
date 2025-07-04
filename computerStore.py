import re
class ComputerStore:
    def __init__(self, GHz, diskSpace, price):
        self.price = price
        self.diskSpace = [diskSpace]
        self.GHz= [GHz]


    def add_GHz (self, price):
        pattern = r"(/(^/W)$[0-9]{1, 3}(\.[0-9][0-9])?\b)"
        if re.match(pattern, str(price)):
            self.GHz.append(price)
        else:
            raise ValueError("GHz must be a the price such as $444.34 or $45")
        
    def add_diskSpace(self, diskSpace):
        pattern = r"(\b[5-9]([00]|[0-9]+)(\.[0-9]+)? *(GB|[G/g]igabyte))"
        if re.match(pattern, str(diskSpace)):
            self.diskSpace.append(diskSpace)
        else:
            raise ValueError("Disk space must be greater than 500 GB")
        
    def add_GHz (self, GHz):
        pattern = r"(\b[6-9][0-9]+(\.[0-9]+)? *(GHz|[G/g]iga[H\h]ertz))"
        if re.match(pattern, str(GHz)):
            self.GHz.append(GHz)
        else:
            raise ValueError("GHz must be 6 GHz or more")
        
    my_computer = ComputerStore(6.5, 1000, 1200.00)
    print(f"Computer Specs: {my_computer.GHz}, {my_computer.diskSpace}, ${my_computer.price}")
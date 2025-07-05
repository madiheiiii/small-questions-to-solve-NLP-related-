import re
GHz = "6.5 GHz"
diskSpace = "1000 GB"
price = "1200.00"
pattern1 = r"\b[6-9]([0-9]*)(\.[0-9]+)? *(GHz|[Gg]iga[Hh]ertz)"
pattern2 = r"\b[5-9]([00]|[0-9]+)(\.[0-9]+)? *(GB|[Gg]igabyte)"
pattern3 = r"(^/W)$[0-9]{1, 3}(\.[0-9][0-9])?\b"
if re.match(pattern1, str(GHz)):
    if re.match(pattern2, str(diskSpace)):
        if re.match(pattern3, str(price)):
            print(f"Computer Specs: {GHz}, {diskSpace}, ${price}")
        else:
            raise ValueError("Price must be something like $444.34 or $45")
    else:
        raise ValueError("Disk space must be greater than 500 GB")
else:
    raise ValueError("GHz must be 6 GHz or more")
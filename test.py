import re
GHz = "6.5 GHz"
pattern = r"\b[6-9]([0-9]*)(\.[0-9]+)? *(GHz|[Gg]iga[Hh]ertz)"
if re.match(pattern, str(GHz)):
    print("Valid GHz format")
else:
    raise ValueError("GHz must be 6 GHz or more")
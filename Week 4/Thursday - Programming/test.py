import string

#!/usr/bin/env python3

for a in string.ascii_lowercase:
    for b in string.ascii_lowercase:
        if a != b:
            print(f"{a}{b}")

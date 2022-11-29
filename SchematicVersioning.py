import re

def isValid(string):
# - each N is made entirely of digits
# - each N is non-empty
# - each N has no extraneous leading zeroes
# - at least one N is not "0"

    parts = string.split(".")
    pattern = '^[0-9]+$'
    zero_count = 0
    for part in parts:
        result = re.fullmatch(pattern, part)
        # if not match, it contains letters
        if not result:
            return False
        else:
            # this token is just one 0
            if part.startswith("0"):
                if len(part) < 2:
                    zero_count += 1
                else:
                    return False

    return True if zero_count < len(parts) - 1 else False


def isBefore(v1, v2):
# - v1 and v2 are guaranteed to be strings.
# - Throw or return an error if either v1 or v2 is not a valid Schematic Version.
# - Otherwise, return true if v1 comes before v2 in Schematic Version ordering, and false otherwise.
    if not isValid(v1) or not isValid(v2):
        return "v1 or v2 is not valid"
    
    v1_parts = v1.split(".")
    v2_parts = v2.split(".")

    if len(v1_parts) < len(v2_parts):
        for _ in range(len(v2_parts) - len(v1_parts)):
            v1_parts.append(0)
    elif len(v2_parts) < len(v1_parts):
        for _ in range(len(v1_parts) - len(v2_parts)):
            v2_parts.append(0)

    for i, j in zip(v1_parts, v2_parts):
        if int(i) < int(j):
            return True
        elif int(i) > int(j):
            return False
        else:
            continue
    
print(isBefore("5.4", "5.3.1"))
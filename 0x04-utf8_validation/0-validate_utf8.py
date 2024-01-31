#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_follow = 3
            else:
                return False

        else:
            if (byte >> 6) == 0b10:
                bytes_to_follow -= 1
            else:
                return False

    return bytes_to_follow == 0

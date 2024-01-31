#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    def is_following_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        current_byte = data[i]

        if is_start_byte(current_byte):
            num_bytes = 1
            mask = 0b10000000
            while (current_byte & mask):
                num_bytes += 1
                mask >>= 1

            for j in range(1, num_bytes):
                i += 1
                if i >= len(data) or not is_following_byte(data[i]):
                    return False
        else:
            return False

        i += 1

    return True

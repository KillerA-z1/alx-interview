#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes (0 <= integer <= 255)

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Get the least significant 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 7) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check that the byte is of the form 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

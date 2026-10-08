#!/usr/bin/python3
"""UTF-8 Validation"""


def count_ones(byte):
    """Count the consecutive 1 bits at the start of an 8-bit number"""
    count = 0
    mask = 0b10000000
    while byte & mask:
        count += 1
        mask >>= 1
    return count


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding"""
    remaining = 0

    for d in data:
        byte = d & 0xFF
        ones = count_ones(byte)

        if remaining == 0:
            if ones == 0:
                continue
            if ones == 1 or ones > 4:
                return False
            remaining = ones - 1
        else:
            if ones != 1:
                return False
            remaining -= 1

    return remaining == 0

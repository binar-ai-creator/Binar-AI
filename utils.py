# utils.py

def bin_to_decimal(binary_str):
    """Converts a binary number to a decimal number"""
    return int(binary_str, 2)

def decimal_to_bin(decimal_num):
    """Converts a decimal number to a binary number"""
    return bin(decimal_num)[2:]

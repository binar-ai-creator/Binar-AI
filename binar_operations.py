# binar_operations.py

def bin_add(bin1, bin2):
    """Adds two binary numbers."""
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def bin_subtract(bin1, bin2):
    """Subtracts two binary numbers."""
    return bin(int(bin1, 2) - int(bin2, 2))[2:]

def bin_multiply(bin1, bin2):
    """Multiplies two binary numbers."""
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def bin_divide(bin1, bin2):
    """Divides two binary numbers."""
    try:
        return bin(int(bin1, 2) // int(bin2, 2))[2:]
    except ZeroDivisionError:
        return "Error: Division by zero"

def bin_modulo(bin1, bin2):
    """Finds the modulo of two binary numbers."""
    return bin(int(bin1, 2) % int(bin2, 2))[2:]

def bin_and(bin1, bin2):
    """Performs a bitwise AND operation on two binary numbers."""
    return bin(int(bin1, 2) & int(bin2, 2))[2:]

def bin_or(bin1, bin2):
    """Performs a bitwise OR operation on two binary numbers."""
    return bin(int(bin1, 2) | int(bin2, 2))[2:]

def bin_xor(bin1, bin2):
    """Performs a bitwise XOR operation on two binary numbers."""
    return bin(int(bin1, 2) ^ int(bin2, 2))[2:]

def bin_not(bin1):
    """Performs a bitwise NOT operation on a binary number."""
    return bin(~int(bin1, 2) & (2 ** len(bin1) - 1))[2:]

def bin_to_decimal(binary_str):
    """Converts a binary number to decimal."""
    return int(binary_str, 2)

def decimal_to_bin(decimal_num):
    """Converts a decimal number to binary."""
    return bin(decimal_num)[2:]

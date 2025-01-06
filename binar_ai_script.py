# binar_ai.py

import sys

def bin_add(bin1, bin2):
    """Adds two binary numbers"""
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def bin_subtract(bin1, bin2):
    """Subtracts two binary numbers"""
    return bin(int(bin1, 2) - int(bin2, 2))[2:]

def bin_multiply(bin1, bin2):
    """Multiplies two binary numbers"""
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def bin_divide(bin1, bin2):
    """Divides two binary numbers"""
    try:
        return bin(int(bin1, 2) // int(bin2, 2))[2:]
    except ZeroDivisionError:
        return "Error: Division by zero"

if __name__ == "__main__":
    # Example Usage
    if len(sys.argv) < 4:
        print("Usage: python binar_ai.py <operation> <bin1> <bin2>")
        sys.exit(1)
    
    operation = sys.argv[1]
    bin1 = sys.argv[2]
    bin2 = sys.argv[3]

    if operation == "add":
        result = bin_add(bin1, bin2)
    elif operation == "subtract":
        result = bin_subtract(bin1, bin2)
    elif operation == "multiply":
        result = bin_multiply(bin1, bin2)
    elif operation == "divide":
        result = bin_divide(bin1, bin2)
    else:
        print("Invalid operation. Use add, subtract, multiply, or divide.")
        sys.exit(1)

    print(f"Result: {result}")

def binary_to_decimal(binary_str):
    # Validate input: Only 0s and 1s allowed
    if not all(char in '01' for char in binary_str):
        return "Error: Only binary digits (0 and 1) are allowed."
    
    # Convert binary to decimal using int() with base 2
    decimal_value = int(binary_str, 2)
    return f"Decimal Equivalent: {decimal_value}"

def decimal_to_binary(decimal_str):
    # Validate input: Only numeric values allowed
    if not decimal_str.isdigit():
        return "Error: Only numeric values are allowed."
    
    # Convert decimal to binary using bin()
    binary_value = bin(int(decimal_str))[2:]
    return f"Binary Equivalent: {binary_value}"

# Get user choice
choice = input("Choose conversion type:\n1. Binary to Decimal\n2. Decimal to Binary\nEnter 1 or 2: ")

if choice == "1":
    binary_input = input("Enter a binary number (up to 8 digits): ")
    if len(binary_input) > 8:
        print("Error: Input must be at most 8 binary digits.")
    else:
        print(binary_to_decimal(binary_input))
elif choice == "2":
    decimal_input = input("Enter a decimal number: ")
    print(decimal_to_binary(decimal_input))
else:
    print("Error: Invalid choice. Please enter 1 or 2.")

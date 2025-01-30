def binary_to_decimal(binary_str):
    # Validate input: Only 0s and 1s allowed
    if not all(char in '01' for char in binary_str):
        return "Error: Only binary digits (0 and 1) are allowed."
    
    # Convert binary to decimal using int() with base 2
    decimal_value = int(binary_str, 2)
    return f"Decimal Equivalent: {decimal_value}"

# Get user input
binary_input = input("Enter a binary number (up to 8 digits): ")

# Limit input length to 8 characters
if len(binary_input) > 8:
    print("Error: Input must be at most 8 binary digits.")
else:
    print(binary_to_decimal(binary_input))

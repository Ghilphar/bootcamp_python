import sys

def arithmetic_operations(A, B):
    # Check if both arguments are integers
    if not isinstance(A, int) or not isinstance(B, int):
        print("Error: Both arguments must be integers.")
        return
    
    # Perform arithmetic operations
    try:
        print("Sum: {}".format(A + B))
        print("Difference: {}".format(A - B))
        print("Product: {}".format(A * B))
        print("Quotient: {}".format(A / B))
        print("Remainder: {}".format(A % B))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

# Check for correct number of arguments
#if len(sys.argv) == 3:
#    # Parse command-line arguments
#    try:
#        A = int(sys.argv[1])
#        B = int(sys.argv[2])
#    except ValueError:
#        print("Error: Both arguments must be integers.")
#    else:
#        arithmetic_operations(A, B)
#else:
#    print("Usage: python program_name.py A B")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        # Parse command-line arguments
        try:
            A = int(sys.argv[1])
            B = int(sys.argv[2])
        except ValueError:
            print("Error: Both arguments must be integers.")
        else:
            arithmetic_operations(A, B)
    else:
        print("Usage: python program_name.py A B")
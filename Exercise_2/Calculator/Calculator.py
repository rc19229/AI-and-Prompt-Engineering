import sys

def main():
    # Check if the correct number of arguments is provided
    # print(sys.argv)
    
    if len(sys.argv) < 4:
        print("Usage: python calc.py <operation> <num1> <num2>")
        sys.exit(1)

    op = sys.argv[1]  # Operation: add, sub, mul, div

    # Try to change input numbers to float
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)

    # Perform the requested operation
    if op == "add":
        print(num1 + num2)
    elif op == "sub":
        print(num1 - num2)
    elif op == "mul":
        print(num1 * num2)
    elif op == "div":
        if num2 == 0:
            print("Error: Division by zero.")  # Handle division by zero
        else:
            print(num1 / num2)
    else:
        print("Unknown operation. Use add, sub, mul, or div.")  # Handle invalid operation

if __name__ == "__main__":
    main()  # Run the main function
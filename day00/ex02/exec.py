import sys

def isEvenOrOdd(number):
    if number == 0:
        print("I'm Zero.")
    elif (number % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main():
    if len(sys.argv) == 2:
        try:
            num = int(sys.argv[1])
            isEvenOrOdd(num)
        except ValueError:
            print("AssertionError: argument is not an integer")
    else:
        if len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
        else:
            print("Usage: python program.py <number>")

if __name__ == '__main__':
    main()
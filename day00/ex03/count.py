import string
import sys


def text_analyzer(text=None):
    if text is None:
        text = input("What is the text to analyze?\n")

    if not isinstance(text, str):
        raise AssertionError("Argument is not a string")

    upper_count = 0
    lower_count = 0
    punct_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punct_count += 1
        elif char.isspace():
            space_count += 1

    print(f"The text contains {len(text)} character(s):")
    print(f"- {upper_count} upper letter(s)")
    print(f"- {lower_count} lower letter(s)")
    print(f"- {punct_count} punctuation mark(s)")
    print(f"- {space_count} space(s)")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Error: too many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
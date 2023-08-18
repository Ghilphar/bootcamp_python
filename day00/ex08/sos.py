import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    ' ': '/'
}

def encode_to_morse(input_string):
    try:
        return ' '.join((MORSE_CODE_DICT[char.upper()] for char in input_string))
    except KeyError:
        return "ERROR"

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 sos.py <string to encode>")
        return
    input_string = ' '.join(args)
    morse_code = encode_to_morse(input_string)
    print(morse_code)

if __name__ == "__main__":
    main()
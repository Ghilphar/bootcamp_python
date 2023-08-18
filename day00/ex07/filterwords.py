import sys
import string

def filter_words(s, n):
    words = s.translate(str.maketrans('', '', string.punctuation)).split()

    filtered_words = [word for word in words if len(word) > n]
    return filtered_words

def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print("ERROR")
        return
    
    try:
        n = int(args[1])
        words = filter_words(args[0], n)
        print(words)
    except ValueError:
        print("ERROR")

if __name__ == "__main__":
    main()
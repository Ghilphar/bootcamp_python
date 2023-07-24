kata = (19,42,21)

def print_tuple(tup):
    if type(kata) == int:
        print(f"The 1 number is: {kata}")
    elif all(isinstance(item, (int)) for item in tup):
        print(f"The {len(tup)} numbers are: {', '.join(map(str, tup))}")
    else:
        print("The tuple contains non-numeric values.")

if __name__ == '__main__':
    print_tuple(kata)
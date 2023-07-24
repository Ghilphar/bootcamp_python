import sys

def main():
	if len(sys.argv) > 1:
		original_string = ' '.join(sys.argv[1:])
		reversed_string = original_string[::-1]
		
		swapped_case_string = reversed_string.translate(str.maketrans(
			'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
			'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
		))
		print(swapped_case_string)
	else:
	    print("Please provide at least one argument.")
    
if __name__ == '__main__':
    main()
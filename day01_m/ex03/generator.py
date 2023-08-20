import random


def unique_ordered(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def custom_shuffle(lst):
    n = len(lst)

    for i in range(n):
        j = random.randint(0, n-1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    '''
    options = ["ordered", "shuffle", "unique"]

    if not isinstance(text, str):
        return ["ERROR"]
    if option and option not in options:
        return ["ERROR"]
    
    substrings = text.split(sep)

    if option == "shuffle":
        print("With shuffle.")
        substrings = custom_shuffle(substrings.copy())
    elif option == "unique":
        print("With unique.")
        substrings = unique_ordered(substrings)
    elif option == "ordered":
        print("With ordered.")
        substrings.sort()

    for s in substrings:
        yield s

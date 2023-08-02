import random

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

    resultList = text.split(sep)
    if option == "ordered":
        resultList = sorted(resultList)
    elif option == "shuffle":
        for i in range(0, len(resultList) - 1):
            j = random.randrange(0, len(resultList))
            resultList[i], resultList[j] = resultList[j], resultList[i]
    elif option == "unique":
        resultList = list(set(resultList))
    return resultList
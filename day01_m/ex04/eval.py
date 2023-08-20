class Evaluator:
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            raise TypeError("words and coefs should from type list.")
        if len(coefs) != len(words):
            return -1
        myList = zip(coefs, words)
        sum = 0
        for coef, word in myList:
            sum += len(word) * coef
        return sum

    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            raise TypeError("words and coefs should from type list.")
        if len(coefs) != len(words):
            return -1
        sum = 0
        for index, coef in enumerate(coefs):
            sum += len(words[index]) * coef
        return sum
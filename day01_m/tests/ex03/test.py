from generator import generator

test_results = []
text = "Le Lorem Ipsum est simplement du faux faux texte."


result1 = []
for word in generator(text, sep=" "):
    print(word)

print('\n')

result2 = []
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

print('\n')


result3 = []
for word in generator(text, sep=" ", option="ordered"):
    print(word)

print('\n')


result4 = []
for word in generator(text, sep=" ", option="unique"):
    print(word)
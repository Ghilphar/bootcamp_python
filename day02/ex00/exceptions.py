from ft_map import ft_map

numbers = [1, 2, 3]

def add_number_5(aNumber):
    if isinstance(aNumber, (int, float)):
        return aNumber + 5
    else:
        raise Exception("aNumber Is not a number")


print("Exception map: ")
try:
    result = list(map(15, "numbers"))
    print(result)
except Exception as e:
    print("map exception")
    print(e)

print("My ft_map exception")
try:
    result = list(ft_map(15, "numbers"))
    print*(result)
except Exception as e:
    print("my exception")
    print(e)

print("Exception map: ")
try:
    result = list(map(add_number_5, "str"))
    print(result)
except Exception as e:
    print("map exception")
    print(e)

print("My ft_map exception")
try:
    result = list(ft_map(add_number_5, "str"))
    print*(result)
except Exception as e:
    print("my exception")
    print(e)
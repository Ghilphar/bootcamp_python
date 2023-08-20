from functools import reduce
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce


#Basicly theses 3 functions take an iterable tab in entry and a function.
'''
But they erxpect differents outputs.
Filter expect a Booleand function.
    With a boolean function he cna createa new list with 
    the ones who returned True to this function.

    Filter return a filter object

Map expect a function who will return the same type.
    Map will apply this function to all the elements of the list.
    And will store on a new list the elements of the results transformed.

    Map return a map object

Reduce expect a function who will return the argument of the next function and take 2 arguments.
    Reduce will apply the function to next element of the list.
    But it will use the last result as second argument.
    Also for the first iteration it will take first and second argument. (0, 1)

    Reduce return the same type

'''



# Define a function that doubles a number
print("\n%s in action\n" % "Map")

def double(x):
    return x * 2

def add_number_5(aNumber):
    if isinstance(aNumber, (int, float)):
        return aNumber + 5
    else:
        raise Exception("aNumber Is not a number")

# Apply the function to each element in the list using map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))
#doubled_numbers = list(map(double, True))
print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# Apply the function to each element in the list using map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(ft_map(double, numbers))
#doubled_numbers = list(ft_map(add_number_5, "str"))
#doubled_numbers = list(ft_map(double, True))

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]


# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Apply the function to each element in the list using map
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))
print(temperatures_fahrenheit)

# Apply my function to each element in the list using map
temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = list(ft_map(celsius_to_fahrenheit, temperatures_celsius))
print(temperatures_fahrenheit)

# Output: [32.0, 50.0, 68.0, 86.0, 104.0]

print('\n%s in action\n' % "Reduce")


# Define a function that adds two numbers
def add(x, y):
    return x + y # + 1

def max_of_two(x, y):
    return x if x > y else y

# Apply the function cumulatively to the elements in the list using reduce
numbers = [1, 2, 3, 4, 5]#, "ewr"]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15 (1 + 2 + 3 + 4 + 5)

sum_of_numbers = ft_reduce(add, numbers)
print(sum_of_numbers)  # Output: 15 (1 + 2 + 3 + 4 + 5)

# Find the maximum value in the list using reduce
numbers = [23, 8, 15, 42, 16, 4]
max_value = reduce(max_of_two, numbers)
print(max_value)  # Output: 42

max_value = ft_reduce(max_of_two, numbers)
print(max_value)  # Output: 42


print("\n%s in action\n" % "Filter")
# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Define a function to check if an element is the first occurrence in the list
def is_first_occurrence(element):
    return numbers.count(element) == 1

# Filter out the even numbers from the list using filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

even_numbers = list(ft_filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 7]
unique_numbers = list(filter(is_first_occurrence, numbers))
print(unique_numbers)  # Output: [1, 3, 6]

unique_numbers = list(ft_filter(is_first_occurrence, numbers))
print(unique_numbers)  # Output: [1, 3, 6]

#lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
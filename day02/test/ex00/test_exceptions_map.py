# First, let's import the ft_map function from the provided code
from ft_map import ft_map
# Define the test functions
def test_exceptions():
    test_cases = [
        (123, [1, 2, 3]),  # non-callable function
        (lambda x: x, 123),  # non-iterable object
        (lambda x: x / 0, [1, 2, 3])  # error during function execution
    ]
    
    results = []
    for func, iterable in test_cases:
        ft_exception = None
        built_in_exception = None
        
        # Test ft_map
        try:
            list(ft_map(func, iterable))
        except Exception as e:
            ft_exception = str(e)
        
        # Test built-in map
        try:
            list(map(func, iterable))
        except Exception as e:
            built_in_exception = str(e)
        
        results.append((ft_exception, built_in_exception))
    
    return results

print(test_exceptions())
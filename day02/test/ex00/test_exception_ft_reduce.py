from ft_reduce import ft_reduce
from functools import reduce 

def test_updated_reduce_exceptions():
    test_cases = [
        (123, [1, 2, 3]),  # non-callable function
        (lambda x, y: x + y, 123),  # non-iterable object
        (lambda x, y: x / 0, [1, 2, 3]),  # error during function execution
        (lambda x, y: x + y, [])  # empty iterable
    ]
    
    results = []
    for func, iterable in test_cases:
        ft_exception = None
        built_in_exception = None
        
        # Test updated ft_reduce
        try:
            ft_reduce(func, iterable)
        except Exception as e:
            ft_exception = str(e)
        
        # Test functools.reduce
        try:
            reduce(func, iterable)
        except Exception as e:
            built_in_exception = str(e)
        
        results.append((ft_exception, built_in_exception))
    
    return results

print(test_updated_reduce_exceptions())
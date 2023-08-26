from ft_filter import ft_filter

# Define the test functions for ft_filter
def test_filter_exceptions():
    test_cases = [
        (123, [1, 2, 3]),  # non-callable function
        (lambda x: x, 123),  # non-iterable object
        (lambda x: x / 0, [1, 2, 3]),  # error during function execution
        (lambda x: x, [1, 'a', 3])  # function returns non-boolean (for comparison with built-in filter)
    ]
    
    results = []
    for func, iterable in test_cases:
        ft_exception = None
        built_in_exception = None
        
        # Test ft_filter
        try:
            list(ft_filter(func, iterable))
        except Exception as e:
            ft_exception = str(e)
        
        # Test built-in filter
        try:
            list(filter(func, iterable))
        except Exception as e:
            built_in_exception = str(e)
        
        results.append((ft_exception, built_in_exception))
    
    return results

print(test_filter_exceptions())
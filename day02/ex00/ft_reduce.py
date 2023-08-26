def ft_reduce(function_to_apply, iterable):
    """
    Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise Exception(f"{type(function_to_apply)} object is not callable")
    try:
        iterator = iter(iterable)
    except Exception as e:
        raise Exception(f"{iterable} object is not an iterable.")
    try:
        value = next(iterator)
    except:
        return None
    for element in iterator:
        try:
            value = function_to_apply(value, element)
        except Exception as e:
            return None
    
    return value


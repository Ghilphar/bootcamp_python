import pprint

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
        value = iterable[0]
        for element in iterable[1:]:
            try:
                value = function_to_apply(value, element)
            except Exception:
                return None
        return value
    except TypeError:
        return None

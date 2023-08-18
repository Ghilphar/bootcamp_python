def ft_map(function_to_apply, iterable):
    """
    Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    try:
        result = []
        for element in iterable:
            result.append(function_to_apply(element))
        return result
        #for i in iterable:
        #    yield function_to_apply(i)
    except TypeError:
        return None
    
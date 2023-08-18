def ft_filter(function_to_apply, iterable):
    """
    Filter the result of function apply to all elements of the iterable.
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
            bool = function_to_apply(element)
            if bool:
                result.append(element)
        return result
        #for i in iterable:
        #    if function_to_apply(i):
        #        yield i
    except TypeError:
        return None
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
    if not callable(function_to_apply):
        raise Exception(f"{type(function_to_apply)} object is not callable")
    try:
        iter(iterable)
    except Exception as e:
        raise Exception(f"{iterable} object is not an iterable.")
    try:
        for i in iterable:
            try:
                if function_to_apply(i):
                    yield i
            except Exception:
                return None
    except TypeError:
        return None
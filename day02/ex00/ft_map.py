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
    if not callable(function_to_apply):
        raise Exception(f"{type(function_to_apply)} object is not callable")
    try:
        some_object_iterator = iter(iterable)
    except Exception as e:
        raise e

    #try:
    for i in iterable:
        try:
            yield function_to_apply(i)
        except Exception as e:
            #print("here")
            return None
    #except TypeError:
    #    return None
    
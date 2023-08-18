import numpy as np

class NumPyCreator:
    def from_list(self, a_list, dtype=None):
        '''
        Convert a list or nested list into a NumPy array
        '''
        if not isinstance(a_list, list) or not all(isinstance(sub, list) for sub in a_list):
            return None
        try:
            arr = np.array(a_list, dtype=dtype)
            if arr.dtype == object:
                return None
            return arr
        except ValueError:
            return None
    
    def from_tuple(self, a_tuple, dtype=None):
        '''
        Convert a tuple or nested tuples into a NumPy array
        '''
        if isinstance(a_tuple, tuple):
            return np.array(a_tuple, dtype=dtype)
        return None
    
    def from_iterable(self, a_iterable, dtype=None):
        '''
        Convert any iterable object into NumPy array 
        '''
        return np.array(list(a_iterable), dtype)
    
    def from_shape(self, a_shape, value=0, dtype=None):
        '''
        Creates a NumPy array with the given shape and fills it with specified value
        '''
        return np.full(a_shape, value, dtype=dtype)
    
    def random(self, shape, dtype=None):
        '''
        Creates a NumPy array with the given shape and fills it with random values between 0 and 1
        '''
        return np.random.rand(*shape).astype(dtype) if dtype else np.random.rand(*shape)
    
    def identity(self, n, dtype=None):
        '''
        Creates a NumPy identity matrix of size n
        '''
        return np.identity(n, dtype=dtype)
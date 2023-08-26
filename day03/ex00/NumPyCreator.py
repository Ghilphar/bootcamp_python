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
        if isinstance(a_tuple, tuple) :
            try:
                arr = np.array(a_tuple, dtype=dtype)
            except:
                return None
            if arr.dtype == np.object:
                return None
            return arr
        return None
    
    def from_iterable(self, a_iterable, dtype=None):
        '''
        Convert any iterable object into NumPy array 
        '''
        if iter(a_iterable):
            try: 
                arr = np.array(list(a_iterable), dtype)
                return arr
            except:
                return None
        else:
            return None
    
    def from_shape(self, a_shape, value=0, dtype=None):
        '''
        Creates a NumPy array with the given shape and fills it with specified value
        '''
        try:
            arr = np.full(a_shape, value, dtype=dtype)
            return arr
        except:
            return None
    
    def random(self, shape, dtype=None):
        '''
        Creates a NumPy array with the given shape and fills it with random values between 0 and 1
        '''
        if dtype:
            try:
                arr = np.random.rand(*shape).astype(dtype)
            except:
                return None
        else:
            try:
                arr = np.random.rand(*shape)
            except:
                return None
        return arr
        #return np.random.rand(*shape).astype(dtype) if dtype else np.random.rand(*shape)
    
    def identity(self, n, dtype=None):
        '''
        Creates a NumPy identity matrix of size n
        '''
        try:
            arr = np.identity(n, dtype=dtype)
            return arr
        except:
            return None
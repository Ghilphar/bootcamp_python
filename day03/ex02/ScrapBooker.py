import numpy as np

class ScrapBooker:

    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) or not isinstance(position, tuple) or \
            len(position) != 2 or len(dim) != 2:
            return None
        
        # Extract Position point of new array
        start_row = position[0]
        start_column = position[1]
        # Extract dimension of new array
        number_of_row = dim[0]
        number_of_columns = dim[1]
        # Compute The ending row and column of new array
        end_row = start_row + number_of_row
        end_col = start_column + number_of_columns
        # Extract number of row and columns of old array
        array_rows = array.shape[0]
        array_columns = array.shape[1]
        # Check if the end row and end column exist on the array
        if end_row > array_rows or end_col > array_columns:
            return None
        
        # Crop the old Array into a new one.
        cropped_array = array[start_row:end_row, start_column:end_col] 
        return cropped_array
    
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or n <= 0 or n > array.shape[axis] or axis not in [0,1]:
            return None

        indice_start = n - 1
        if axis == 1:
            #Working on deleting rows
            number_of_rows = array.shape[1 - axis] # array.shape[0] = number_of_rows
            # Extracting indices to delete
            indices_to_delete = np.arange(indice_start, number_of_rows, n)
            thinned_array = np.delete(array, indices_to_delete, axis=0)
        elif axis == 0:
            # Working on deleting columns
            number_of_columns = array.shape[1 - axis] # array.shape[1] = number_of_columns
            # Extracting indices to delete
            indices_to_delete = np.arange(indice_start, number_of_columns, n)
            thinned_array = np.delete(array, indices_to_delete, axis=1)
        
        return thinned_array
    
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or n <= 0 or axis not in [0, 1]:
            return None

        # Multiply the array on the desired axis
        juxtaposed_array = np.concatenate([array] * n, axis=axis)
        return juxtaposed_array
    
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) or len(dim) != 2 or \
            dim[0] <= 0 or dim[1] <= 0:
            return None
        
        mosaic_array = np.tile(array, dim)
        return mosaic_array
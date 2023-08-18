import numpy as np

class ScrapBooker:

    def crop(self, array, dim, position=(0, 0)):
        """Return a cropped version of the input array based on the specified dimensions and position."""

        end_row = position[0] + dim[0]
        end_col = position[1] + dim[1]

        if end_row > array.shape[0] or end_col > array.shape[1]:
            return None
        
        cropped_array = array[position[0]:end_row, position[1]:end_col] 
        return cropped_array
    
    def thin(self, array, n, axis):
        """Delete every n-th pixel/row/column (depending on axis) from the array."""

        if n <= 0 or n > array.shape[axis] or axis not in [0, 1]:
            return None
        indices_to_delete = np.arange(n - 1, array.shape[1 - axis], n)
        thinned_array = np.delete(array, indices_to_delete, axis=1) if axis == 0 else np.delete(array, indices_to_delete, axis=0)
        # Use slicing to keep every n-th line pixels along the specified axis, and delete the rest
        return thinned_array
    
    def juxtapose(self, array, n, axis):
        """Replicate the input array n times along the specified axis."""

        if n <= 0 or axis not in [0, 1]:
            return None
        juxtaposed_array = np.concatenate([array] * n, axis=axis)
        return juxtaposed_array
    
    def mosaic(self, array, dim):
        """Create a mosaic of the input array based on the specified dimensions."""
        
        if dim[0] <= 0 or dim[1] <= 0:
            return None
        mosaic_array = np.title(array, dim)
        return mosaic_array
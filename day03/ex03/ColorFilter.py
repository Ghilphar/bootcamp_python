import numpy as np

class ColorFilter:
    def invert(self, array):
        """Invert the color of the image"""
        array_rgb = array[:, :, :3]

        inverted_array = array_rgb.copy()


        if array.dtype == np.float32 or array.dtype == np.float64:
            inverted_array = 1.0 - inverted_array
        else:
            inverted_array = 255 - inverted_array

        return inverted_array
    
    def to_blue(self, array):
        """Applies a blue filter to the image"""
        blue_filtered_array = array.copy()
        blue_filtered_array[:, :, 0] = 0
        blue_filtered_array[:, :, 1] = 0 
        return blue_filtered_array
    
    def to_green(self, array):
        """Applies a green filter to the image"""
        green_filtered_array = array.copy()
        green_filtered_array[:, :, 0] = 0
        green_filtered_array[:, :, 2] = 0
        return green_filtered_array
    
    def to_red(self, array):
        """Applies a red filter to the array"""
        red_filtered_array = array.copy()
        red_filtered_array[:, :, 1] = 0
        red_filtered_array[:, :, 2] = 0
        return red_filtered_array
    
    def to_celluloid(self, array):
        """Applies a celluloid filter to the image"""
        celluloid_array = array.copy()

        # Define the color threshold for the celluloid filter
        min_val, max_val = celluloid_array.min(), celluloid_array.max()
        thresholds = np.linspace(min_val, max_val, 5)

        # Apply the thresolds
        for i in range(1, len(thresholds)):
            mask = ((celluloid_array > thresholds[i-1]) & (celluloid_array <= thresholds[i]))
            celluloid_array[mask] = thresholds[i] - (thresholds[1] / 2)
        return celluloid_array
    
    def to_grayscale(self, array, filter, **kwargs):
        """Applies a greyscale filter to the image."""

        array_rgb = array[:, :, :3]

        if filter in ["mean", "m"]:
            grayscale_array = array_rgb.sum(axis=2, keepdims = True) / 3.0
        elif filter in ["weight", "w"]:
            if "weights" in kwargs and int(sum(kwargs["weights"])) == 1:
                weights = kwargs["weights"]
                grayscale_array = np.dot(array_rgb, weights).reshape(array_rgb.shape[0], array_rgb.shape[1], 1)
            else:
                return None
        else:
            return None
        
        grayscale_array = np.broadcast_to(grayscale_array, array_rgb.shape)
        
        return grayscale_array.astype(array_rgb.dtype)
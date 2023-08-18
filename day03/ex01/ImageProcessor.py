import numpy as np
import matplotlib.pyplot as plt
import os

class ImageProcessor:
    @staticmethod
    def load(path):
        try:
            # Test image path.
            if not os.path.exists(path):
                raise FileNotFoundError(f"FileNotFoundError -- strerror: No such file or directory {path}")
            # Test file empty:
            if os.path.getsize(path) == 0:
                raise OSError(f"OSError -- strerror: Empty file: {path}")
            # Reading the image using matplotlib can also use imageio
            image = plt.imread(path)
            
            # Check if the image is RGBA, and if so, convert it to RGB
            if image.shape[2] == 4:
                image = image[:, :, :3]

            # Displaying the dimensions
            print(f"Loading image of dimensions {image.shape[0]} x {image.shape[1]}")
            # print(f"{image.shape[0]} x {image.shape[1]}")
            
            return image.astype(np.float32)
        except FileNotFoundError as e:
            print(str(e))
            return None
        except OSError as e:
            print(str(e))
            return None
        except Exception as e:
            print(f"An error occurred while reading the image: {e}")
            return None

    @staticmethod
    def display(array):
        if array is not None:
            plt.imshow(array)
            plt.axis('off')  # Turn off axes
            plt.show()
        else:
            print("An error occurred while displaying the image.")
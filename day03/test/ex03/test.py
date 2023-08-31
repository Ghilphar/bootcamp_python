import sys
sys.path.append("..")

import numpy as np
import matplotlib.pyplot as plt
import os
from ex01.ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter  # Assuming this is the name of the file where VerifiedColorFilter is saved


def main():
    imp = ImageProcessor()
    cf = ColorFilter()

    # Load the image
    arr = imp.load("../ressources/elon_canaGAN.png")
    # Check if the image was loaded successfully
    if arr is not None:
        #Display the original image
        print("Original Image:")
        imp.display(arr)

        # Apply invert filter and display
        inverted_image = cf.invert(arr)
        print("Inverted Image:")
        imp.display(inverted_image)

        # Apply blue filter and display
        blue_image = cf.to_blue(arr)
        print("Blue Filtered Image:")
        imp.display(blue_image)

        # Apply green filter and display
        green_image = cf.to_green(arr)
        print("Green Filtered Image:")
        imp.display(green_image)

        # Apply red filter and display
        red_image = cf.to_red(arr)
        print("Red Filtered Image:")
        imp.display(red_image)

        # Apply celluloid filter and display
        celluloid_image = cf.to_celluloid(arr)
        print("Celluloid Filtered Image:")
        imp.display(celluloid_image)

        # Apply grayscale filter (mean) and display
        grayscale_mean_image = cf.to_grayscale(arr, 'mean')
        print("Grayscale (Mean) Image:")
        imp.display(grayscale_mean_image)

        # Apply grayscale filter (weighted) and display
        grayscale_weighted_image = cf.to_grayscale(arr, 'weight', weights=(0.3, 0.5, 0.2))
        print("Grayscale (Weighted) Image:")
        imp.display(grayscale_weighted_image)

    else:
        print("Failed to load the image.")

if __name__ == "__main__":
    main()
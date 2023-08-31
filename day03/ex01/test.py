
import numpy as np
from ImageProcessor import ImageProcessor

# The normalized 2x2 images
image_blue_green_normalized = [[[0.0, 0.0, 1.0], [1, 1, 1], [1, 0, 0]],
                               [[0.0, 1.0, 0.0], [1.0, 0, 0.0], [1, 1, 1]],
                               [[1, 1,1],[0.25, 0.25, 1],[0.25, 1, 0.25]]]
random_image1_normalized = [[[0.3764705882352941, 0.07058823529411765, 0.596078431372549], [0.47843137254901963, 0.8274509803921568, 0.796078431372549]], [[0.5450980392156862, 0.803921568627451, 0.21176470588235294], [0.8823529411764706, 0.6862745098039216, 0.07450980392156863]]]
random_image2_normalized = [[[0.6745098039215687, 0.8941176470588236, 0.6705882352941176], [0.2196078431372549, 0.4627450980392157, 0.8235294117647058]], [[0.19607843137254902, 0.4117647058823529, 0.9176470588235294], [0.6078431372549019, 0.28627450980392155, 0.34509803921568627]]]
random_image3_normalized = [[[0.9725490196078431, 0.8666666666666667, 0.7098039215686275], [0.7019607843137254, 0.403921568627451, 0.5137254901960784]], [[0.1568627450980392, 0.396078431372549, 0.6], [0.22745098039215686, 0.4, 0.1607843137254902]]]

# Use the ImageProcessor class to display the images
# Assuming the class has a 'display' method to show images
image_processor = ImageProcessor()

# Display the blue-green image
image_processor.display(image_blue_green_normalized)

# Display the random color images
#image_processor.display(random_image1_normalized)
#image_processor.display(random_image2_normalized)
#image_processor.display(random_image3_normalized)

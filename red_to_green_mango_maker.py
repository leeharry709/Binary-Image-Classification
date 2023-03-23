# This will make an image of a mango turn green from the bottom up in incremental steps defined by num_steps

import cv2
import numpy as np

# Load the image
img = cv2.imread('mango.jpg')

# Convert the image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of green color in HSV
lower_green = np.array([25, 52, 72])
upper_green = np.array([102, 255, 255])

# Find the green pixels in the image
mask = cv2.inRange(hsv, lower_green, upper_green)

# Normalize the mask to make it 0 or 1
mask = mask / 255

# Set the initial green value to 0
green = 0

# Define the number of steps to take
num_steps = 1000

# Define the increment of the green value for each step
step_size = 255 / num_steps

# Loop over each step
for i in range(num_steps):
    # Add the green overlay to the image
    img_with_green = img.copy()
    img_with_green[:, :, 1] = np.minimum(green + mask * step_size, 255)
    
    # Save the image with a new filename
    filename = f'mango_green_{i}.jpg'
    cv2.imwrite(filename, img_with_green)
    
    # Update the green value for the next step
    green += step_size

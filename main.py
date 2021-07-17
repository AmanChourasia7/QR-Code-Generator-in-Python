# -----------------------------
# About the Project: This is a Code written in Python to Generate String's into QR Code!
# Author: Aman Chourasia
# Website: www.amanchourasia.in
# Date of Creation: 20th May 2021
# -----------------------------
# Code Starts Here!

import pyqrcode # Imported pyqrcode Module

data = "Enter the link you want to store in QR Image" # Declaring the Variables

image = pyqrcode.create(data) # Creating a Function

image.png("image_name.png",scale=8) # Saving the Image

# Code Ends Here!

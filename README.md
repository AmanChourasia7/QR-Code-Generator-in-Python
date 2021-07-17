# QR-Code-Generator-in-Python
## Introduction
In this readme, we are going to see the demonstration of QR code Generation with the help of few python lines. Before Starting Let's Understand What is a QR code and why it is needed?.

## What Is QR Code and What is the need for QR Code?
A QR code stands for quick response code. It is a type of matrix barcode (or two-dimensional barcode). 

A QR code consists of black squares arranged in a square grid on a white background, which can be read by an imaging device such as a camera, and processed using Reed–Solomon error correction until the image can be appropriately interpreted.

The Quick Response system became popular outside the automotive industry due to its fast readability and greater storage capacity compared to standard UPC barcodes. Applications include product tracking, item identification, time tracking, document management, and general marketing

## This is the QR Code of my YouTube Channel You can scan it to check!

![QR Code of my YouTube Channel](https://user-images.githubusercontent.com/76176138/126047396-a3bef30a-c98f-410e-b1b8-d5cfd2e9353b.png)

## Implementation
To generate a QR code we are going to use two libraries PyQRCode and pypng libraries.

You need to install them first on your local device by command:

```python
pip install PyQRCode pypng
```

After the installation of these two modules. let's use them by importing.

```python
import pyqrcode # Imported pyqrcode
data = "Enter the link you want to store in QR Image" # Declaring the Variables
image = pyqrcode.create(data) # Creating a Function
image.png("image_name.png",scale=8) # Saving the Image
```
## Video Tutorial

[![QR Code Generator in Python](https://img.youtube.com/vi/Q6Qi4cN6POg/0.jpg)](https://www.youtube.com/watch?v=Q6Qi4cN6POg)

## Conclusion

The scale parameter tells you the size/Resolution of the png image.

The above QR code is of scale=8

So, This is how you can Generate QR Code in Python. I hope you ❤️ This repository.

-----------------------------

Author: Aman Chourasia
Website: www.amanchourasia.in

Date of Creation: 20th May 2021

Post Link: https://www.amanchourasia.in/2021/05/generate-qr-code-with-3-lines-of-code-in-python.html

-----------------------------



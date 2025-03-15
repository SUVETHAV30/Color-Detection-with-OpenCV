

Color Detection using OpenCV and HSV Colorspace

Overview:
This project is a Python-based application that detects colors using OpenCV and the HSV color space. It allows users to identify specific colors in images or live video feeds using color thresholding and contour detection techniques.

Features:
Detects and highlights specific colors in an image or video feed.
Uses HSV color space for better color segmentation.
Adjustable color range for precise detection.
Real-time processing with OpenCV.

Technologies Used:
Python
OpenCV
NumPy

Run the script:
python color_detection.py
Adjust the HSV range in the script to detect specific colors.
The program will display the processed video feed with detected colors highlighted.

How It Works:
The image is converted from BGR to HSV color space.
A color threshold is applied using cv2.inRange() to isolate the desired color.
Contours are detected and drawn to highlight the selected color regions.

## 📽 Project Demo  
[Click here to watch the demo](https://github.com/your-username/your-repo/blob/main/demo.mp)


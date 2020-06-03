
# Calibrate to 4 points on a flat surface
# Track a particular colour
# Save down the images
# Project back the images onto the surface
# Result is drawing on a flat surface with a coloured fingernail without dirtying the surface


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# List of colours to detect
# e.g. orange, purple
myColours = [(5,107,0,19,255,255),
			(133,56,0,159,156,255)]

def find_color(img):
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(imgHSV, lower, upper)
	cv2.imshow('img', mask)

purple = {'h_min':133, 's_min':56, 'v_min':0,
		'h_max':159, 's_max':156, 'v_max':255}

def find_purple(img, colourSpec):
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower = np.array([colourSpec['h_min'], colourSpec['s_min'], colourSpec['v_min']])
	upper = np.array([colourSpec['h_max'], colourSpec['s_max'], colourSpec['v_max']])
	mask = cv2.inRange(imgHSV, lower, upper)
	cv2.imshow('img', mask)

while True:
	success, img = cap.read()
	cv2.imshow("Output", img)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
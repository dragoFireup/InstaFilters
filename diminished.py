import cv2
import numpy as np
from math import ceil, floor

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)
	diminished = frame
	h, w, _ = frame.shape
	for i in range(3):
		frame = cv2.resize(frame, (0, 0), fx=0.9, fy=0.9)
		h1, w1, _ = frame.shape
		start_h = (h-h1)/2
		start_w = (w-w1)/2
		end_h = ceil(h - start_h)
		end_w = ceil(w - start_w)
		start_h, start_w = ceil(start_h), ceil(start_w)
		diminished[start_h:end_h, start_w:end_w] = frame
	print(frame.shape)
	cv2.imshow('frame', diminished)
	if cv2.waitKey(1) & 0xff == 27:
		break

cap.release()
cv2.destroyAllWindows()
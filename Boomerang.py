import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('fast.avi',fourcc, 80, (640,480))

frames = []

while cap.isOpened():
	ret, frame = cap.read()

	if ret == False:
		break

	frame = cv2.flip(frame, 1)

	frames.append(frame)
	out.write(frame)
	cv2.imshow('image', frame)
	if cv2.waitKey(1) & 0xff == 27:
		break
	if len(frames) == 80:
		break

for _ in range(10):
	out.write(frames[-1])

for i in frames[::-1]:
	out.write(i)

cap.release()
out.release()
cv2.destroyAllWindows()
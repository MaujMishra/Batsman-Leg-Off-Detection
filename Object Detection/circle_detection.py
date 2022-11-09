import cv2 as cv
import numpy as np

video = "../../Dataset/8qXVwlm9eGQ/303_309.mp4"

vidCap = cv.VideoCapture(video)

while True:
    ret, frame = vidCap.read()

    if not ret: break

    print(ret)
    cv.imshow("frame", frame)


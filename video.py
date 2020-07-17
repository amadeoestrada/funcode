import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
# get size
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
# Define the codec and create VideoWriter object
#fourcc = cv.VideoWriter_fourcc(*'XVID')
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('output.avi', fourcc, 20.0, size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #frame = cv.flip(frame, 0)

    # write the flipped frame
    out.write(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()

cap = cv.VideoCapture('output.avi')
choose = []

while cap.isOpened():
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    k = cv.waitKey(20)   # creates a pause in between frames
    if k == ord('q'):
        break
    elif k == ord('g'):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        choose = 0
    elif k == ord('c') or choose == 1:   # if 'c' is pressed, change to canny
        edges = cv.Canny(frame,100,200)
        cv.imshow('frame', edges)
        choose = 1
    else:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
    # create pauses between videos
    #cv.waitKey(20)  # if is too less, video will be fast.

cap.release()
cv.destroyAllWindows()
